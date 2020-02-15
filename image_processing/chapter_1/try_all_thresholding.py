"""Trying other methods (Thresholding)
As we saw in the video, not being sure about what thresholding method to use
isn't a problem. In fact, scikit-image provides us with a function to check
multiple methods and see for ourselves what the best option is. It returns a
figure comparing the outputs of different global thresholding methods. You
will apply this function to this image, matplotlib.pyplot has been loaded as
plt. Remember that you can use try_all_threshold() to try multiple global
algorithms.

> Import the try all function.
> Import the rgb to gray convertor function.
> Turn the fruits image to grayscale.
> Use the try all method on the grayscale image.
"""

import sys
from skimage.filters import try_all_threshold
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
sys.path.append('./helpers')
from settings import nda_import_image, show_image

str_fruit_image_path = './dataset/chapter 1/fruits-2.jpg'
img_fruit = nda_import_image(str_fruit_image_path)
img_fruit_grayscale = rgb2gray(img_fruit)

fig, ax = try_all_threshold(img_fruit_grayscale, verbose=False)
plt.show()
