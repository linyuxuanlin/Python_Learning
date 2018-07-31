# -*- coding: utf-8 -*-

print('设置参数，计算乘方:')
def power(x,n):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s
print(power(3,2))

print('设置默认参数:')
def power(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s
print(power(3))
print(power(3,3))

#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
#变化小的参数就可以作为默认参数。

#未完结：可变参数