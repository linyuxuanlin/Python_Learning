# -*- coding: utf-8 -*-

print('迭代输出元素:')
abc = [1,2,3,4,5,6,7,8,9,10]
for i in abc:
	print(i)


print('求和:')
sum=0
for x in abc:
	sum=sum+x
print(sum)


print('整数列求和:')
print(range(101)) #0~100的整数列
sum=0
for x in range(101):
	sum=sum+x
print(sum)	


print('自定义数列，求和:')
#n=range(101)
Sn=0
for n in range(11):
	An=2*n+1
	Sn=Sn+An
print(Sn)
