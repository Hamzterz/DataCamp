from matplotlib import pyplot as plt
from skimage import io
import numpy as np


def show_image(img):
    io.imshow(img)
    plt.show()


def nda_import_image(str_img_path):
    nda_img = plt.imread(str_img_path)

    return nda_img


def plot_comparison(img_original, img_filtered, img_title_filtered):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 6), sharex=True, sharey=True)
    ax1.imshow(img_original, cmap=plt.cm.gray)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(img_filtered, cmap=plt.cm.gray)
    ax2.set_title(img_title_filtered)
    ax2.axis('off')

    plt.show(fig)


def get_mask(img):
    mask = np.zeros(img.shape[:-1])

    mask[101:106, 0:240] = 1
    mask[152:154, 0:60] = 1
    mask[154:156, 100:120] = 1
    mask[155:156, 120:140] = 1
    mask[212:217, 0:150] = 1
    mask[217:222, 150:256] = 1

    return mask
