"""
A collection of objects thats can wrap / otherwise modify arbitrary neural
network layers. 
"""

from abc import ABC, abstractmethod

import numpy as np


class WrapperBase(ABC):
    def __init__(self, wrapped_layer):
        pass
    
    @abstractmethod
    def _init_wrapper_params(self):
        raise NotImplementedError
    
    @abstractmethod
    def forward(self, z, **kwargs):
        """Overwritten by inherited class"""
        raise NotImplementedError
    
    @abstractmethod
    def backward(self, z, **kwargs):
        pass
    
    @property
    def trainable(self):
        pass

    @property
    def parameters(self):
        pass
    
    @property
    def hyperparameters(self):
        pass
    
    @property
    def derived_variables(self):
        pass
    
    @property
    def gradients(self):
        pass

    @property
    def act_fn(self):
        pass
    
    def _init_params(self):
        pass
    
    def freeze(self):
        pass
    
    def unfreeze(self):
        pass
    
    def flush_gradient(self):
        pass
    
    def update(self, lr):
        pass
    
    def _set_wrapper_params(self, pdict):
        pass
    
    def set_params(self, summary_dict):
        pass
    
    def summary(self):
        pass
    

class Dropout(WrapperBase):
    def __init__(self, wrapped_layer, p):
        pass

    def _init_wrapper_params(self):
        pass
    
    def forward(self, X, retain_derived=True):
        pass
    
    def backward(self, dLdy, retain_grads, True):
        pass
    
    def init_wrappers(layer, wrappers_list):
        pass