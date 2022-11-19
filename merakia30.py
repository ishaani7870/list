list=["a","n","t","a","a","t","n","a","x","u","g","a","x","a"]
L= []
for I in list :
      C=0
      for j in list :
          If I==j: 
              C+=1
      if I not in L:
          L. append(I) 
          print([I, C],end="") 
                 
# output=(['a',5]['n',3]['t',2]['x',2]['u',1]['g',1])