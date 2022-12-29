vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
    if char in count:
       count[char] += 1
print(count)




line = "hello world i am pavan"
b = line.casefold()
b.split()
count = {}.fromkeys(vowels,0)
for char in b:
    if char in count:
        count[char] =1
print(count)
