# %%
from random import randint

FILE_NAME = "data.txt"
SIZE = 100#_000

with open(FILE_NAME, 'w') as f:
    for _ in range(SIZE):
        f.write(str(randint(0,1)))

