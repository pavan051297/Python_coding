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





class addition:

    def __init__(self, name):
        print("you have created obj for add class")
        self.name = name
        pass

    def add_two_num(self, a, b):
        c = a + b
        return c

    def print_name(self):
        print(self.name)

    def modifie_name(self, new_name):
        self.name = new_name


obj = addition("pavan")
obj2 = addition("sekhar")
# b = obj.add_two_num(2, 3)
# c = obj.add_two_num(10,20)
# print(c)


obj.print_name()
obj2.print_name()

obj.modifie_name("yugesh")
obj.print_name()
obj2.print_name()











class hub:
    def __init__(self,a,b):
        print("hello")
        self.a = a
        self.b=  b

    def addi(self):
        print(self.a +self.b)

    def subb(self):
        print(self.a - self.b)


o = hub(6,3)
o2 = hub(9,1)
print(o.addi())
print(o2.subb())
