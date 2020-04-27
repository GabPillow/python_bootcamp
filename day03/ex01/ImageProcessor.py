import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ImageProcessor:

    @staticmethod
    def load(path):
        data = mpimg.imread(path)
        print('Loading img size of', data.shape[0], 'x', data.shape[1])
        return data
    
    @staticmethod
    def display(array):
        img = plt.imshow(array)
        plt.show(block =img)
