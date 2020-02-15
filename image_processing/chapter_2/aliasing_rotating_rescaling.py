"""Aliasing, rotating and rescaling
Let's look at the impact of aliasing on images.
Remember that aliasing is an effect that causes different signals, in this
case pixels, to become indistinguishable or distorted.

You'll make this cat image upright by rotating it 90 degrees and then
rescaling it two times. Once with the anti aliasing filter applied before
rescaling and a second time without it, so you can compare them.

> Import the module and the rotate and rescale functions
> Rotate the image 90 degrees clockwise
> Rescale with anti aliasing
> Rescale without anti aliasing
> Show the resulting images
"""

import sys
from skimage.transform import rescale, rotate
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_cat_image_path = './dataset/chapter 2/image_cat.jpg'
img_cat = nda_import_image(str_cat_image_path)
img_cat_rotated = rotate(img_cat, -90)

plot_comparison(img_cat, img_cat_rotated, 'Rotated 90-degrees clockwise')

img_cat_rotated_rescaled = rescale(img_cat_rotated, 1/4, anti_aliasing=True, multichannel=True)

plot_comparison(img_cat, img_cat_rotated_rescaled, 'Rotated 90-degrees clockwise and Rescaled')

img_cat_rotated_rescaled_no_aa = rescale(img_cat_rotated, 1/4, anti_aliasing=False, multichannel=True)

plot_comparison(img_cat, img_cat_rotated_rescaled, 'Rotated 90-degrees clockwise and Rescaled (No AA)')
