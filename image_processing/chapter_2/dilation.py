"""Improving thresholded image (Dilation)

In this exercise, we'll try to reduce the noise of a thresholded image using
the dilation morphological operation.

This operation, in a way, expands the objects in the image.

> Import the module.
> Obtain the binarized and dilated image, from the original image world_image.
"""

import sys
from skimage import morphology
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_world_image_binary_path = './dataset/chapter 2/world_image_binary.jpg'
img_world = nda_import_image(str_world_image_binary_path)

thresh = threshold_otsu(rgb2gray(img_world))
img_world_binary = img_world > thresh

img_world_dilated = morphology.binary_dilation(img_world_binary)

plot_comparison(img_world, img_world_dilated, 'Dilated Image')
