from skimage import data
import numpy as np

img_coffee = data.coffee()
img_coins = data.coins()

tp_shape_coffee = np.shape(img_coffee)
tp_shape_coins = np.shape(img_coins)

print(tp_shape_coffee, tp_shape_coins)
print(type(tp_shape_coffee), type(tp_shape_coins))
