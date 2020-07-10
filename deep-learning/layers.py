"""A collection of composable layer objects for building neural networks"""

from abc import ABC, abstractmmethod

import numpy as np

from wrappers import init_wrappers, Dropout
from initializers import WeightInitializer, OptimizerInitializer, ActivationInitializer
from utils import pad1D, pad2D, conv1D, conv2D, im2col, col2im, dilate, deconv2D_naive, calc_pad_dims_2D


class LayerBase(ABC):
    pass


class DotProductAttention(LayerBase):
    pass


class RBM(LayerBase):
    pass


# Layer Ops ================================================

class Add(LayerBase):
    pass


class Multiply(LayerBase):
    pass


class Flatten(LayerBase):
    pass


# Normalization Layers =====================================

class BatchNorm2D(LayerBase):
    pass


class BatchNorm1D(LayerBase):
    pass


class LayerNorm2D(LayerBase):
    pass


class LayerNorm1D(LayerBase):
    pass


# MLP Layers ===============================================

class Embedding(LayerBase):
    pass


class FullyConnected(LayerBase):
    pass

class Softmax(LayerBase):
    pass


class SparseEvolution(LayerBase):
    pass


# Convolutional Layers =====================================
class Conv1D(LayerBase):
    pass


class Conv2D(LayerBase):
    pass


class Pool2D(LayerBase):
    pass


class Deconv2D(LayerBase):
    pass


# Recurrent Layers =========================================

class RNNCell(LayerBase):
    pass


class LSTMCell(LayerBase):
    pass


class RNN(LayerBase):
    pass


class LSTM(LayerBase):
    pass