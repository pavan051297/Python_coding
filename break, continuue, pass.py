# ava = 10
# x = int(input("how many candies u need:-"))
# i = 1
# while i <= x :
#     if i >ava:
#         print("out of stock")
#         break
#     print("candy",i)
#     i+= 1
#
# print("bye")




for i in range(1,101):
    if i % 3 ==0 or i % 5 ==0:
        continue
    print(i,end="")

