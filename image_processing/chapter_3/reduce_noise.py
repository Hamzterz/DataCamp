"""
Reducing noise

We have a noisy image that we want to improve by removing the noise in it.

Use total variation filter denoising to accomplish this.

> Import the denoise_tv_chambolle function from its module.
> Apply total variation filter denoising.
> Show the original noisy and the resulting denoised image.
"""
import sys
from skimage.restoration import denoise_tv_chambolle
from skimage.util import random_noise
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_cute_dog_img_noisy_path = './dataset/chapter 3/miny.jpeg'
img_cute_dog_noisy = random_noise(nda_import_image(str_cute_dog_img_noisy_path))

img_cute_dog = denoise_tv_chambolle(img_cute_dog_noisy, multichannel=True)

plot_comparison(img_cute_dog_noisy, img_cute_dog, 'Denoised (TV Champbolle Method)')
