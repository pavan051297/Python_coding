# x=1
# y=1
# z=1
# n=2
# k=list()
# print(k)
# for i in range(x):
#     for j in range(y):
#         for l in range(z):
#             c=sum([i,j,l])
#             if c < n:
#                 print([i,j,l])


# task 2
#  list_of = []
# grade = []
# for i in range(int(input())):
#      names = input()
#      marks = float(input())
#      list_of.append([names,marks])
#      grade.append(marks)
#      grade = sorted(set(grade))
# m =grade[1]
# final_list = []
# for j in list_of:
#      if m == j[1]:
#           final_list.append(j[0])
# final_list.sort()
# for nm in final_list:
#     print(nm)
#

    # type 2

    # list_of = []
    # grade = []
    # for i in range(int(input())):
    #     names = input()
    #     marks = int(input())
    #     list_of.append([names, marks])
    #     grade.append(marks)
    #     grade = sorted(set(grade))
    # m = grade[1]
    # print(m)
    # for j in list_of:
    #     if m == j[1]:
    #         print(j[0])




l = []
N = int(input())
for i in range(N):
    a = l.append(input())
    b = l.append(input())
    c = list(str(input()))
    l.insert(1,c[0])
    print(l)
    l.remove(input())
    l.append(input())
    l.append(input())
    l.sort
    print(l)
    l.pop()
    l.reverse()
    print(l)

for i in range(N):
    a = input()
    if "insert" in a:
        t = a.split()
        l.insert(int(t[1]), int(t[2]))
    elif "append" in a:
        l.append(int(a.split()[1]))
    elif "sort" in a:
        l.sort()
    elif "pop" in a:
        l.pop()
    elif "reverse" in a:
        l.reverse()
    elif "remove" in a:
        l.remove(int(a.split()[1]))
    elif "print" in a:
        print(l)

        if __name__ == '__main__':
            s = input()
            print(any(map(str.isalnum, s)))
            print(any(map(str.isalpha, s)))
            print(any(map(str.isdigit, s)))
            print(any(map(str.islower, s)))
            print(any(map(str.isupper, s)))