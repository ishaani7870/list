elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
c1=0
c2=0
while i<len(elements): 
    if elements[i]%2==0:
    	sum=sum+(elements[i])
    	c1=c1+1
    else:
        sum1=sum+(elements[i])
        c2=c2+1
        i+=1
        avg1=sum//c1
        avg2=sum//c2
    i+=1
print("avg of even=",even)
print("avg of odd=",odd)
