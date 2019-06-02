import os
import tensorflow as tf
import numpy as np
import math
import timeit
#import matplotlib.pyplot as plt

def training_step(scores, y, params, learning_rate):
    """
    Set up the part of the computational graph which makes a training step.

    Inputs:
    - scores: TensorFlow Tensor of shape (N, C) giving classification scores for
      the model.
    - y: TensorFlow Tensor of shape (N,) giving ground-truth labels for scores;
      y[i] == c means that c is the correct class for scores[i].
    - params: List of TensorFlow Tensors giving the weights of the model
    - learning_rate: Python scalar giving the learning rate to use for gradient
      descent step.
      
    Returns:
    - loss: A TensorFlow Tensor of shape () (scalar) giving the loss for this
      batch of data; evaluating the loss also performs a gradient descent step
      on params (see above).
    """
    #展开列表
    feed= [i for k in params for i in k]
    # First compute the loss; the first line gives losses for each example in
    # the minibatch, and the second averages the losses across the batch
    losses = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=scores)
    loss = tf.reduce_mean(losses)

    # Compute the gradient of the loss with respect to each parameter of the the
    # network. This is a very magical function call: TensorFlow internally
    # traverses the computational graph starting at loss backward to each element
    # of params, and uses backpropagation to figure out how to compute gradients;
    # it then adds new operations to the computational graph which compute the
    # requested gradients, and returns a list of TensorFlow Tensors that will
    # contain the requested gradients when evaluated.
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

def train_part2(model_fn, init_fn, learning_rate):

    # First clear the default graph
    tf.reset_default_graph()
    is_training = tf.placeholder(tf.bool, name='is_training')
    # Set up the computational graph for performing forward and backward passes,
    # and weight updates.
    with tf.device(device):
        # Set up placeholders for the data and labels
        x1 = tf.placeholder(tf.float32, [None, 32, 32, 3])
        x2 = tf.placeholder(tf.float32, [None, 32, 32, 3])
        
        y = tf.placeholder(tf.int32, [None])
        params = init_fn()           # Initialize the model parameters
        scores = model_fn(x1,x2, params) # Forward pass of the model
        loss = training_step(scores, y, params, learning_rate)

    # Now we actually run the graph many times using the training data
    with tf.Session() as sess:
        # Initialize variables that will live in the graph
        sess.run(tf.global_variables_initializer())
        for t, (x_np, y_np) in enumerate(train_dset):
            # Run the graph on a batch of training data; recall that asking
            # TensorFlow to evaluate loss will cause an SGD step to happen.
            feed_dict = {x1: x_np,x2:x_np, y: y_np}
            loss_np = sess.run(loss, feed_dict=feed_dict)
            
            # Periodically print the loss and check accuracy on the val set
            if t % print_every == 0:
                print('Iteration %d, loss = %.4f' % (t, loss_np))
                check_accuracy(sess, val_dset, x1,x2, scores, is_training)

def check_accuracy(sess, dset, x1,x2, scores, is_training=None):
    """
    Check accuracy on a classification model.
    
    Inputs:
    - sess: A TensorFlow Session that will be used to run the graph
    - dset: A Dataset object on which to check accuracy
    - x: A TensorFlow placeholder Tensor where input images should be fed
    - scores: A TensorFlow Tensor representing the scores output from the
      model; this is the Tensor we will ask TensorFlow to evaluate.
      
    Returns: Nothing, but prints the accuracy of the model
    """
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
    """
    Initialize the weights of a Three-Layer ConvNet, for use with the
    three_layer_convnet function defined above.
    
    Inputs: None
    
    Returns a list containing:
    - conv_w1: TensorFlow Variable giving weights for the first conv layer
    - conv_b1: TensorFlow Variable giving biases for the first conv layer
    - conv_w2: TensorFlow Variable giving weights for the second conv layer
    - conv_b2: TensorFlow Variable giving biases for the second conv layer
    - fc_w: TensorFlow Variable giving weights for the fully-connected layer
    - fc_b: TensorFlow Variable giving biases for the fully-connected layer
    """
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

learning_rate = 3e-3
train_part2(conv_centralnet, conv_centralnet_init, learning_rate)