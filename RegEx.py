

import re
a = "hello pavan is @ my name pannnahsahvhc"
c = re.search("^pavan.*name$",a)
if c:
    print("yes it is")
else:
    print("it is not")

f =re.findall("[a-m]",a)
print(f)
g =re.findall("/d",a)
print(g)
gg= re.findall("pa..n",a)
print(gg)
aa =re.findall("he.*o",a)
print(aa)
s =re.findall("pa.{2}n",a)
print(s)
q =re.findall("pavan|yugesh",a)
print(q)
w =re.search("p",a)
print(w)
r= re.split("\s",a)
print(r)