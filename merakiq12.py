n=["a","n","t","a","a","t","n","n","a","x","u","u","g","a","x","a"]
i=0
a=[]
while i<len(n):
	j=0
	c=0
	while j<len(n):
	    if n[i]==n[j]:
	    	c=c+1
	    j+=1
	if n[i]not in a:
	    a+=n[i]
	    print(n[i],c)
	i+=1