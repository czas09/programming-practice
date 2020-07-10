import re
from functools import partial
from ast import literal_eval as eval

import numpy as np

from optimizers import OptimizerBase, SGD, AdaGrad, RMSProp, Adam
from activations import ActivationBase, Affine, ReLU, Tanh, Sigmoid, LeakyReLU
from schedulers import SchedulerBase, ConstantScheduler, ExponentialScheduler, NoamScheduler, KingScheduler
from utils import he_normal, he_uniform, glorot_normal, glorot_uniform, truncated_normal


class ActivationInitializer(object):
    def __init__(self, param=None):
        pass

    def __call__(self):
        pass

    def init_from_str(self, act_str):
        pass
    

class SchedulerInitializer(object):
    def __init__(self, param=None, lr=None):
        pass
    
    def __call__(self):
        pass

    def init_from_str(self):
        pass
    
    def init_from_dict(self):
        pass
    

class OptimizerInitializer(object):
    def __init__(self, param=None):
        pass
    
    def __call__(self):
        pass

    def init_from_str(self):
        pass
    
    def init_from_dict(self):
        pass
    

class WeightInitializer(object):
    def __init__(self, act_fn_str, mode="glorot_uniform"):
        pass
    
    def __call__(self):
        pass

    def _calc_glorot_gain(self):
        pass