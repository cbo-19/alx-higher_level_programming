#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if i >= 97 and i <= 122:
            i -= 32
            i = chr(i)
            n = format(i)
        elif not(i >= 97 and i <= 122):
            i = chr(i)
            s = format(i)
            print("{}".format(s, n), end="")
    print("")
