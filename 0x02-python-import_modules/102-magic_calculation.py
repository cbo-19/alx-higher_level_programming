<<<<<<< HEAD
#!/usr/bin/python3


=======
!/usr/bin/python3
>>>>>>> 3cecb09c292abee8a878edc093a849d74061f5d3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
