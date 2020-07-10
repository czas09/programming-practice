from abc import ABC, abstractmethod

import re
import numpy as np

from wrappers import Dropout
from utils import calc_pad_dims_2D
from activations import Tanh, Sigmoid, ReLU, LeakyReLU, Affine
from layers import DotProductAttention, FullyConnected, BatchNorm2D, Conv1D, Conv2D, Multiply, LSTMCell, Add


class ModuleBase(ABC):
    pass


class WavenetResidualModule(ModuleBase):
    pass


class SkipConnectionIdentityModule(ModuleBase):
    pass


class SkipConnectionConvModule(ModuleBase):
    pass


class BidirectionalLSTM(ModuleBase):
    pass


class MultiHeadedAttentionModule(ModuleBase):
    pass