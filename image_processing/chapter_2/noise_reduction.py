"""Blurring to reduce noise

In this exercise you will reduce the sharpness of an image of a building taken
during a London trip, through filtering.

> Import the Gaussian filter.
> Apply the filter to the building_image, set the multichannel parameter to the
correct value.
> Show the original building_image and resulting gaussian_image.
"""

import sys
from skimage.filters import gaussian
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_building_img_path = './dataset/chapter 2/building_image.jpg'
img_building = nda_import_image(str_building_img_path)

img_building_gaussian = gaussian(img_building, multichannel=True)
plot_comparison(img_building, img_building_gaussian, 'Reduced Sharpness Gaussian')
