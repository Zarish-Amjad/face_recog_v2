import cv2
import numpy as np
import time
import os
from skimage.io import imread_collection
import numpy as np

def bytetoimage(array_image, width, height, channels = 3):
    flat_image = np.array(array_image)
    #image = flat_image.reshape(width, height, channels)
    return True, flat_image