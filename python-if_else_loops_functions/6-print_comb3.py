#!/usr/bin/python3
for i in range(0,10):
    for j in range(0,10):
        if i != j and i < 9 and j < 10:
            if (i == 8 and j == 9):
                print("{}{}".format(i, j), end="\n")
            else:
                print("{}{}".format(i, j), end=", ")

