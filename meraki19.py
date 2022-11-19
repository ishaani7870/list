list=[1,2,3,1,2,2]
i=0
a=[]
while i<len(list):
	if list[i] not in a:
		a.append(list[i])
	i+=1
print(a)