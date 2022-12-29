# # a = int(input("Enter a num:"))
# # b = int(input("Enter the second number"))
try:
 print(a/b)
except ZeroDivisionError:
 b = int(input("You entred Zero. Pleae enter Non Zero Value"))
 print("new result is ", a/b)

try:
 print(d)
except ValueError:
 print("Name Error is observed. The name 'd' is not defined")

try:
 b = "hello world"
 a = int(b)
except ValueError:
 b = "77"
 a = int(b)

print(a)

a = "Hello"
b = " 77"
print(a+b)





def a():
 return "hello"

def b():
 return 20


try:
 print(int(a()))
except (ValueError, ZeroDivisionError, TypeError, ArithmeticError):
 print("The called method returned String instad of integer. Please check whether u called correct function")