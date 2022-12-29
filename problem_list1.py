a = [2,39,4,5,6,7,10,22,23,32,34]
b = 30


# sum of Two numbers in the above list is 30. I wanted the indexes of those numbers
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         # print(i,a[i],j)
#         if (a[i]+a[j]) == b:
#             print(i, j)

for i in range(len(a)):
    c = b - a[i]
    if c in a[i+1:]:
        print(i, a.index((c)))

