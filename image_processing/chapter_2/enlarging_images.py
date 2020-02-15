"""Enlarging images
Have you ever tried resizing an image to make it larger? This usually results
in loss of quality, with the enlarged image looking blurry.

The good news is that the algorithm used by scikit-image works very well for
enlarging images up to a certain point.

In this exercise you'll enlarge an image three times!!

You'll do this by rescaling the image of a rocket, that will be loaded from
the data module.

> Import the module and function needed to enlarge images, you'll do this by
rescaling.
> Import the data module.
> Load the rocket() image from data.
> Enlarge the rocket_image so it is 3 times bigger, with the anti aliasing
filter applied.
> Make sure to set multichannel to True or you risk your session timing out!
"""
import sys
from skimage.transform import rescale
from skimage.data import rocket
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

img_rocket = rocket()
img_rocket_enlarged = rescale(img_rocket, 3, anti_aliasing=True, multichannel=True)

plot_comparison(img_rocket, img_rocket_enlarged, '3-times enlarged image')
