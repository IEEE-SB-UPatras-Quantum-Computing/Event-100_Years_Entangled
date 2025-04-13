# %%

FILE_NAME = "data.txt"
CHAR_SIZE = 6

with open(FILE_NAME, "r") as f:
    data = f.read()

characters_len = len(data)//CHAR_SIZE
characters = []

for i in range(characters_len):
    datum = data[CHAR_SIZE*i : CHAR_SIZE*(i+1)]
    char_index = int(datum, 2)
    char = chr(char_index + 31)
    characters.append(char)

characters = ''.join(characters)

print(characters)
