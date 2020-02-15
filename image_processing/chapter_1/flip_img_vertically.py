import sys
import numpy as np

sys.path.append('./helpers')
from settings import show_image, nda_import_image

nda_flipped_horiz_vert_seville = nda_import_image('./dataset/chapter 1/sevilleup(2).jpg')

nda_flipped_horiz_seville = np.flipud(nda_flipped_horiz_vert_seville)

show_image(nda_flipped_horiz_seville)

nda_seville = np.fliplr(nda_flipped_horiz_seville)

show_image(nda_seville)
