import argparse
import importlib
import os
import sys
import time

# import matplotlib.pyplot as plt
import numpy as np
import scipy

import CNet
import provider
import tensorflow as tf
#from helper import str2bool




def Evaluate(model_init_fn,device,BATCH_SIZE):
    with tf.device(device):
        
        data_input = provider.DVR_FMAP_Provider_rotation()

        imgs_pl, pts_pl, labels_pl = CNet.placeholder_inputs(BATCH_SIZE)
        x1=imgs_pl
        x2=imgs_pl
        y=labels_pl

        is_training = tf.placeholder(tf.bool, shape=())
        print(is_training)

        # Use the model function to build the forward pass.
        scores = model_init_fn(x1,x2, is_training)

        # Compute the loss like we did in Part II
        loss = CNet.get_loss(scores,y)

        # Add ops to save and restore all the variables.
        saver = tf.train.Saver()

    # Create a session
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    config.allow_soft_placement = True
    config.log_device_placement = True
    sess = tf.Session(config=config)

    # Restore variables from disk.
    saver.restore(sess, "log/model_best.ckpt")
    print("Model restored.")

    ops = {'x1': x1,
            'x2': x2,
            'y': y,
            'is_training': is_training,
            'scores': scores,
            'loss': loss}

    eval_one_epoch(sess, ops, data_input, BATCH_SIZE)


