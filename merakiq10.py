element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
count1=0
count2=0
sum1=0
sum2=0
while i<len(element):
	if element[i]%2==0:
		sum1=sum1+element[i]
		count1=count1+1
	else:
		sum2=sum2+element[i]
		count2=count2+1
	i+=1
print('sum1=',sum1)
print('sum2=',sum2)
print('count1=',count1)
print('count2=',count2)
print('total sum=',sum1+sum2)
print('total count=',count1+count2)
print('even ',sum1,'count1=',count1)
print('odd',sum2,'count2=',count2)
print('avg1=',sum1/count1)
print('avg2=',sum2/count2)
print('total avg=',sum1/count1+sum2/count2)
