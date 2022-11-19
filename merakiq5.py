elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[ ]
b=[ ]
while i<len(elements): 
    if elements[i]%2==0:
        a.append(elements[i])
    else:
        b.append(elements[i])
    i+=1
print("even=",a)
print("odd=",b)