def eval_one_epoch(sess, ops, data_input, BATCH_SIZE):
    """ ops: dict mapping from string to tf ops """
    is_training = False
    loss_sum = 0

    num_batches = data_input.num_val // BATCH_SIZE
    acc_a_sum = [0] * 5
    acc_s_sum = [0] * 5

    preds = []
    labels_total = []
    acc_a = [0] * 5
    acc_s = [0] * 5
    for batch_idx in range(num_batches):

        imgs,fmaps, labels = data_input.load_one_batch(BATCH_SIZE, "val")

        feed_dict = {ops['x1']: imgs,
                     ops['x2']: fmaps,
                     ops['y']: labels,
                     ops['is_training']: is_training}

        loss_val, pred_val = sess.run([ops['loss'], ops['scores']],
                                    feed_dict=feed_dict)

        preds.append(pred_val)
        labels_total.append(labels)
        loss_sum += np.mean(np.square(np.subtract(pred_val, labels)))
        for i in range(5):
            acc_a[i] = np.mean(np.abs(np.subtract(pred_val[:, 1], labels[:, 1])) < (1.0 * (i+1) / 180 * scipy.pi))
            acc_a_sum[i] += acc_a[i]
            acc_s[i] = np.mean(np.abs(np.subtract(pred_val[:, 0], labels[:, 0])) < (1.0 * (i+1) / 20))
            acc_s_sum[i] += acc_s[i]

    print('eval mean loss: %f' % (loss_sum / float(num_batches)))
    for i in range(5):
        print('eval accuracy (angle-%d): %f' % (float(i+1), (acc_a_sum[i] / float(num_batches))))
        print('eval accuracy (speed-%d): %f' % (float(i+1), (acc_s_sum[i] / float(num_batches))))

    preds = np.vstack(preds)
    labels = np.vstack(labels_total)

    
    a_error, s_error = mean_max_error(preds, labels, get_dicts())
    print('eval error (mean-max): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))
               
    a_error, s_error = max_error(preds, labels)
    print('eval error (max): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))
    a_error, s_error = mean_topk_error(preds, labels, 5)
    print('eval error (mean-top5): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))
    a_error, s_error = mean_error(preds, labels)
    print('eval error (mean): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))
    
    print (preds.shape, labels.shape)

    # plot_acc(preds, labels)


def test():
    with tf.device('/gpu:'+str(GPU_INDEX)):
        if '_pn' in MODEL_FILE:
            data_input = provider.Provider2()
            imgs_pl, pts_pl, labels_pl = MODEL.placeholder_inputs(BATCH_SIZE)
            imgs_pl = [imgs_pl, pts_pl]
        elif '_io' in MODEL_FILE:
            data_input = provider.Provider2()
            imgs_pl, labels_pl = MODEL.placeholder_inputs(BATCH_SIZE)
        else:
            raise NotImplementedError


        is_training_pl = tf.placeholder(tf.bool, shape=())
        print(is_training_pl)

        # Get model and loss
        pred = MODEL.get_model(imgs_pl, is_training_pl)

        loss = MODEL.get_loss(pred, labels_pl)

        # Add ops to save and restore all the variables.
        saver = tf.train.Saver()

    # Create a session
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    config.allow_soft_placement = True
    config.log_device_placement = True
    sess = tf.Session(config=config)

    # Restore variables from disk.
    saver.restore(sess, MODEL_PATH)
    log_string("Model restored.")

    ops = {'imgs_pl': imgs_pl,
            'labels_pl': labels_pl,
            'is_training_pl': is_training_pl,
            'pred': pred,
            'loss': loss}

    test_one_epoch(sess, ops, data_input)


def test_one_epoch(sess, ops, data_input):
    """ ops: dict mapping from string to tf ops """
    is_training = False
    loss_sum = 0

    num_batches = data_input.num_test // BATCH_SIZE
    acc_a_sum = [0] * 5
    acc_s_sum = [0] * 5

    preds = []
    labels_total = []
    acc_a = [0] * 5
    acc_s = [0] * 5
    for batch_idx in range(num_batches):
        if "_io" in MODEL_FILE:
            imgs, labels = data_input.load_one_batch(BATCH_SIZE, reader_type="io")
            if "resnet" in MODEL_FILE or "inception" in MODEL_FILE or "densenet" in MODEL_FILE:
                imgs = MODEL.resize(imgs)
            feed_dict = {ops['imgs_pl']: imgs,
                         ops['labels_pl']: labels,
                         ops['is_training_pl']: is_training}
        else:
            imgs, others, labels = data_input.load_one_batch(BATCH_SIZE)
            if "resnet" in MODEL_FILE or "inception" in MODEL_FILE or "densenet" in MODEL_FILE:
                imgs = MODEL.resize(imgs)
            feed_dict = {ops['imgs_pl'][0]: imgs,
                         ops['imgs_pl'][1]: others,
                         ops['labels_pl']: labels,
                         ops['is_training_pl']: is_training}

        loss_val, pred_val = sess.run([ops['loss'], ops['pred']],
                                    feed_dict=feed_dict)

        preds.append(pred_val)
        labels_total.append(labels)
        loss_sum += np.mean(np.square(np.subtract(pred_val, labels)))
        for i in range(5):
            acc_a[i] = np.mean(np.abs(np.subtract(pred_val[:, 1], labels[:, 1])) < (1.0 * (i+1) / 180 * scipy.pi))
            acc_a_sum[i] += acc_a[i]
            acc_s[i] = np.mean(np.abs(np.subtract(pred_val[:, 0], labels[:, 0])) < (1.0 * (i+1) / 20))
            acc_s_sum[i] += acc_s[i]

    log_string('test mean loss: %f' % (loss_sum / float(num_batches)))
    for i in range(5):
        log_string('test accuracy (angle-%d): %f' % (float(i+1), (acc_a_sum[i] / float(num_batches))))
        log_string('test accuracy (speed-%d): %f' % (float(i+1), (acc_s_sum[i] / float(num_batches))))

    preds = np.vstack(preds)
    labels = np.vstack(labels_total)

    a_error, s_error = mean_max_error(preds, labels, dicts=get_dicts())
    log_string('test error (mean-max): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))
    a_error, s_error = max_error(preds, labels)
    log_string('test error (max): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))
    a_error, s_error = mean_topk_error(preds, labels, 5)
    log_string('test error (mean-top5): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))
    a_error, s_error = mean_error(preds, labels)
    log_string('test error (mean): angle:%.2f speed:%.2f' %
               (a_error / scipy.pi * 180, s_error * 20))

    print (preds.shape, labels.shape)
    np.savetxt(os.path.join(TEST_RESULT_DIR, "preds_val.txt"), preds)
    np.savetxt(os.path.join(TEST_RESULT_DIR, "labels_val.txt"), labels)
    # plot_acc(preds, labels)


def plot_acc(preds, labels, counts = 100):
    a_list = []
    s_list = []
    for i in range(counts):
        acc_a = np.abs(np.subtract(preds[:, 1], labels[:, 1])) < (20.0 / 180 * scipy.pi / counts * i)
        a_list.append(np.mean(acc_a))

    for i in range(counts):
        acc_s = np.abs(np.subtract(preds[:, 0], labels[:, 0])) < (15.0 / 20 / counts * i)
        s_list.append(np.mean(acc_s))

    print (len(a_list), len(s_list))
    a_xaxis = [20.0 / counts * i for i in range(counts)]
    s_xaxis = [15.0 / counts * i for i in range(counts)]

    auc_angle = np.trapz(np.array(a_list), x=a_xaxis) / 20.0
    auc_speed = np.trapz(np.array(s_list), x=s_xaxis) / 15.0

    plt.style.use('ggplot')
    plt.figure()
    plt.plot(a_xaxis, np.array(a_list), label='Area Under Curve (AUC): %f' % auc_angle)
    plt.legend(loc='best')
    plt.xlabel("Threshold (angle)")
    plt.ylabel("Validation accuracy")
    plt.savefig(os.path.join(RESULT_DIR, "acc_angle.png"))
    plt.figure()
    plt.plot(s_xaxis, np.array(s_list), label='Area Under Curve (AUC): %f' % auc_speed)
    plt.xlabel("Threshold (speed)")
    plt.ylabel("Validation accuracy")
    plt.legend(loc='best')
    plt.savefig(os.path.join(RESULT_DIR, 'acc_spped.png'))

def plot_acc_from_txt(counts=100):
    preds = np.loadtxt(os.path.join(RESULT_DIR, "test/preds_val.txt"))
    labels = np.loadtxt(os.path.join(RESULT_DIR, "test/labels_val.txt"))
    print (preds.shape, labels.shape)
    plot_acc(preds, labels, counts)

def get_dicts(description="val"):
    if description == "train":
        raise NotImplementedError
    elif description == "val": # batch_size == 8
        return [120] * 4 + [111] + [120] +[41]
    elif description == "test": # batch_size == 8
        return [120] * 9 + [116] + [120] * 4 + [106] + [120] * 4 + [114 - 114 % 8]
    else:
        raise NotImplementedError

def mean_max_error(preds, labels, dicts):
    cnt = 0
    a_error = 0
    s_error = 0
    for i in dicts:
        print (preds.shape, cnt, cnt + i)
        a_error += np.max(np.abs(preds[cnt:cnt+i, 1] - labels[cnt:cnt+i, 1]))
        s_error += np.max(np.abs(preds[cnt:cnt+i, 0] - labels[cnt:cnt+i, 0]))
        cnt += i
    return a_error / float(len(dicts)), s_error / float(len(dicts))

def max_error(preds, labels):
    return np.max(np.abs(preds[:,1] - labels[:,1])), np.max(np.abs(preds[:, 0] - labels[:, 0]))

def mean_error(preds, labels):
    return np.mean(np.abs(preds[:,1] - labels[:,1])), np.mean(np.abs(preds[:,0] - labels[:,0]))

def mean_topk_error(preds, labels, k):
    a_error = np.abs(preds[:,1] - labels[:,1])
    s_error = np.abs(preds[:,0] - labels[:,0])
    return np.mean(np.sort(a_error)[::-1][0:k]), np.mean(np.sort(s_error)[::-1][0:k])

if __name__ == "__main__":
    if FLAGS.test: test()
    else: evaluate()
    # plot_acc_from_txt()
