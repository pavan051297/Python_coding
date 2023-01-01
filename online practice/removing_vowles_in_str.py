string = "pavan new project"
vowels = ("a","A","e","E","i","I","o","O","u","U")
result = ''
for i in string:
    if i in vowels:
        i =''
    result += i
print(result)
