__author__ = "Máté Szegedi"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np
from PIL import Image
import sys

def main(image_location):
    #loads the image, turn it into black-and-white and resize it to 64x64px
    image = Image.open(image_location).convert('L').resize((64, 64))
    #converts the image into a 2D-numpy matrix, where every value represent
    # a pixel in the picture, and every value are between 0-255.
    # 255 represents here white.
    data = np.array(image)
    # This categorization simply checks, if the "frame" of the
    # picture is made out mainly from white pixels.
    # If yes, it is safe to assume that the picture has an uniform
    # "white-background". If not, then it has a  "multi-colour background"
    # the following step sums the values in the first and last
    # 2 rows and columns. Ideally these values should be ~255
    # but sometimes there are rouge pixels, which are near to
    # this value. Hence I set the sum of these lower, so these
    # rouge pixels are still included, but the categorization
    # is still accurate.
    if np.sum(data[:,[0,1]])+np.sum(data[:,[62,63]])+np.sum(data[[0,1],:])+np.sum(data[[62,63],:])>=120000:
        print("Image has white-background")
    else:
        print("Image has multi-colour background")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(sys.argv[1])
