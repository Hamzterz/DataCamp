"""Local Thresholding
When the background isn't that obvious.
Sometimes, it isn't that obvious to identify the background. If the image
background is relatively uniform, then you can use a global threshold value
as we practiced before, using threshold_otsu(). However, if there's uneven
background illumination, adaptive thresholding threshold_local() (a.k.a.
local thresholding) may produce better results.

In this exercise, you will compare both types of thresholding methods (global
and local), to find the optimal way to obtain the binary image we need.

1.
> Import the otsu threshold function
> Obtain the optimal otsu global thresh value
> Obtain the binary image by applying global thresholding
> Show the binary image obtained

2.
> Import the local threshold function
> Set the block size to 35
> Obtain the optimal local thresholding
> Obtain the binary image by applying local thresholding
> Show the binary image
"""

import sys
sys.path.append('./helpers')
from settings import show_image, nda_import_image


from skimage.filters import threshold_otsu, threshold_local
from skimage import color

img_page = nda_import_image('./dataset/chapter 1/page_image.png')

def img_thresholding(img, type):
    show_image(img)
    img_grayscale = color.rgb2gray(img)
    if type == 'global':
        thresh = threshold_otsu(img_grayscale)
    else:
        thresh = threshold_local(img_grayscale, block_size=35, offset=10)
    img_binary = img_grayscale > thresh
    img_binary2 = img_grayscale < thresh
    show_image(img_binary)
    show_image(img_binary2)


img_thresholding(img_page, type='global')
img_thresholding(img_page, type='local')
