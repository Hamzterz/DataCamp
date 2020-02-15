"""Aerial image (Exposure Equalisation)

In this exercise, we will improve the quality of an aerial image of a city.
The image has low contrast and therefore we can not distinguish all the
elements in it.

For this we will use the normal or standard technique of Histogram
Equalization.

> Import the required module from scikit-image.
> Use the histogram equalization function from the module previously imported.
> Show the resulting image.
"""

import sys
from skimage import exposure
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_aerial_img_path = './dataset/chapter 2/image_aerial.tiff'
img_aerial = nda_import_image(str_aerial_img_path)
img_aerial_eq = exposure.equalize_hist(img_aerial)

plot_comparison(img_aerial, img_aerial_eq, 'Resulting Image')
