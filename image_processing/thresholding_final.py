"""Apply thresholding
In this exercise, you will decide what type of thresholding is best used to
binarize an image of knitting and craft tools. In doing so, you will be able
to see the shapes of the objects, from paper hearts to scissors more clearly.

What type of thresholding would you use judging by the characteristics of the
image? Is the background illumination and intensity even or uneven?

> Import the appropriate thresholding and rgb2gray() functions.
> Turn the image to grayscale.
> Obtain the optimal thresh.
> Obtain the binary image by applying thresholding.
"""

import sys
from skimage.filters import try_all_threshold, threshold_li
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
sys.path.append('./helpers')
from settings import nda_import_image, show_image

str_tools_image_path = './dataset/chapter 1/shapes52.jpg'
img_tools = nda_import_image(str_tools_image_path)


def apply_thresholding_test(img):
    img_grayscale = rgb2gray(img)
    fig, ax = try_all_threshold(img_grayscale, verbose=False)
    plt.show()


apply_thresholding_test(img_tools)

img_tools_grayscale = rgb2gray(img_tools)
li_thresh = threshold_li(img_tools_grayscale)
img_tools_binary = img_tools_grayscale > li_thresh
show_image(img_tools_binary)
