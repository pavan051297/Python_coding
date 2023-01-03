i = "paapaag fueogidion"
count = {}.fromkeys(i, 0)
print(count)

for char in i:
    if char in count:
         count[char] += 1

print(i,count)
print(max(i,key =count.get))