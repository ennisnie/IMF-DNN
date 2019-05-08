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

def test_flatten():
    # Clear the current TensorFlow graph.
    tf.reset_default_graph()
    
    # Stage I: Define the TensorFlow graph describing our computation.
    # In this case the computation is trivial: we just want to flatten
    # a Tensor using the flatten function defined above.
    
    # Our computation will have a single input, x. We don't know its
    # value yet, so we define a placeholder which will hold the value
    # when the graph is run. We then pass this placeholder Tensor to
    # the flatten function; this gives us a new Tensor which will hold
    # a flattened view of x when the graph is run. The tf.device
    # context manager tells TensorFlow whether to place these Tensors
    # on CPU or GPU.
    with tf.device(device):
        x = tf.placeholder(tf.float32)
        x_flat = flatten(x)
    
    # At this point we have just built the graph describing our computation,
    # but we haven't actually computed anything yet. If we print x and x_flat
    # we see that they don't hold any data; they are just TensorFlow Tensors
    # representing values that will be computed when the graph is run.
    print('x: ', type(x), x)
    print('x_flat: ', type(x_flat), x_flat)
    print()
    
    # We need to use a TensorFlow Session object to actually run the graph.
    with tf.Session() as sess:
        # Construct concrete values of the input data x using numpy
        x_np = np.arange(24).reshape((2, 3, 4))
        print('x_np:\n', x_np, '\n')
    
        # Run our computational graph to compute a concrete output value.
        # The first argument to sess.run tells TensorFlow which Tensor
        # we want it to compute the value of; the feed_dict specifies
        # values to plug into all placeholder nodes in the graph. The
        # resulting value of x_flat is returned from sess.run as a
        # numpy array.
        x_flat_np = sess.run(x_flat, feed_dict={x: x_np})
        print('x_flat_np:\n', x_flat_np, '\n')

        # We can reuse the same graph to perform the same computation
        # with different input data
        x_np = np.arange(12).reshape((2, 3, 2))
        print('x_np:\n', x_np, '\n')
        x_flat_np = sess.run(x_flat, feed_dict={x: x_np})
        print('x_flat_np:\n', x_flat_np)
test_flatten()

def two_layer_fc(x, params):
    """
    A fully-connected neural network; the architecture is:
    fully-connected layer -> ReLU -> fully connected layer.
    Note that we only need to define the forward pass here; TensorFlow will take
    care of computing the gradients for us.
    
    The input to the network will be a minibatch of data, of shape
    (N, d1, ..., dM) where d1 * ... * dM = D. The hidden layer will have H units,
    and the output layer will produce scores for C classes.

    Inputs:
    - x: A TensorFlow Tensor of shape (N, d1, ..., dM) giving a minibatch of
      input data.
    - params: A list [w1, w2] of TensorFlow Tensors giving weights for the
      network, where w1 has shape (D, H) and w2 has shape (H, C).
    
    Returns:
    - scores: A TensorFlow Tensor of shape (N, C) giving classification scores
      for the input data x.
    """
    w1, w2 = params  # Unpack the parameters
    x = flatten(x)   # Flatten the input; now x has shape (N, D)
    ly1=tf.matmul(x, w1)
    h = tf.nn.relu(ly1) # Hidden layer: h has shape (N, H)
    scores = tf.matmul(h, w2)        # Compute scores of shape (N, C)
    return scores

def centralnet(h1,h2,params):
    """
    Inputs:
    - h1: A TensorFlow Tensor of shape (N, C) from previous layer
    - params: A list [c1, c2] of TensorFlow Tensors giving weights for the
      network, where have shape (C,M).
    
    Returns:
    - scores: A TensorFlow Tensor of shape (N, M) giving classification scores
      for the input data x.
    """
    w1,w2=params
    h1=flatten(h1) #h1,h2 of shape(N,D)
    h2=flatten(h2)
    hc=tf.matmul(h1,w1)+tf.matmul(h2,w2)#Hidden layer:hc has shape (N,H)
    return hc


