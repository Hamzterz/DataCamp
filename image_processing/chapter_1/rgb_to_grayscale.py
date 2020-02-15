import sys
from skimage import data, color
sys.path.append('./helpers')
from settings import show_image

img_rocket = data.rocket()

img_grey_scaled_rocket = color.rgb2gray(img_rocket)

show_image(img_rocket)

show_image(img_grey_scaled_rocket)
