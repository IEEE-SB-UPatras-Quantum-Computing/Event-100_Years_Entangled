# %%
import matplotlib.pyplot as plot

FILE_NAME = "data.txt"

with open(FILE_NAME, "r") as f:
    data = [int(i) for i in f.read()]


numbers = ['Μηδενικά (0)', 'Άσοι (1)']
counts = [data.count(0), data.count(1)]
plot.bar(numbers, counts, color=["cyan", "Purple"])


plot.xlabel('Τιμές')
plot.ylabel('Πλήθος')
plot.title('Ιστόγραμμα')
plot.grid(axis='y', linestyle='--', alpha=0.7)
plot.show()