def two_layer_fc_test():
    # TensorFlow's default computational graph is essentially a hidden global
    # variable. To avoid adding to this default graph when you rerun this cell,
    # we clear the default graph before constructing the graph we care about.
    tf.reset_default_graph()
    hidden_layer_size = 42

    # Scoping our computational graph setup code under a tf.device context
    # manager lets us tell TensorFlow where we want these Tensors to be
    # placed.
    with tf.device(device):
        # Set up a placehoder for the input of the network, and constant
        # zero Tensors for the network weights. Here we declare w1 and w2
        # using tf.zeros instead of tf.placeholder as we've seen before - this
        # means that the values of w1 and w2 will be stored in the computational
        # graph itself and will persist across multiple runs of the graph; in
        # particular this means that we don't have to pass values for w1 and w2
        # using a feed_dict when we eventually run the graph.
        x = tf.placeholder(tf.float32)
        w1 = tf.zeros((32 * 32 * 3, hidden_layer_size))
        w2 = tf.zeros((hidden_layer_size, 10))
        
        # Call our two_layer_fc function to set up the computational
        # graph for the forward pass of the network.
        scores = two_layer_fc(x, [w1, w2])
    
    # Use numpy to create some concrete data that we will pass to the
    # computational graph for the x placeholder.
    x_np = np.zeros((64, 32, 32, 3))
    with tf.Session() as sess:
        # The calls to tf.zeros above do not actually instantiate the values
        # for w1 and w2; the following line tells TensorFlow to instantiate
        # the values of all Tensors (like w1 and w2) that live in the graph.
        sess.run(tf.global_variables_initializer())
        
        # Here we actually run the graph, using the feed_dict to pass the
        # value to bind to the placeholder for x; we ask TensorFlow to compute
        # the value of the scores Tensor, which it returns as a numpy array.
        scores_np = sess.run(scores, feed_dict={x: x_np})
        print(scores_np.shape)

def centralnet_test():
    # TensorFlow's default computational graph is essentially a hidden global
    # variable. To avoid adding to this default graph when you rerun this cell,
    # we clear the default graph before constructing the graph we care about.
    tf.reset_default_graph()
    hidden_layer_size = 42

    # Scoping our computational graph setup code under a tf.device context
    # manager lets us tell TensorFlow where we want these Tensors to be
    # placed.
    with tf.device(device):
        # Set up a placehoder for the input of the network, and constant
        # zero Tensors for the network weights. Here we declare w1 and w2
        # using tf.zeros instead of tf.placeholder as we've seen before - this
        # means that the values of w1 and w2 will be stored in the computational
        # graph itself and will persist across multiple runs of the graph; in
        # particular this means that we don't have to pass values for w1 and w2
        # using a feed_dict when we eventually run the graph.
        x1 = tf.placeholder(tf.float32)
        x2 = tf.placeholder(tf.float32)
        w1 = tf.zeros((32 * 32 * 3, hidden_layer_size))
        w2 = tf.zeros((hidden_layer_size, 10))
        c1 = tf.zeros((10, 2))
        c2 = tf.zeros((10, 2))
        # Call our two_layer_fc function to set up the computational
        # graph for the forward pass of the network.
        h1 = two_layer_fc(x1, [w1, w2])
        h2 = two_layer_fc(x2, [w1, w2])
        scores=centralnet(h1,h2,[c1,c2])
    
    # Use numpy to create some concrete data that we will pass to the
    # computational graph for the x placeholder.
    x1_np = np.zeros((64, 32, 32, 3))
    x2_np = np.zeros((64, 32, 32, 3))
    with tf.Session() as sess:
        # The calls to tf.zeros above do not actually instantiate the values
        # for w1 and w2; the following line tells TensorFlow to instantiate
        # the values of all Tensors (like w1 and w2) that live in the graph.
        sess.run(tf.global_variables_initializer())
        
        # Here we actually run the graph, using the feed_dict to pass the
        # value to bind to the placeholder for x; we ask TensorFlow to compute
        # the value of the scores Tensor, which it returns as a numpy array.
        scores_np = sess.run(scores, feed_dict={x1: x1_np,x2:x2_np})
        print(scores_np.shape)

