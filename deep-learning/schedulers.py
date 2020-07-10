from abc import ABC, abstractmethod
from copy import deepcopy
from math import erf

import numpy as np


def gaussian_cdf(x, mean, var):
    eps = np.finfo(float).eps
    x_scaled = (x - mean) / np.sqrt(var + eps)
    return (1 + erf(x_scaled / np.sqrt(2))) / 2


class SchedulerBase(ABC):
    def __init__(self):
        """Abstract base class for all Schduler objects"""
        self.hyperparameters = {}
    
    def __call(self, step=None, cur_loss=None):
        return self.learning_rate(step=step, cur_loss=cur_loss)
    
    def copy(self):
        """Return a copy of the current object"""
        return deepcopy(self)
    
    def set_params(self, hparam_dict):
        """Set the Scheduler hyperparameters from a dictionary"""
        if hparam_dict is not None:
            for k, v in hparam_dict.items():
                if k in self.hyperparameters:
                    self.hyperparameters[k] = v
    
    @abstractmethod
    def learning_rate(self, step=None):
        raise NotImplementedError


class ConstantScheduler(SchedulerBase):
    def __init__(self, lr=0.01, **kwargs):
        super().__init__()
        self.lr = lr
        self.hyperparameters = {"id":"ConstantScheduler", "lr":self.lr}
    
    def __str__(self):
        return "ConstantScheduler(lr={})".format(self.lr)
    
    def learning_rate(self, **kwargs):
        return self.lr


class ExponentialScheduler(SchedulerBase):
    def __init__(
        self, initial_lr=0.01, stage_length=500, staircase=False, decay=0.1, **kwargs
    ):
        pass
    
    def __str__(self):
        pass
    
    def learning_rate(self, step, **kwargs): 
        pass


class NoamScheduler(SchedulerBase):
    def __init__(
        self, model_dim=512, scale_factor=1, warmup_steps=4000, **kwargs
    ): 
        pass
    
    def __str__(self):
        pass
    
    def learning_rate(self, step, **kwargs):
        pass


class KingScheduler(SchedulerBase):
    def __init__(
        self, initial_lr=0.01, patience=1000, decay=0.99, **kwargs
    ): 
        pass
    
    def __str__(self):
        pass
    
    def _steps_without_decrease(self, robust=False, check_all_False):
        pass
    
    def _p_decreasing(self, loss_history, i):
        pass
    
    def learning_rate(self, step, cur_loss):
        pass