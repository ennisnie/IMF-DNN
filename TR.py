import os
import sys
import tensorflow as tf
import numpy as np
import math
import timeit
import scipy

import CNet
import provider
    
def train_part34(model_init_fn, optimizer_init_fn, MAX_EPOCH, device, BATCH_SIZE):

    tf.reset_default_graph()    
    with tf.device(device):

        data_input = provider.DVR_FMAP_Provider()

        imgs_pl, pts_pl, labels_pl = CNet.placeholder_inputs(BATCH_SIZE)
        x1=imgs_pl
        x2=imgs_pl
        y=labels_pl
        
        is_training = tf.placeholder(tf.bool, name='is_training')
        
        # Use the model function to build the forward pass.
        scores = model_init_fn(x1,x2, is_training)

        # Compute the loss like we did in Part II
        loss = CNet.get_loss(scores,y)
        #saver = tf.train.Saver()

        # Use the optimizer_fn to construct an Optimizer, then use the optimizer
        # to set up the training step. Asking TensorFlow to evaluate the
        # train_op returned by optimizer.minimize(loss) will cause us to make a
        # single update step using the current minibatch of data.
        
        # Note that we use tf.control_dependencies to force the model to run
        # the tf.GraphKeys.UPDATE_OPS at each training step. tf.GraphKeys.UPDATE_OPS
        # holds the operators that update the states of the network.
        # For example, the tf.layers.batch_normalization function adds the running mean
        # and variance update operators to tf.GraphKeys.UPDATE_OPS.
        optimizer = optimizer_init_fn()
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(update_ops):
            train_op = optimizer.minimize(loss)

    # Now we can run the computational graph many times to train the model.
    # When we call sess.run we ask it to evaluate train_op, which causes the
    # model to update.
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        ops = {'x1': x1,
               'x2': x2,
               'y': y,
               'is_training': is_training,
               'train_op': train_op,
               'scores': scores,
               'loss': loss}
        
        for epoch in range(MAX_EPOCH):
            print('Starting epoch %d' % epoch)
            #for x_np, y_np in train_dset:
            #    feed_dict = {x1: x_np,x2:x_np, y: y_np, is_training:1}
            #    loss_np, _ = sess.run([loss, train_op], feed_dict=feed_dict)
            #    if t % print_every == 0:
            #        print('Iteration %d, loss = %.4f' % (t, loss_np))
            #        check_accuracy(sess, val_dset, x1,x2, scores, is_training=is_training)
            #        print()
            #    t += 1
            train_one_epoch(sess, ops, data_input, BATCH_SIZE)
            eval_one_epoch(sess, ops, data_input, BATCH_SIZE)

            # Save the variables to disk.
            #if epoch % 10 == 0:
                #save_path = saver.save(sess, os.path.join(LOG_DIR, "model.ckpt"))
                #log_string("Model saved in file: %s" % save_path)

def train_one_epoch(sess, ops, data_input, BATCH_SIZE):
    """ ops: dict mapping from string to tf ops """
    is_training = True
    num_batches = data_input.num_train // BATCH_SIZE
    loss_sum = 0
    acc_a_sum = 0
    acc_s_sum = 0

    for batch_idx in range(num_batches):

        imgs, fmaps,labels = data_input.load_one_batch(BATCH_SIZE, "train")
        feed_dict = {ops['x1']: imgs,
                     ops['x2']: fmaps,
                     ops['y']: labels,
                     ops['is_training']: is_training}

        _, loss_val, pred_val = sess.run([ops['train_op'],
                                         ops['loss'],
                                         ops['scores']],
                                        feed_dict=feed_dict)

        loss_sum, acc_a_sum, acc_s_sum=check_accuracy(loss_sum, acc_a_sum, acc_s_sum,pred_val,labels)

    print('mean loss: %f' % (loss_sum / float(num_batches)))
    print('accuracy (angle): %f' % (acc_a_sum / float(num_batches)))
    print('accuracy (speed): %f' % (acc_s_sum / float(num_batches)))


def eval_one_epoch(sess, ops, data_input, BATCH_SIZE):
    """ ops: dict mapping from string to tf ops """
    is_training = False
    loss_sum = 0

    num_batches = data_input.num_val // BATCH_SIZE
    loss_sum = 0
    acc_a_sum = 0
    acc_s_sum = 0

    for batch_idx in range(num_batches):
        imgs, fmaps,labels = data_input.load_one_batch(BATCH_SIZE, "val")
        feed_dict = {ops['x1']: imgs,
                     ops['x2']: fmaps,
                     ops['y']: labels,
                     ops['is_training']: is_training}

        _, loss_val, pred_val = sess.run([ops['train_op'],
                                         ops['loss'],
                                         ops['scores']],
                                        feed_dict=feed_dict)
        
        loss_sum, acc_a_sum, acc_s_sum=check_accuracy(loss_sum, acc_a_sum, acc_s_sum,pred_val,labels)

    print('eval mean loss: %f' % (loss_sum / float(num_batches)))
    print('eval accuracy (angle): %f' % (acc_a_sum / float(num_batches)))
    print('eval accuracy (speed): %f' % (acc_s_sum / float(num_batches)))

def  check_accuracy(loss_sum, acc_a_sum, acc_s_sum,pred_val,labels):
    loss_sum += np.mean(np.square(np.subtract(pred_val, labels)))
    acc_a = np.abs(np.subtract(pred_val[:, 1], labels[:, 1])) < (5.0 / 180 * scipy.pi)
    acc_a = np.mean(acc_a)
    acc_a_sum += acc_a
    acc_s = np.abs(np.subtract(pred_val[:, 0], labels[:, 0])) < (5.0 / 20)
    acc_s = np.mean(acc_s)
    acc_s_sum += acc_s
    return loss_sum, acc_a_sum, acc_s_sum