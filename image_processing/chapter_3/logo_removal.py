"""Removing logos

As we saw in the video, another use of image restoration is removing objects
from an scene. In this exercise, we'll remove the Datacamp logo from an image.

You will create and set the mask to be able to erase the logo by inpainting
this area.

Remember that when you want to remove an object from an image you can either
manually delineate that object or run some image analysis algorithm to find it.

> Initialize a mask with the same shape as the image, using np.zeros().
> In the mask, set the region that will be inpainted to 1 .
> Apply inpainting to image_with_logo using the mask.
"""
import sys
import numpy as np
from skimage.restoration import inpaint
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_lake_img_with_logo = './dataset/chapter 3/4.2.06_w_logo_2_2.png'
img_lake_with_logo = nda_import_image(str_lake_img_with_logo)


mask = np.zeros(img_lake_with_logo.shape[:-1])

print(img_lake_with_logo.shape[:-1])

mask[210:272, 360:425] = 1

img_logo_removed = inpaint.inpaint_biharmonic(
        img_lake_with_logo,
        mask,
        multichannel=True
    )
plot_comparison(img_lake_with_logo, img_logo_removed, 'Removed Logo')
