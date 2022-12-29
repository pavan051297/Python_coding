# d={
#     "s1":{"name":"pavan",
#           "age" : 25,
#         "marks":[43,54,55,66,77]},
#     "s2":{"name":"mohan",
#           "age":32,
#           "marks":[54,44,55,55,25]},
#     "s3":{"name": "navya" ,
#           "age" : 26,
#         "marks":[44,44,65,26,27]}
#                                     }
# d["s3"]["marks"][1]=d["s3"]["marks"][1]+60
# print(d)



# # task 2
# d={"pavan":32,"mohan":23,"kiran":44}
#
# print(d["pavan"])
# d["gow"]=222
# print(d)
# f=d.clear()
# print(d)
# d={"pavan":32,"mohan":23,"kiran":44}
# f=d.copy()
# print(d)
# x=d.fromkeys("pavan",32)
# print(x)
#



# task 3
# print({
#      'python' : 210,
#      'perl' : 155,
#      'java': 150,
#      'linux' : 300,
#      'c' : 180
# })
# num=input("select a couse")
# if num=="python":
#     print("210")
# elif num=="perl":
#     print("155")
# elif num=="java":
#     print("300")
# elif num=="c":
#     print("180")

#
# a = {'pav','oko','fcfc'}
# b = {32,33,44}
# d = dict.fromkeys(a,b)
# print(d)

#
#
#
# e = {"pavan":32,"mohan":23,"kiran":44}
# f =e.items()
# print(f)
#
# #
# g =e.keys()
# print(g)
#
# #
# h = e.values()
# print(h)

# i =e.pop("pavan")
# print(i)
# print(e)
#
# j = e.update({"ksdksda": 66})
# print(e)



# task 3
# dic={
#     "student1":{"name":"pavan",
#                 "age":26,
#                 "marks":[121,11,33,333]},
#     "student2":{"name":"mohan",
#                 "age"  :28,
#                 "marks":[22,11,222,32]},
#     "student3":{"name":"kiran",
#                 "age" : 29,
#                 "marks":[22,33,44,444]}}
# d=sum(dic["student1"]["marks"])/len(dic["student1"]["marks"])
# print(d)


# task 4
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# res_dict = dict()
#
# for i in range(len(keys)):
#     res_dict.update({keys[i]: values[i]})
# print(res_dict)
#

#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# dict3 = {**dict1,**dict2}
# print(dict3)

# dic ={"p":[12,13,14],
#       "m": [13,14,15],
#       "n":[11,15,16]}
# res =sum(dic["n"])/len(dic["n"])
# print(res)


# name, *line = input("print ").split()
# scores = list(map(float, line))
# print(scores)
# r = ["pavan",""]
# l = [[12,13,14],[11,13,14],[11,24,22]]
# print(list(l))


# finding number of characters using dict

# a = 'hello i am pavan'
# b =a.split()
# mydict = {}
# for i in b:
#      for j in i:
#          for keys in j:
#              mydict[keys] = a.count(keys)
# print(mydict)



a = ["pavan","bdu","hjshc","ehbfh"]
b =[12,22,33,44]
c =dict(zip(a,b))
print(c)
