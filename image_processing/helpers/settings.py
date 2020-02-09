from matplotlib import pyplot as plt
from skimage import io


def show_image(img):
    io.imshow(img)
    plt.show()


def nda_import_image(str_img_path):
    nda_img = plt.imread(str_img_path)

    return nda_img
