import numpy as np

class NumPyCreator:

    @staticmethod
    def from_list(lst):
        return np.array(lst)

    @staticmethod
    def from_tuple(tpl):
        return np.array(tpl)

    @staticmethod
    def from_iterable(itr):
        return np.arange(itr)
    
    @staticmethod
    def from_shape(shape, value = 0):
        return np.full(shape, value, dtype=int)

    @staticmethod
    def random(shape):
        return np.random.rand(shape[0], shape[1])

    @staticmethod
    def identity(n):
        return np.identity(n)
