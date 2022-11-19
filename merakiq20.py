number=[50,40,23,70,56,12,5,10,7]
i=0
max=0
max2=0
max3=0
while i<len(number):
	if number[i]>=max:
		max=number[i]
	i+=1
j=0
max2=0
while j<len(number):
	if number[j]<max:
		if number[j]>max2:
			max2=number[j]
	j+=1
k=0
while j<len(number):
	if number[k]<max:
		if number[k]>max3:
			max3>=number[k]
		j+=1
print("first",max)
print("second",max2)
print('third',max3)