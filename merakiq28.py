a=["my_name_is_kajal_ishaani"]
i=0
c=0
b=""
while i<len(a):
	j=0
	while j<len(a[i]):
		if a[i][j]=="_":
			c+=1
		j+=1
	i+=1
print(c,"space")