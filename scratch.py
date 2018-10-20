import re
name = input("Enter file:")
if len(name) == 0:
    name = "regex.txt"
go = open(name)
boing = re.findall('[0-9]+',go.read())
sum = 0
for x in boing:
    x = int(x)
    sum = sum + x
print(sum)