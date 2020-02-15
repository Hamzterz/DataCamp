"""Let's restore a damaged image

In this exercise, we'll restore an image that has missing parts in it, using
the inpaint_biharmonic() function.

We'll work on an image from the data module, obtained by data.astronaut().
Some of the pixels have been replaced by 1s using a binary mask, on purpose,
to simulate a damaged image. Replacing pixels with 1s turns them totally black.
The defective image is saved as an array called defect_image.

The mask is a black and white image with patches that have the position of the
image bits that have been corrupted. We can apply the restoration function on
these areas.

Remember that inpainting is the process of reconstructing lost or deteriorated
parts of images and videos.

> Import the module from restoration
> Show the defective image
> Apply the restoration function to the image using the mask
"""
import sys
from skimage.restoration import inpaint
sys.path.append('./helpers')
from settings import nda_import_image, show_image, plot_comparison, get_mask

str_damaged_astronaut_path = './dataset/chapter 3/damaged_astronaut.png'
img_damaged_astronaut = nda_import_image(str_damaged_astronaut_path)
img_restored_astronaut = inpaint.inpaint_biharmonic(img_damaged_astronaut, mask, multichannel=True)
plot_comparison(img_damaged_astronaut, img_restored_astronaut, 'Restored Image')
# need to elaborate on this one further
