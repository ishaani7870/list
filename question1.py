b=["Red","Green","Blue"]
i=0
L=[]
while i<len(b):
	a=[]
	j=0
	while j<len(b[i]):
		a.append(b[i][j])
		j=j+1
	L.append(a)
	i+=1
print(L)