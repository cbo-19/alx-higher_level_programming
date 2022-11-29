#!/usr/bin/python3
def main():
    #the  (97,123) are ascii representation of lower letters
    for i in range(97,123):
        #the chr() function is used to change the ascii value to character
        print(f"{chr(i)}",end= "")
main()
