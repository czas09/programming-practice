from abc import ABC, abstractmethod
import numpy as np

class ActivationBase(ABC):
    def __init__(self, **kwargs): 
        """Initialize the ActivationBase object"""
        super().__init__()
    
    def __call__(self, z):
        """Apply the activation function to an input"""
        if z.ndim == 1:
            z = z.reshape(1, -1)
        return self.fn(z)
    
    @abstractmethod
    def fn(self, z): 
        """Applu the activation function to an input"""
        raise NotImplementedError
    
    @abstractmethod
    def grad(self, x, **kwargs):
        """Compute the gradient of the activation function wrt the input"""
        raise NotImplementedError
    

class Sigmoid(ActivationBase):
    def __init__(self):
        """A logistic sigmoid activation function"""
        super().__init__()
    
    def __str__(self):
        """Return a string representation of the activation function"""
        return "Sigmoid"
    
    def fn(self, z):
        r"""
        Evaluate the logistic sigmoid, :math:`\sigma`, on the elements of imput `z`

        .. math::

            \sigma(x_i) = \frac{1}{1 + e^{-x_i}}
        """
        return 1 / (1 + np.exp(-z))
    
    def grad(self, x):
        r"""
        Evaluate the first derivative of the logistic sigmoid on the elements of `x`

        .. math::

            \frac{\partial \sigma}{\partial x_i} = \sigma(x_i) (1 - \sigma(x_i))
        """
        fn_x = self.fn(x)
        return fn_x * (1 - fn_x)
    
    def grad2(self, x):
        r"""
        Evaluate the second derivative of the logistic sigmoid on the elements of `x`

        .. math::

            \frac{\partial^2 \sigma}{\partial x_i^2} = 
                \frac{\partial \sigma}{\partial x_i} (1 - 2 \sigma(x_i))
        """
        fn_x = self.fn(x)
        return fn_x * (1 - fn_x) * (1 - 2 * fn_x)


class ReLU(ActivationBase):
    """
    A rectified linear activation function

    Notes
    -----
    "ReLU unis can be fragile during training and can "die". For example, a 
    large gradient flowing through a ReLU neuron could cause the weights to 
    update in such a way that the neuron will never activate on any datapoint 
    again. If this happens, then the gradient flowing through the unit will 
    forever be zero from that point on. That is, the ReLU units can 
    irreversibly die during training since they can get knocked off the data 
    manifold.

    """

    def __init__(self):
        super().__init__()
    
    def __str__(self):
        """Return a string representation of the activation function"""
        return "ReLU"
    
    def fn(self, z):
        r"""
        """
        pass
    
    def grad(self, x):
        pass

    def grad2(self, x):
        pass


class LeakyReLU(ActivationBase):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass


class Tanh(ActivationBase):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass


class Affine(ActivationBase):
    def __init__(self, slope=1, intercept=0):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass


class Identity(Affine):
    def __init__(self):
        pass
    
    def __str__(self):
        pass


class ELU(ActivationBase):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass

class Exponential(ActivationBase):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass


class SELU(ActivationBase):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass


class HardSigmoid(ActivationBase):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass
    

class SoftPlus(ActivationBase):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def fn(self, z):
        pass
    
    def grad(self, x):
        pass
    
    def grad2(self, x):
        pass