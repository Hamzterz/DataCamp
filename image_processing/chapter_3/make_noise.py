"""Let's make some noise!

In this exercise, we'll practice adding noise to a fruit image.

>Import the util module and the random noise function.
>Add noise to the image.
>Show the original and resulting image.
"""
import sys
from skimage.util import random_noise
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_fruits_img_path = './dataset/chapter 3/fruits_square.jpg'
img_fruits = nda_import_image(str_fruits_img_path)

img_fruits_noisy = random_noise(img_fruits)

plot_comparison(img_fruits, img_fruits_noisy, 'Noise')
