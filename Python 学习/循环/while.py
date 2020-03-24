# -*- coding: utf-8 -*-

print('计算100以内奇数的和:')
sum=0
n=99
while n>0:
	sum = sum+n
	n=n-2
print(sum)


#break 和 continue 必须配合if语句使用。别滥用，容易乱。

print('break 结束当前循环:')
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

print('continue 跳过当前循环:')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)