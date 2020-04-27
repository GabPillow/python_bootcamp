import numpy as np

class ScrapBooker:

    @staticmethod
    def crop(array, dimensions, position = (0,0)):
        if dimensions[0] + position[0] > array.shape[0] or\
        dimensions[1] + position[1] > array.shape[1]:
            raise AttributeError('Dimensions bigger than picture')
        return array[position[0]:dimensions[0] + position[0],\
            position[1]:dimensions[1] + position[1]]

    @staticmethod
    def thin(array, n, axis):
        axis = 1 if axis == 0 else 0
        max = array.shape[axis]
        ind = [n - 1]
        if n > 0:
            while ind[-1] < max:
                ind.append(ind[-1] + n)
            ind = tuple(ind)
        return np.delete(array, ind, axis)
    
    @staticmethod
    def juxtapose(array, n, axis):
        axis = 1 if axis == 0 else 0
        cpy = array
        while n:
            array = np.append(array, cpy, axis)
            n -= 1
        return array
    
    @staticmethod
    def mosaic(array, dimensions):
        array = ScrapBooker.juxtapose(array, dimensions[0] - 1, 1)
        return ScrapBooker.juxtapose(array, dimensions[1] - 1, 0)
    