def convnet(x, params):
    """
    A three-layer convolutional network with the architecture described above.
    
    Inputs:
    - x: A TensorFlow Tensor of shape (N, H, W, 3) giving a minibatch of images
    - params: A list of TensorFlow Tensors giving the weights and biases for the
      network; should contain the following:
      - conv_w1: TensorFlow Tensor of shape (KH1, KW1, 3, channel_1) giving
        weights for the first convolutional layer.
      - conv_b1: TensorFlow Tensor of shape (channel_1,) giving biases for the
        first convolutional layer.
      - conv_w2: TensorFlow Tensor of shape (KH2, KW2, channel_1, channel_2)
        giving weights for the second convolutional layer
      - conv_b2: TensorFlow Tensor of shape (channel_2,) giving biases for the
        second convolutional layer.
      - fc_w: TensorFlow Tensor giving weights for the fully-connected layer.
        Can you figure out what the shape should be?
      - fc_b: TensorFlow Tensor giving biases for the fully-connected layer.
        Can you figure out what the shape should be?
    """
    conv_w1, conv_b1 = params
    scores = None
#     pass
    x_conv = tf.nn.conv2d(x, conv_w1, [1,1,1,1], "SAME") 
    x_conv_b = tf.nn.bias_add(x_conv,conv_b1) 
    x_relu = tf.nn.relu(x_conv_b)
    return x_relu

def three_layer_convnet_test():
    tf.reset_default_graph()

    with tf.device(device):
        #第一层
        x1 = tf.placeholder(tf.float32)
        x2 = tf.placeholder(tf.float32)
        conv_w1 = tf.zeros((5, 5, 3, 6))
        conv_b1 = tf.zeros((6,))
        #conv_w2 = tf.zeros((3, 3, 6, 9))
        #conv_b2 = tf.zeros((9,))

        h11_conv=convnet(x1,[conv_w1, conv_b1])
        h12_conv=convnet(x2,[conv_w1, conv_b1])
        
        #centralnet1
        fc_w1 = tf.zeros((32 * 32 * 6, 10))
        fc_b1 = tf.zeros((10,))
        
        c11 = tf.zeros((10, 2))
        c12 = tf.zeros((10, 2))
        
        h11_flat = flatten(h11_conv)
        h11 = tf.matmul(h11_flat, fc_w1) + fc_b1
        h12_flat = flatten(h12_conv)
        h12 = tf.matmul(h12_flat, fc_w1) + fc_b1
        
        hc1=centralnet(h11,h12,[c11,c12])
        
        #第二层
        
        conv_w2 = tf.zeros((3, 3, 6, 9))
        conv_b2 = tf.zeros((9,))
        
        h21_conv=convnet(h11_conv,[conv_w2, conv_b2])
        h22_conv=convnet(h12_conv,[conv_w2, conv_b2])
        #centralnet2
        fc_w2 = tf.zeros((32 * 32 * 9, 10))
        fc_b2 = tf.zeros((10,))
        
        c21 = tf.zeros((10, 4))
        c22 = tf.zeros((10, 4))
        cc1 = tf.zeros((2, 4))
        
        h21_flat = flatten(h21_conv)
        h21 = tf.matmul(h21_flat, fc_w2) + fc_b2
        h22_flat = flatten(h22_conv)
        h22 = tf.matmul(h22_flat, fc_w2) + fc_b2
        
        hc2=centralnet(h21,h22,[c21,c22])
        scores=hc2+tf.matmul(hc1,cc1)

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
