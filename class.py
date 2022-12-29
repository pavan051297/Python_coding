# class algoritham:
#     def __int__(self,a,b):
#         self.a = num1
#         self.b = num2
#     def add(self):
#         op = num1 + num2
#          print(op)
#
#     def myfun(self,a,b):
#         res = a * b
#         print(res)
#
#
# num1 = 5
# num2 = 4
# s=algoritham()
# s.add()
# s.myfun(12,13)
# #


#
# class dog:
#      def __int__(self,name):
#         self.name = name
#         self.tricks = []
#      def add_trick(self,trick):
#          self.tricks.append(trick)
#
# d = dog(fiddo)
# e = dog(buddy)
# d.add_trick('roll over')
# e.add_trick('play dead')



# class car():
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def mycar(self):
#         print("the name of car is", self.a)
#         print("the colour of car is ",self.b)
#
# p1 = car(12,13)
# print(p1.a)
# print(p1.mycar)



class mine:
    def __int__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 +self.m2+self.m3)/3

s1 = mine(12,13,14)
s2 = mine(11,2,22)
print(s1.m1, s1.m2, s1.m3)

