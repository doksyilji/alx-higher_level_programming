#!/usr/bin/python3

def uppercase(string):
    upper = ""
    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            upper += chr(ord(string[i]) - 32)
        else:
            upper += string[i]
    print("{}".format(upper))
