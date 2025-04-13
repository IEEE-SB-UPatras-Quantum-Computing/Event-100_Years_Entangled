from matplotlib import pyplot as plt
import numpy as np 
import math 
import random


# print("My image arrray is:\n")
# print(my_array)



def ImageSize(size):
    side = math.isqrt(size)

    if (side%2 !=0):
        rows = round(side)
        cols= round(side)
    else:
        rows=side
        cols=side
    return rows, cols
    


def create_pixel_art(data, rows, cols):

    # total_pixels = rows * cols
    # if len(data) < total_pixels:
    #     data += [0] * (total_pixels - len(data))  # Συμπλήρωση με 0 για να ταιριάζει
    # data_array = np.array(data).reshape(rows, cols)  # Προσαρμογή δεδομένων
    with open("data.txt", "r") as f:
        data_list = []      
        for item in f:
            data_list.append(int(item.rstrip()))
    
    arr = np.array(data_list[:rows * cols])
    data_array= arr.reshape(rows,cols)
    
    # Δημιουργία colormap με τυχαία χρώματα για τα 0 και 1
    # cmap = [(random.random(), random.random(), random.random()),  # Χρώμα για το 0
    #         (random.random(), random.random(), random.random())]  # Χρώμα για το 1
    
    # plt.imshow(data_array, cmap=plt.cm.colors.ListedColormap(cmap), interpolation="nearest")
    
    plt.imshow(data_array, cmap='grey')
    # plt.axis("off")  # Κρύβουμε τους άξονες
    plt.show()


def Import_data ():
    with open("data.txt", "r") as f:
        data_list = []      
        for item in f:
            data_list.append(int(item.rstrip()))
        print(data_list) 
    return data_list 


# def Count():
#     with open("data.txt", "r") as f:
        
#         total_num=0       
#         for item in f:
#             total_num+=1
#         print(total_num)
#     return total_num 


data = Import_data()
# numOfdata=Count()


if data:
    # without count function, rows, cols = ImageSize(len(data))
    rows, cols = ImageSize(len(data))  # Βρίσκουμε το κατάλληλο μέγεθος
    create_pixel_art(data, int(rows), int(cols))  # Δημιουργούμε την εικόνα






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
