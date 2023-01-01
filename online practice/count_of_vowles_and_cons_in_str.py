string = "pavan new project"
vowels = ("a","A","e","E","i","I","o","O","u","U")
vowel = 0
consonent =0
for i in string:
     if i in vowels:
         vowel +=1
     elif i.isalpha():
         consonent += 1
print("total no of characters in the string is",len(string))
print("vowels in the given string is ",vowel)
print("consonents in the given string",consonent)