import numpy as np


# Training Utils ===========================================

def minibatch(x, batchsize=256, shuffle=True):
    pass


# Padding Utils ============================================

def calc_pad_dims_2D(X_shape, out_dim, kernel_shape, stride, dilation=0):
    pass

def calc_pad_dims_1D(X_shape, l_out, kernel_width, stride, dilation=0, causal=False):
    pass

def pad1D(X, pad, kernel_width=None, stride=None, dilation=0):
    pass

def pad2D(X, pad, kernel_width=None, stride=None, dilation=0):
    pass

def dilate(D, d):
    pass


# Convolution Arithmetic ===================================

def calc_fan(weight_shape):
    pass

def calc_conv_out_dims(X_shape, W_shape, stride=1, pad=0, dilation=0):
    pass


# Convolution Vectorization Utils ==========================

def _im2col_indices(X_shape, fr, fc, p, s, d=0):
    pass

def im2col(X, W_shape, pad, stride, dilation=0):
    pass

def col2im(X_col, X_shape, W_shape, pad, stride, dilation=0):
    pass


# Convalution ==============================================

def conv2D(X, W, stride, pad, dilation=0):
    pass

def conv1D(X, W, stride, pad, dilation=0):
    pass

def deconv2D_naive(X, W, stride, pad, dilation=0):
    pass

def conv2D_naive(X, W, stride, pad, dilation=0):
    pass


# Weight Initialization ====================================

def he_uniform(weight_shape):
    """
    Initializes network weights `W` with using the He uniform initialization
    strategy. 
    """
    pass

def he_normal(weight_shape):
    pass

def lorot_uniform(weight_shape, gain=1.0):
    pass

def glorot_normal(weight_shape, gain=1.0):
    pass

def truncated_normal(mean, std, out_shape):
    pass