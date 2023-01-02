class A:
    def __init__(self):
        print("Class A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B constructor")


class C(A):
    def __init__(self):
        super().__init__()
        print("Class C constructor")

class D(B, C):
    def __init__(self):
        super().__init__()
        # C.__init__(self)
        print("Class D constructor")

o = D()