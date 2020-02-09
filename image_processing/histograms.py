import sys
from matplotlib import pyplot as plt

sys.path.append('./helpers')
from settings import show_image, nda_import_image

nda_90s_girl = nda_import_image('./dataset/chapter 1/4.1.01.tiff')

nda_red_channel = nda_90s_girl[:, :, 0]

plt.hist(nda_red_channel.ravel(), bins=256)
plt.title('Red Histogram of 90\'s Girl')
plt.show()
