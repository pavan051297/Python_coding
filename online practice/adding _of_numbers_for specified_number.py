list = [4,2,7,9,1,8]
result =9
for i in range(len(list) -1):
    if list[i]+list[i+1] == result :
        print(list[i],list[i+1])

