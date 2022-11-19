elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
a="even"
b="odd"
while i<len(elements): 
    if elements[i]%2==0:
    	sum=sum+(elements[i])
    else:
        sum1==sum1+(elements[i])
    i+=1
print("sum of even=",sum,"sum of odd=",sum1)
