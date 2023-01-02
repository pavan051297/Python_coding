class Vehicle:
    def __init__(self, name, no_of_wheels):
        print("VECHICLE constructor class called")
        self.name = name
        self.count = no_of_wheels

    def gear_box(self):
        print("I am in Vehicle gear Box")

    def brake(self):
        print("i am in brakes of the Vehicle")

    def get_name(self):
        print("The vehicle name is " + self.name)

    def get_number_of_wheels(self):
        print("Th e number of wheels are ", self.count)


# o1 = Vehicle("Creata", 4)
# o1.gear_box()
# o1.brake()
# o1.get_name()
# o1.get_number_of_wheels()

class Car(Vehicle):
    def __init__(self, a, b, c=0, d=0):
        super().__init__(a, b)
        self.a = a

        print("The constructor of the Car class called")


    def music(self):
        print("I am in car music System")

    def air_cool(self):
        print("I am in car cool")

    # def get_name(self):
    #     print("The vehicle name is th marvelous mighty  " + self.name)



# o2 = Car("Harrier", 4)
# o2.get_name()
# o2.gear_box()
# o2.get_number_of_wheels()

class luxury_car(Car, Vehicle):
    def __init__(self):
        super().__init__("Fortuner", 8)

        print("Luxury car constructor called")
        # Car.__init__("Fortuner", 8)

    def __m1(self):
        print("I am TBD")

    def m2(self):
        print("I am in m2 TBD")

    def get_name(self):
        print("SUPER SUPER SUPER DREAM is " + self.name)
        self.m2()
        self.__m1()


o3 = luxury_car()
# o3.get_number_of_wheels()
# o3.m1()
# o3.m2()
# o3.music()
o3.get_name()
