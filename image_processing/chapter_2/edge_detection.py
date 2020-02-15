"""
Edge detection

In this exercise, you'll detect edges in an image by applying the Sobel filter.
Let's see if it spots all the figures in the image.

> Import the color module so you can convert the image to grayscale.
> Import the sobel() function from filters module.
> Make soaps_image grayscale using the appropriate method from the color
module.
> Apply the sobel edge detection filter on the obtained grayscale image
soaps_image_gray.
"""

import sys
from skimage.color import rgb2gray
from skimage.filters import sobel
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_soap_img_path = './dataset/chapter 2/soap_image.jpg'
img_soaps = nda_import_image(str_soap_img_path)
# show_image(img_soaps)

img_soaps_gs = rgb2gray(img_soaps)
# show_image(img_soaps_gs)

img_soaps_edge_sobel = sobel(img_soaps_gs)
print(type(img_soaps_edge_sobel))

# show_image(img_soaps_edge_sobel)

plot_comparison(img_soaps, img_soaps_edge_sobel, 'Edges with Sobel')
