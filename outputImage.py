# %%
import numpy as np 
import math 
import random
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

FILE_NAME = "data.txt"
RANDOM_COLORS = True


def get_image_size(size):
    return math.isqrt(size), math.isqrt(size)


def create_image(data_list, rows, cols, random_colors=RANDOM_COLORS):
    arr = np.array(data_list[:rows * cols])
    data_array= arr.reshape(rows,cols)

    cmap = "grey"
    if random_colors:
        color_0 = [random.random(), random.random(), random.random()]
        # color_1 = (random.random(), random.random(), random.random())
        color_1 = [1 - 2*c for c in color_0]
        cmap = ListedColormap([color_0, color_1])

    plt.imshow(data_array, cmap=cmap)

    plt.axis("off")
    # plt.savefig('bunt.png')
    plt.show()


with open(FILE_NAME, "r") as f:
    data = [int(i) for i in f.read()]

create_image(data, *get_image_size(len(data)))

