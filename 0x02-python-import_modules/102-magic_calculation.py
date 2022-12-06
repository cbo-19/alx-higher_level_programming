<<<<<<< HEAD
<<<<<<< HEAD
#!/usr/bin/python3


=======
!/usr/bin/python3
>>>>>>> 3cecb09c292abee8a878edc093a849d74061f5d3
=======
#!/usr/bin/python3

>>>>>>> e149d487655da5a77a2c9ed8d07f578726993002
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
