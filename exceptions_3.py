__version__ = 1
a = int(input("Enter a num:"))
b = int(input("Enter the second number"))

try:
    if b == 2:
        raise Exception("Divided By Two error")
    print(a / b)
except ZeroDivisionError:
    b = int(input("You entred Zero. Pleae enter Non Zero Value"))
    print("new result is ", a / b)
