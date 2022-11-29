#!/usr/bin/python3
def main():
    for i in range(97, 123):
        if i != 101 and i != 113:
            print("{}".format(chr(i)), end="")
        else:
            continue


main()
