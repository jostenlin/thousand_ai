# 作業3-1
n=int(input())
for i in range(n,0,-1):
  print(' '*(n-i)+'*'*i)
  
  
# 作業3-2
n=int(input())
for i in range(n):  
  print(' '*(n-i-1)+'*'*(i+1))


# 作業3-3
p1=[int(i) for i in input('point1:').split()]
p2=[int(i) for i in input('point2:').split()]
ans=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
print(f'{ans:.2f}')


# 作業3-4
import random
import numpy as np
row=int(input('row:'))
col=int(input('col:'))
m=[]
for i in range(row):
  r=[]
  for j in range(col):
    r.append(random.randint(1,20))
  m.append(r)
np.mat(m)
