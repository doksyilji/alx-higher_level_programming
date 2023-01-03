#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if j <= i:
            continue
        if i != j:
            if i == 0 and j == 1:
                print("{:d}{:d}".format(i, j), end="")
            else:
                print(", {:d}{:d}".format(i, j), end="")
print("")
