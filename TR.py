import os
import tensorflow as tf
import numpy as np
import math
import timeit
#import matplotlib.pyplot as plt
USE_GPU = True

if USE_GPU:
    device = '/device:GPU:0'
else:
    device = '/cpu:0'

def training_step(scores, y, params, learning_rate):

    #展开列表
    feed= [i for k in params for i in k]
    # First compute the loss; the first line gives losses for each example in
    # the minibatch, and the second averages the losses across the batch
    losses = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=scores)
    loss = tf.reduce_mean(losses)

    grad_params = tf.gradients(loss, feed)
    
    # Make a gradient descent step on all of the model parameters.
    new_weights = []   
    for w, grad_w in zip(feed, grad_params):
        new_w = tf.assign_sub(w, learning_rate * grad_w)
        new_weights.append(new_w)

    # Insert a control dependency so that evaluting the loss causes a weight
    # update to happen; see the discussion above.
    with tf.control_dependencies(new_weights):
        return tf.identity(loss)


def check_accuracy(sess, dset, x1,x2, scores, is_training=None):

    num_correct, num_samples = 0, 0
    for x_batch, y_batch in dset:
        feed_dict = {x1: x_batch,x2:x_batch, is_training: 0}
        scores_np = sess.run(scores, feed_dict=feed_dict)
        y_pred = scores_np.argmax(axis=1)
        num_samples += x_batch.shape[0]
        num_correct += (y_pred == y_batch).sum()
    acc = float(num_correct) / num_samples
    print('Got %d / %d correct (%.2f%%)' % (num_correct, num_samples, 100 * acc))

def kaiming_normal(shape):
    if len(shape) == 2:
        fan_in, fan_out = shape[0], shape[1]
    elif len(shape) == 4:
        fan_in, fan_out = np.prod(shape[:3]), shape[3]
    return tf.random_normal(shape) * np.sqrt(2.0 / fan_in)

def conv_centralnet_init():
    params = None
    #conv1
    conv1_w1 = tf.Variable(kaiming_normal([5,5,3,32]))
    conv1_b1 = tf.Variable(tf.zeros(32))
    conv1_w2 = tf.Variable(kaiming_normal([3,3,32,16]))
    conv1_b2 = tf.Variable(tf.zeros(16))
    fc1_w = tf.Variable(kaiming_normal((16 * 32 * 32, 10)))
    fc1_b = tf.Variable(tf.zeros(10))
    #conv2
    conv2_w1 = tf.Variable(kaiming_normal([5,5,3,32]))
    conv2_b1 = tf.Variable(tf.zeros(32))
    conv2_w2 = tf.Variable(kaiming_normal([3,3,32,16]))
    conv2_b2 = tf.Variable(tf.zeros(16))
    fc2_w = tf.Variable(kaiming_normal((16 * 32 * 32, 10)))
    fc2_b = tf.Variable(tf.zeros(10))
    #centralnet
    c11 = tf.Variable(kaiming_normal((32 * 32 * 32, 4)))
    c12 = tf.Variable(kaiming_normal((32 * 32 * 32, 4)))
    c21 = tf.Variable(kaiming_normal((16 * 32 * 32, 10)))
    c22 = tf.Variable(kaiming_normal((16 * 32 * 32, 10)))
    cc1 = tf.Variable(kaiming_normal((4, 10)))
    
    feed1 = [conv1_w1, conv1_b1, conv1_w2, conv1_b2, fc1_w, fc1_b]
    feed2 = [conv2_w1, conv2_b1, conv2_w2, conv2_b2, fc2_w, fc2_b]
    feedc=[c11,c12,c21,c22,cc1]
    params=[feed1,feed2,feedc]
    
    return params
