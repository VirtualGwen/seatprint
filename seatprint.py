num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

for i in range(num_rows):
    for j in range(num_cols):
        char_cols = chr(j + 97)
        print('{}{}'.format(i+1, char_cols.upper()), end = ' ')

print()
