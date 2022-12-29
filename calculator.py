# a = int(input("first numbver"))
# b = int(input("second number"))
#
# c = input("1. Add\n2. Sub\n3. Mul\n4. Div\n Enter your choice")
# print(c)
#
# if c == "Add":
#     print("Sum is {}".format(a + b))
# elif c == "sub":
#     print("sub is {} ".format(a - b))
# elif c == "mul":
#     print("mul is {}".format(a * b))
# elif c == "div":
#     print("div is {}".format(a / b))
# else:
#     print("new operation needed")



a = int(input("first number:-"))
b = int(input("second number :-"))

operations = input("1.add\n2.sub\n3.multi\n4.div choose the number")
print(operations)

if operations == "add":
    print(a+b)
elif operations== "sub":
    print(a-b)
elif operations=="multi":
    print(a*b)
elif operations=="div":
    print(a/b)
else:
    print("choose the correct option")
