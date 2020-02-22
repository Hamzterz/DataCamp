"""
Reducing noise while preserving edges

In this exercise, you will reduce the noise in this landscape picture.

Since we prefer to preserve the edges in the image, we'll use the bilateral
denoising filter.

> Import the denoise_bilateral function from its module.
> Apply bilateral filter denoising.
> Show the original noisy and the resulting denoised image.
"""

import sys
from skimage.restoration import denoise_bilateral
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_nature_img_noisy = './dataset/chapter 3/noise-noisy-nature.jpg'
img_nature_noisy = nda_import_image(str_nature_img_noisy)

img_nature = denoise_bilateral(img_nature_noisy, multichannel=True)

plot_comparison(img_nature_noisy, img_nature, 'Denoised (Bilateral, Preserve Edges)')
