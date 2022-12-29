# a=("hello world how are u ")
# b=a.split()
# print(b)
# print(len(b))


# task 2
# a="pavan mohan kumar kiran goetham phani sharma"
# b=a.count("a")
# print(b)
# b=list(a)
# print(b)

# task 3
# a = input("Please enter the string: ")
# b = a.split()
# numberofchar = list(a)
# single = set(a)
# su = 0
# for i in b:
#     c = len(i)
#     su += c
#     d = len(b)
# print("Total number of characters present in the given string is :- {}".format(su))
# print("total number of words in the string is {}".format(d))
# for j in single:
#     f = numberofchar.count(j)
#     print("the specied char {} is repeated {}".format(j,f))








# task 5
a = input("Please enter the string: ")
b = a.split()
numberofchar = list(a)
su = 0
c=f=d=0
for i in b:
    for j in i:
        f = a.count(j)
        print("the specfied char {} is repeated {}".format(j, f))
    c = len(i)
    su += c
d = len(b)
print("Total number of characters present in the given string is :- {}".format(su))
print("total number of words in the string is {}".format(d))







