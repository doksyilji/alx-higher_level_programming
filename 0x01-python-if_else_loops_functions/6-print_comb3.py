#!/usr/bin/python3

for i in range(10):
  for j in range(10):
    if j <= i:
        continue
    if i != j:
        print("{:d}{:d},".format(i, j), end=" ")
print("{:d}{:d}".format(i, j))
