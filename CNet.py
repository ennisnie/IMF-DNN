import os
import tensorflow as tf
import numpy as np
import math
import timeit
#import matplotlib.pyplot as plt

class CentralNet(tf.keras.Model):
    def __init__(self, channel_1, channel_2,channel_3,channel_4, num_classes,c1,c2,c3,c4):
        super().__init__()

         #pass
        initializer = tf.variance_scaling_initializer(scale=2.0)
        self.conv1 = tf.layers.Conv2D(channel_1, kernel_size=(3,3), 
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer())
        self.conv2 = tf.layers.Conv2D(channel_1, kernel_size=(3,3), 
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer())
        self.maxpool1 = tf.layers.MaxPooling2D(pool_size = (2,2), 
                               strides = (2,2), padding='SAME')
        
        self.conv3 = tf.layers.Conv2D(channel_2, kernel_size=(3,3), 
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer())        
        self.conv4 = tf.layers.Conv2D(channel_2, kernel_size=(3,3), 
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer())
        self.maxpool2 = tf.layers.MaxPooling2D(pool_size = (2,2), 
                               strides = (2,2), padding='SAME')
        
        self.conv5 = tf.layers.Conv2D(channel_3, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-256
        self.conv6 = tf.layers.Conv2D(channel_3, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-256
        self.conv7 = tf.layers.Conv2D(channel_3, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-256
        self.maxpool3 = tf.layers.MaxPooling2D(pool_size = (2,2), 
                               strides = (2,2), padding='SAME')

        self.conv8 = tf.layers.Conv2D(channel_4, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-512
        self.conv9 = tf.layers.Conv2D(channel_4, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-512
        self.conv10 = tf.layers.Conv2D(channel_4, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-512
        self.maxpool4 = tf.layers.MaxPooling2D(pool_size = (2,2), 
                               strides = (2,2), padding='SAME')

        self.conv11 = tf.layers.Conv2D(channel_4, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-512
        self.conv12 = tf.layers.Conv2D(channel_4, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-512
        self.conv13 = tf.layers.Conv2D(channel_4, kernel_size=(3,3),
                                      strides=(1,1),padding="SAME",
                                      activation = tf.nn.relu,use_bias=True,
                                      kernel_initializer = initializer,
                                      bias_initializer=tf.zeros_initializer()) # conv3-512
        self.maxpool5 = tf.layers.MaxPooling2D(pool_size = (2,2), 
                               strides = (2,2), padding='SAME')
                                     
        self.fc4c1 = tf.layers.Dense(c1, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.c14c2 = tf.layers.Dense(c2, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.fc4c2 = tf.layers.Dense(c2, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.c24c3 = tf.layers.Dense(c3, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.fc4c3 = tf.layers.Dense(c3, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.c34c4 = tf.layers.Dense(c4, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.fc4c4 = tf.layers.Dense(c4, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        self.c44c5 = tf.layers.Dense(4096, activation=tf.nn.relu,use_bias=False,
                                  kernel_initializer=initializer,
                                  bias_initializer=tf.zeros_initializer())
        
        self.flatten = tf.keras.layers.Flatten()
        
        self.fc1=tf.layers.Dense(4096, activation = tf.nn.relu, 
                        kernel_initializer=initializer)
        self.fc2=tf.layers.Dense(4096, activation = tf.nn.relu, 
                        kernel_initializer=initializer)
        self.fc3=tf.layers.Dense(1000, activation = tf.nn.relu, 
                        kernel_initializer=initializer)
        self.fc4=tf.layers.Dense(num_classes, activation = None, 
                        kernel_initializer=initializer)
     
    def call(self, x1,x2, training=None):
        scores = None
        ###

        x1_conv1 = self.conv1(x1)
        x1_conv2 = self.conv2(x1_conv1)
        x1_maxpool1 = self.maxpool1(x1_conv2)
        h1_x1=self.flatten(x1_maxpool1)
        x2_conv1 = self.conv1(x2)
        x2_conv2 = self.conv2(x2_conv1)
        x2_maxpool1 = self.maxpool1(x2_conv2)
        h1_x2=self.flatten(x2_maxpool1)
        hc1=self.fc4c1(h1_x1)+self.fc4c1(h1_x2)
        ##conv3-64
        x1_conv3 = self.conv3(x1_maxpool1)
        x1_conv4 = self.conv4(x1_conv3)
        x1_maxpool2 = self.maxpool2(x1_conv4)
        h2_x1=self.flatten(x1_maxpool2)
        x2_conv3 = self.conv3(x2_maxpool1)
        x2_conv4 = self.conv4(x2_conv3)
        x2_maxpool2 = self.maxpool2(x2_conv4)
        h2_x2=self.flatten(x2_maxpool2)
        hc2=self.fc4c2(h2_x1)+self.fc4c2(h2_x2)+self.c14c2(hc1)
        ##conv3-128
        x1_conv5 = self.conv5(x1_maxpool2)
        x1_conv6 = self.conv6(x1_conv5)
        x1_conv7 = self.conv7(x1_conv6)
        x1_maxpool3 = self.maxpool3(x1_conv7)
        h3_x1=self.flatten(x1_maxpool3)
        x2_conv5 = self.conv5(x2_maxpool2)
        x2_conv6 = self.conv6(x2_conv5)
        x2_conv7= self.conv7(x2_conv6)
        x2_maxpool3= self.maxpool3(x2_conv7)
        h3_x2=self.flatten(x2_maxpool3)
        hc3=self.fc4c3(h3_x1)+self.fc4c3(h3_x2)+self.c24c3(hc2)
        ##conv3-256
        x1_conv8 = self.conv8(x1_maxpool3)
        x1_conv9 = self.conv9(x1_conv8)
        x1_conv10 = self.conv10(x1_conv9)
        x1_maxpool4 = self.maxpool4(x1_conv10)
        h4_x1=self.flatten(x1_maxpool4)
        x2_conv8 = self.conv8(x2_maxpool3)
        x2_conv9 = self.conv9(x2_conv8)
        x2_conv10 = self.conv10(x2_conv9)
        x2_maxpool4= self.maxpool4(x2_conv10)
        h4_x2=self.flatten(x2_maxpool4)
        hc4=self.fc4c4(h4_x1)+self.fc4c4(h4_x2)+self.c34c4(hc3)
        ##conv3-512
        x1_conv11 = self.conv11(x1_maxpool4)
        x1_conv12 = self.conv12(x1_conv11)
        x1_conv13 = self.conv13(x1_conv12)
        x1_maxpool5 = self.maxpool5(x1_conv13)
        h5_x1=self.flatten(x1_maxpool5)
        x2_conv11 = self.conv11(x2_maxpool4)
        x2_conv12 = self.conv12(x2_conv11)
        x2_conv13 = self.conv13(x2_conv12)
        x2_maxpool5= self.maxpool5(x2_conv13)
        h5_x2=self.flatten(x2_maxpool5)
        hc5=self.fc1(h5_x1)+self.fc1(h5_x2)+self.c44c5(hc4)    #x1 and x2 have the same size    #4096
        dense2=self.fc2(hc5) #4096
        dense3=self.fc3(dense2)#1000
        scores= self.fc4(dense3)#num_classes
        return scores

class CentralNet_Simple(tf.keras.Model):
    def __init__(self, channel_1, channel_2, num_classes,c1):
        super().__init__()
        
        #a three-layer ConvNet.
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
    
    channel_1, channel_2,channel_3,channel_4, num_classes,c1,c2,c3,c4=64,128,256,512,10,64,128,256,512
    model = CentralNet(channel_1, channel_2,channel_3,channel_4, num_classes,c1,c2,c3,c4)

    with tf.device('/cpu:0'):
        x1 = tf.zeros((64, 32, 32,3))
        x2 = tf.zeros((64, 32, 32,3))
        scores = model(x1,x2)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        scores_np = sess.run(scores)
        print(scores_np.shape)