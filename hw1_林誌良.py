# 作業1-1
from math import floor
a=input()
b=input()
try:
  # round四捨六入五平分(奇進偶捨)
  ans=int(a)/int(b)

  # 題目要求逢五必進
  if(floor(ans*1000))%100 in [5,25,45,65,85]:
    ans+=0.001
  
  print(round(ans,2))
except ValueError:
  print('請輸入正確數字格式')



# 作業1-2
a=int(input())
if(a%6==0):
  print(f'{a} 為 6的倍數。')
elif(a%2==0):
  print(f'{a} 為 2的倍數。')
elif(a%3==0):
  print(f'{a} 為 3的倍數。')



# 作業1-3
n=int(input())

# 時
h=n//(60*60)
n=n%(60*60)

# 分
m=n//60
n=n%60

# 秒
s=n

print(f'{h}時 {m}分 {s}秒')



# 作業1-4
n=int(input())
i=1
while(i<n):
  if(i%2==1):
    print(i,end=' ')
  i+=1

