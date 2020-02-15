"""Proportionally resizing

We want to downscale the images of a veterinary blog website so all of them
have the same compressed size.

It's important that you do this proportionally, meaning that these are not
distorted.

First, you'll try it out for one image so you know what code to test later in
the rest of the pictures.

Remember that by looking at the shape of the image, you can know its width and
height.

> Import the module and function to resize.
> Set the proportional height and width so it is half the image's height size.
> Resize using the calculated proportional height and width.
"""
import sys
from skimage.transform import resize
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_dogs_banner_img_path = './dataset/chapter 2/dogs_banner.jpg'
img_dogs_banner = nda_import_image(str_dogs_banner_img_path)

height = int(img_dogs_banner.shape[0] / 2)
width = int(img_dogs_banner.shape[1] / 2)

img_dogs_banner_resized = resize(img_dogs_banner, (height, width), anti_aliasing=True)

plot_comparison(img_dogs_banner, img_dogs_banner_resized, 'Resized image (half)')
