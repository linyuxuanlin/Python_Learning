# -*- coding: utf-8 -*-

print('自定义绝对值函数:')
def my_abs(x):
	if x >= 0 :
		return x
	else:
		return -x

#函数可以同时返回多个值，但其实就是一个 tuple.


#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。		
print('一元二次方程求根：')
import math
def quadratic(a,b,c):
	delta=b*b-4*a*c
	x1=(-b+math.sqrt(delta))/(2*a)
	x2=(-b-math.sqrt(delta))/(2*a)
	return x1,x2

#测试：
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
