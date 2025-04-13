from matplotlib import pyplot as plt
import numpy as np 
import math 
import random
from matplotlib.colors import ListedColormap


# print("My image arrray is:\n")
# print(my_array)



# def ImageSize(size):
#     side = math.isqrt(size)

#     if (side%2 !=0):
#         rows = round(side)
#         cols= round(side)
#     else:
#         rows=side
#         cols=side
#     return rows, cols

def ImageSize(size):
    side = math.isqrt(size)

    return side, side
    


def Create_image(data, rows, cols):
    
    with open("DATAa.txt", "r") as f:
        data_list = []      
        for item in f:
            data_list.append(int(item.rstrip()))
    
    arr = np.array(data_list[:rows * cols])
    data_array= arr.reshape(rows,cols)
    
    # Δημιουργία colormap με τυχαία χρώματα για τα 0 και 1
    color_0 = (random.random(), random.random(), random.random())
    color_1 = (random.random(), random.random(), random.random())
    cmaps = ListedColormap([color_0, color_1])
    
    
    # cmaps = ListedColormap([ (random.random(), random.random(), random.random()),  
    #                         (random.random(), random.random(), random.random()) ])
    
    plt.imshow(data_array, cmap=cmaps)

    # plt.imshow(data_array)
    plt.axis("off")  # Κρύβουμε τους άξονες
    plt.show()
    plt.savefig('foo.png')


def Import_data ():
    with open("DATAa.txt", "r") as f:
        data_list = []      
        for item in f:
            data_list.append(int(item.rstrip()))
        # print(data_list) 
    return data_list 


data = Import_data()
Create_image(data, *ImageSize(len(data))) 





# my_list= Import_data()
# print(my_list)
# my_array= np.array(my_list)
# print(my_array)
# imSize=Count()

# plt.figure(figsize=(7, 6))
# plt.imshow(my_array)
# plt.show()



# my_list= [[1,0,0,1,0,1,1,0]]
# my_array= np.array(my_list)
# imSize=Count()

# plt.figure(figsize=(7, 6))
# plt.imshow(my_array)
# plt.show()
