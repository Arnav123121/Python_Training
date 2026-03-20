# code:- Find count of special character in a string
import re
var ='gasgg54@#vsvcsd!s*'
count =0
for i in var:
    # z=re.findall('[a-z,0-9]',i)
    z=ord(i)
    # print(z)
    # if z:
    if z>=97 and z<=122:
        continue
    elif z>=48 and z<=57:
        continue
    else:
        count+=1
print(count)