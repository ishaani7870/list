list=[5,6,[],3,[],[],9]
i=0
while i<len(list):
	j=0
	while j<len(list[i]):
	   if list[i]not in list:
	   	list[i]==[]
	   list.remove([])
	   print(list[i])
	   i+=1