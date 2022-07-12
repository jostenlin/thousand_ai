# 作業2-1
n=int(input())
lst=list(range(1,n+1))
print('+'.join([str(i) for i in lst]),'=',str(sum(lst)))



# 作業2-2
lst=input()
n=int(input())
lst=lst.strip('[').strip(']').split(',')
print([i for i in lst if int(i)>=n])



# 作業2-3
lst=input()
lst=lst.split(' ')
print(sum([int(i) for i in lst if int(i)%2==0]))



# 作業2-4
str1=input() # 主字串
str2=input() # 子字串
count=0
for i in range(len(str1)-len(str2)+1):
  if(str1[slice(i,i+len(str2))]==str2):    
    count+=1
print(count)
