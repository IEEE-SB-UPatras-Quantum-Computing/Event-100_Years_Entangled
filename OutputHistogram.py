
import matplotlib.pyplot as plot

with open ('data.txt', 'r')as file:
    values=[int(line.strip()) for line in file]


total= len(values)
zeros=values.count(0)
ones=values.count(1)




print("Το συνολικό πλήθος αριθμών είναι:", total)
print("Το συνολικό πλήθος των μηδενικών είναι:", zeros)
print("Το συνολικό πλήθος των άσων είναι:", ones)

# data1=[]
# for i in range(zeros):
#     data1.append(0)


# data2=[]
# for i in range(zeros):
#     data2.append(1)

 
counts=[zeros,ones]
numbers = ['Μηδενικά (0)', 'Άσοι (1)']
plot.bar(numbers, counts,color=["cyan", "Purple"])


# plot.bar([data1, data2],bins=2, color=["cyan", "Purple"], edgecolor='black')

# plot.xlabel('Τιμές')
plot.ylabel('Πλήθος')
plot.title('Ιστόγραμμα')
plot.grid(axis='y', linestyle='--', alpha=0.7)


# plot.xticks([data1,data2], ['0', '1'])
 

# plot.legend(['0', '1'])
 
# Display the plot
plot.show()