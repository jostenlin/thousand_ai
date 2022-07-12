# 作業4-1
print('A:')
A=[]
for i in range(2):  
  r=[int(s) for s in input().split()]
  A.append(r)

print('B:')
B=[]
for i in range(3):  
  r=[int(s) for s in input().split()]
  B.append(r)

import numpy as np
A=np.array(A)
B=np.array(B)
print(np.matmul(A,B))



# 作業4-2
School=[]
myClass=['A','B','C']
for c in myClass:
  print(f'{c} class:',end='') 
  r=[float(s) for s in input().split()]
  School.append(r)

import numpy as np
School=np.array(School)
s=np.sum(School,axis=1)
m=np.max(School,axis=1)
for idx,c in enumerate(myClass):
  print(f'{c} class 總和: {s[idx]}, 最大: {m[idx]}')


