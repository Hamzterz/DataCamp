"""Apply Global Thresholding.
In this exercise, you'll transform a photograph to binary so you can separate
the foreground from the background. To do so, you need to import the required
modules, load the image, obtain the optimal thresh value using threshold_otsu()
and apply it to the image. You'll see the resulting binarized image when using
the show_image() function, previously explained. Remember we have to turn
colored images to grayscale. For that we will use the rgb2gray() function
learned in previous video. Which has already been imported for you.

Instructions:
> Import the otsu threshold function
> Make the image grayscale using rgb2gray
> Obtain the optimal threshold value with otsu
> Apply thresholding to the image
> Show the image

"""
import sys
from skimage.filters import threshold_otsu
from skimage import color
sys.path.append('./helpers')
from settings import show_image, nda_import_image


img_chess_pieces = nda_import_image('./dataset/chapter 1/bw.jpg')

show_image(img_chess_pieces)

img_chess_pieces_gray = color.rgb2gray(img_chess_pieces)

thresh = threshold_otsu(img_chess_pieces_gray)

img_binary = img_chess_pieces_gray > thresh
img_binary2 = img_chess_pieces_gray < thresh

show_image(img_binary)
show_image(img_binary2)
