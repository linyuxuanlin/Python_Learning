# -*- coding: utf-8 -*-

#python 没有 do ~ while 语法，可以这样实现：

print('执行如图所示的流程图，则输出的S值为:')

S=0;x=1;y=1;n=9

while True:
	S=S+x*y
	if n<=1:
		break
	else:
		x=x+1
		y=y+1
		n=n-1

print(S)