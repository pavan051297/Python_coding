from array import *
valuse = array('i',[1,2,3,4,5,6])
print(valuse)                   #not float values supported


va = array('i',[1,2,3,-4,5,6])
print(va)                # negavtive values also printed


v = array('i',[1,2,3,4,5,6])
print(v)                    #negative values are not supported in caPITAAL iI ARRAY



Vi = array('i',[1,2,3,4,5,6])
print(Vi.buffer_info())  # returns address of tuple and len of tuple
Vi.reverse()
print(Vi)

