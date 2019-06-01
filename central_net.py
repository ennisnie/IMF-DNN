import os
import tensorflow as tf
import numpy as np
import math
import timeit
import matplotlib.pyplot as plt

# Set up some global variables
USE_GPU = False

if USE_GPU:
    device = '/device:GPU:0'
else:
    device = '/cpu:0'

# Constant to control how often we print when training models
print_every = 100

print('Using device: ', device)

def flatten(x):
    """    
    Input:
    - TensorFlow Tensor of shape (N, D1, ..., DM)
    
    Output:
    - TensorFlow Tensor of shape (N, D1 * ... * DM)
    """
    N = tf.shape(x)[0]
    return tf.reshape(x, (N, -1))
    
def fc(x, w):

    x = flatten(x)   # Flatten the input; now x has shape (N, D)
    ly=tf.matmul(x, w)
    out = tf.nn.relu(ly) # Hidden layer: h has shape (N, H)
    return out

def convlayer(x, params):
    conv_w, conv_b = params
    x_conv = tf.nn.conv2d(x, conv_w, [1,1,1,1], "SAME") 
    x_conv_b = tf.nn.bias_add(x_conv,conv_b) 
    out = tf.nn.relu(x_conv_b)
    return out

def three_layer_convnet(x, params):
    conv_w1, conv_b1, conv_w2, conv_b2, fc_w, fc_b = params
    scores = None
    ly1=convlayer(x,[conv_w1,conv_b1])
    ly2=convlayer(ly1,[conv_w2,conv_b2])
    x_flat = flatten(ly2)
    scores = tf.matmul(x_flat, fc_w) + fc_b

    return ly1,ly2,scores

def centralnet(h1,h2,params):
    w1,w2=params
    h1=flatten(h1) #h1,h2 of shape(N,D)
    h2=flatten(h2)
    hc=tf.matmul(h1,w1)+tf.matmul(h2,w2)#Hidden layer:hc has shape (N,H)
    return hc

def conv_centralnet(x1,x2,params):
    feed1,feed2,feedc=params
    #convnet
    h11,h21,out1 = three_layer_convnet(x1, feed1)
    h12,h22,out2 = three_layer_convnet(x2, feed2)

    #centralnet
    c11,c12,c21,c22,cc1=feedc
    hc1=centralnet(h11,h12,[c11,c12])
    hc2=centralnet(h21,h22,[c21,c22])+tf.matmul(hc1,cc1)

    #final
    scores= out1+out2+hc2
    return scores

def three_layer_convnet_test():
    tf.reset_default_graph()

    with tf.device(device):
        #conv1
        x1 = tf.placeholder(tf.float32)
        conv1_w1 = tf.zeros((5, 5, 3, 6))
        conv1_b1 = tf.zeros((6,))
        conv1_w2 = tf.zeros((3, 3, 6, 9))
        conv1_b2 = tf.zeros((9,))
        fc1_w = tf.zeros((32 * 32 * 9, 10))
        fc1_b = tf.zeros((10,))
        feed1 = [conv1_w1, conv1_b1, conv1_w2, conv1_b2, fc1_w, fc1_b]
        
        #conv2
        
        x2 = tf.placeholder(tf.float32)
        conv2_w1 = tf.zeros((5, 5, 3, 6))
        conv2_b1 = tf.zeros((6,))
        conv2_w2 = tf.zeros((3, 3, 6, 9))
        conv2_b2 = tf.zeros((9,))
        fc2_w = tf.zeros((32 * 32 * 9, 10))
        fc2_b = tf.zeros((10,))
        feed2 = [conv2_w1, conv2_b1, conv2_w2, conv2_b2, fc2_w, fc2_b]

        
        #centralnet
        c11 = tf.zeros((32*32*6, 4))
        c12 = tf.zeros((32*32*6, 4))
        c21 = tf.zeros((32*32*9, 10))
        c22 = tf.zeros((32*32*9, 10))
        cc1 = tf.zeros((4, 10))
 
        feedc=[c11,c12,c21,c22,cc1]

        #final
        
        params=[feed1,feed2,feedc]
        scores=conv_centralnet(x1,x2,params)
    # Inputs to convolutional layers are 4-dimensional arrays with shape
    # [batch_size, height, width, channels]
    x1_np = np.zeros((64, 32, 32, 3))
    x2_np = np.zeros((64, 32, 32, 3))   
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        scores_np = sess.run(scores, feed_dict={x1: x1_np,x2:x2_np})
        print('scores_np has shape: ', scores_np.shape)

with tf.device('/cpu:0'):
    three_layer_convnet_test()