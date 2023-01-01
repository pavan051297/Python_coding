def S1(char):
     # char = "s"
     st ="Hello worls my name is pavan\n"
     lt = list(st)
     for i in lt:
        if i != char:
            print("".join(i),end="",)

def s2(ch):
    st = "Hello worls my name is pavan"
    st.replace(ch,"")
    print( st)


S1("r")
s2("p")