# Map
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 16]
c = (1, 2, 3, 4, 5, 6, 7, 8, 9)
e = [(1,2), (3,4)]
d = {1: 1, 2: 9}


def square(i):
    return i*i


# When ever we want call a function up on every element of a Iterable object then Map can be used
print(square(10))
print(square)
b = map(str, a)
print(b)
print(range(10))
# for i in b:
#     print(i)
print(list(b))



# Filter

# Filter which will filter the all the elements of a sequence or iterable object using another
# function which will return only if condition satisfied in side that

names = ["Pavan", "yugesh", "sek", "nav", "janu"]
def cmp(i):
    if i % 2:
        return 10


f = filter(cmp, a)
print(list(f))


def greter_five(name):
    if len(name) >= 5:
        return True


names_filter = filter(greter_five, names)
print(list(names_filter))


#Reduce
from functools import reduce


def add(i, j):
    return i*j





print(reduce(add, a))