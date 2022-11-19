elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
c1=0
sum=0
sum1=0
while i<len(elements):
	if elements[i]%2==0:
		sum=sum+elements[i]
		c=c+1
	else:
		sum1=sum1+elements[i]
		c1=c1+1
	i+=1
aver1=sum//c
aver2=sum1//c1
	
print("avg of even=",aver1)
print("avg of odd=",aver2)

avg of even and odd
