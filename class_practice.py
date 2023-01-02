class A:
    def __init__(self, name, lname, mob):
        # print("ia m in constructor")
        self.name = name
        self.l_name = lname
        self.mob = mob

    def set(self, name):
        # self.name = name
        self.new_name = name

    def get_name(self):
        print(self.name)


    def addition(self, num1, num2):
        print("I am in addition method")
        return num1 + num2

    def get_new_name(self):
        print("The new name is " + self.new_name)


obj1 = A("Yugesh", "B", "143")
obj1.get_name()

# obj1.get_new_name()

obj1.set("Pavan Romeo")

obj1.get_new_name()
print(obj1.addition(2,3))






obj2 = A("pavan", "B", "225")
obj2.get_new_name()










# obj2 = A("pavan", "B", "225")


# res = A.addition(obj1, 2, 3)
# print("Resulat1: {}".format(res))
#
# res2 = obj2.addition(2, 3)
# print(res2)



# print(type(a))
# print(type(10))


