"""Medical images (Exposure Equalisation)

You are trying to improve the tools of a hospital by pre-processing the 
X-ray images so that doctors have a higher chance of spotting relevant
details. You'll test our code on a chest X-ray image from the National
Institutes of Health Chest X-Ray Dataset.

First, you'll check the histogram of the image and then apply standard
histogram equalization to improve the contrast. Remember we obtain the
histogram by using the hist() function from Matplotlib, which has been
already imported as plt.

> Import the required Scikit-image module for contrast.
"""
import sys
from skimage import exposure
from matplotlib import pyplot as plt
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison

str_xray_img_path = './dataset/chapter 2/chest_xray_image.png'
img_xray = nda_import_image(str_xray_img_path)

plt.title('Histogram of image')
plt.hist(img_xray.ravel(), bins=256)
plt.show()

img_xray_eq = exposure.equalize_hist(img_xray)

plot_comparison(img_xray, img_xray_eq, 'Resulting Image')
