a=[6,1,3,5,6,3,1]
s=set(a)
d=list(s)
print(d)
i=0
mult=1
while i<len(d):
	mult*=d[i]
	i+=1
print(mult)