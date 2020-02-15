"""Handwritten letters (Morphology)

A very interesting use of computer vision in real-life solutions is performing
Optical Character Recognition (OCR) to distinguish printed or handwritten text
characters inside digital images of physical documents.

Let's try to improve the definition of this handwritten letter so that it's
easier to classify.

As we can see it's the letter R, already binary, with with some noise in it.
It's already loaded as upper_r_image.

Apply the morphological operation that will discard the pixels near the letter
boundaries.

> Import the module from scikit-image.
> Apply the morphological operation for eroding away the boundaries of regions
of foreground pixels.
"""
import sys
from skimage import morphology
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_written_r_path = './dataset/chapter 2/r5.png'
img_written_r = nda_import_image(str_written_r_path)

# Had to convert image to binary before binary_erosion()
thresh = threshold_otsu(rgb2gray(img_written_r))
img_written_r_binary = rgb2gray(img_written_r) > thresh

img_written_r_eroded = morphology.binary_erosion(img_written_r_binary)

plot_comparison(img_written_r, img_written_r_eroded, 'Eroded Image')
