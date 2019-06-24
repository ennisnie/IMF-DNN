import os
import tensorflow as tf
import numpy as np
import math
import timeit
#import matplotlib.pyplot as plt

class CentralNet(tf.keras.Model):
    def __init__(self, channel_1, channel_2, num_classes,c1):
        super().__init__()
        ########################################################################
        # TODO: Implement the __init__ method for a three-layer ConvNet. You   #
        # should instantiate layer objects to be used in the forward pass.     #
        ########################################################################
#         pass
        initializer = tf.variance_scaling_initializer(scale=2.0)
        self.conv1 = tf.layers.Conv2D(channel_1, kernel_size=(5,5), 
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer())
        self.conv2 = tf.layers.Conv2D(channel_2, kernel_size=(3,3), 
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer())
        self.fc4c1 = tf.layers.Dense(c1, activation=None,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.fc4c2 = tf.layers.Dense(num_classes, activation=None,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.fc4cc = tf.layers.Dense(num_classes, activation=None,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.fc4conv = tf.layers.Dense(num_classes, activation=None,use_bias=True,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.flatten = tf.keras.layers.Flatten()
                                      
        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################

    
    def call(self, x1,x2, training=None):
        scores = None
        ########################################################################
        # TODO: Implement the forward pass for a three-layer ConvNet. You      #
        # should use the layer objects defined in the __init__ method.         #
        ########################################################################
#         pass
        x1_conv1 = self.conv1(x1)
        h1=self.flatten(x1_conv1)
        x2_conv1 = self.conv1(x2)
        h2=self.flatten(x2_conv1)
        hc1=self.fc4c1(h1)+self.fc4c1(h2)
        ##
        x1_conv2 = self.conv2(x1_conv1)
        x2_conv2 = self.conv2(x2_conv1)
        x1_flat = self.flatten(x1_conv2)
        x2_flat = self.flatten(x2_conv2)
        hc2=self.fc4c2(x1_flat)+self.fc4c2(x2_flat)+self.fc4cc(hc1)
        scores = self.fc4conv(x1_flat)+self.fc4conv(x2_flat)+hc2
        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################        
        return scores

def placeholder_inputs(batch_size, img_rows=66, img_cols=200, points=16384, separately=False):
    imgs_pl = tf.placeholder(tf.float32, shape=(batch_size, img_rows, img_cols, 3))
    pts_pl = tf.placeholder(tf.float32, shape=(batch_size, points, 3))
    if separately:
        speeds_pl = tf.placeholder(tf.float32, shape=(batch_size))
        angles_pl = tf.placeholder(tf.float32, shape=(batch_size))
        labels_pl = [speeds_pl, angles_pl]
    labels_pl = tf.placeholder(tf.float32, shape=(batch_size, 2))
    return imgs_pl, pts_pl, labels_pl


def get_loss(pred, label, l2_weight=0.0001):
    diff = tf.square(tf.subtract(pred, label))
    train_vars = tf.trainable_variables()
    l2_loss = tf.add_n([tf.nn.l2_loss(v) for v in train_vars[1:]]) * l2_weight
    loss = tf.reduce_mean(diff + l2_loss)

    return loss


if __name__ == '__main__':
    tf.reset_default_graph()
    
    channel_1, channel_2, num_classes,c1 = 12, 8, 10, 4
    model = CentralNet(channel_1, channel_2, num_classes,c1)
    with tf.device('/cpu:0'):
        x1 = tf.zeros((64, 32, 32,3))
        x2 = tf.zeros((64, 32, 32,3))
        scores = model(x1,x2)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        scores_np = sess.run(scores)
        print(scores_np.shape)