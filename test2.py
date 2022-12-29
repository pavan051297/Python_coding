num=int(input("first number"))
num2=int(input("upto which number"))
for i in range(1,num2):
  c=num*i
  print("{} * {}={}".format(num,i,c))
