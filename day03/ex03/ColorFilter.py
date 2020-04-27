import numpy as np

class   ColorFilter:

    @staticmethod
    def invert(array):
        return 1 - array
    
    @staticmethod
    def to_blue(array):
        dim = np.shape(array)
        new = np.zeros(dim, dtype = array.dtype)
        new[:, :, 2] = array[:, :, 2]
        return(new)


    @staticmethod
    def to_green(array):
        copy = np.copy(array)
        copy[:, :, 2] = copy[:, :, 2] * 0
        copy[:, :, 0] = copy[:, :, 0] * 0
        return copy


    @staticmethod
    def to_red(array):
        blue = ColorFilter.to_blue(array)
        green = ColorFilter.to_green(array)
        red = array - (green + blue)
        return red

    # @staticmethod
    # def celluloid(array)