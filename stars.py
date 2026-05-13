rows = 5

for i in range(rows):
    for j in range(rows):
        if (i == 0 and j == 2) or \
           (i == 1 and (j == 1 or j == 3)) or \
           (i == 2 and (j == 0 or j == 1 or j == 3 or j == 4)) or \
           (i == 3 and (j == 1 or j == 3)) or \
           (i == 4 and j == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()