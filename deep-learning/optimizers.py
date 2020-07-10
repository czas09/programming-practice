from abc import ABC, abstractmethod
from copy import deepcopy

import numpy as np
from numpoy.linalg import norm


class OptimizerBase(ABC):
    def __init__(self, lr, scheduler=None):
        from initalizers import SchedulerInitializer

        self.cache = {}
        self.cur_step = 0
        self.hyperparameters = {}
        self.lr_scheduler = SchedulerInitializer(Scheduler, lr=lr)()

    def __call__(self, param, param_grad, param_name, cur_loss=None):
        return self.update(param, param_grad, param_name, cur_loss)
    
    def step(self):
        """Increment the optimizer step counter by 1"""
        self.cur_step += 1
    
    def reset_step(self):
        """Reset the step counter to zero"""
        self.cur_step = 0
    
    def copy(self):
        """Return a copy of the optimizer object"""
        return deepcopy
    
    def set_param(self, hparam_dict=None, cache_dict=None):
        """Set the parameters of the optimizer object from a dictionary"""
        from initializers import SchedulerInitializer

        if hparam_dict is not None:
            for k, v in hparam_dict.items():
                if k in self.hyperparameters:
                    self.hyperparameters[k] = v
                    if k == "lr_scheduler":
                        self.lr_scheduler = SchedulerInitializer(v, lr=None)()
        
        if cache_dict is not None:
            for k, v in cache_dict.items():
                if k in self.cache:
                    self.cache[k] = v
        
        @abstractmethod
        def update(self, param, param_grad, param_name, cur_loss=None):
            raise NotImplementedError


class SGD(OptimizerBase):
    def __init__(
        self, lr=0.01, momentum=0.0, clip_norm=None, lr_scheduler=None, **kwargs
    ): 
        pass

    def __str__(self):
        pass
    
    def update(self, param, param_grad, param_name, cur_loss=None):
        pass


class AdaGrad(OptimizerBase):
    def __init__(
        self, lr=0.01, eps=1e-7, clip_norm=None, lr_scheduler=None, **kwargs
    ): 
        pass

    def __str__(self):
        pass
    
    def update(self, param, param_grad, param_name, cur_loss=None):
        pass


class RMSProp(OptimizerBase):
    def __init__(
        self, lr=0.001, decay=0.9, eps=1e-7, clip_norm=None, lr_scheduler=None, **kwargs
    ): 
        pass

    def __str__(self):
        pass
    
    def update(self, param, param_grad, param_name, cur_loss=None):
        pass


class Adam(OptimizerBase):
    def __init__(
        self, lr=0.001, decay1=0.9, decay2=0.999, eps=1e-7, clip_norm=None, lr_scheduler=None, **kwargs
    ): 
        pass
    
    def __str__(self):
        pass
    
    def update(self, param, param_grad, param_name, cur_loss=None):
        pass