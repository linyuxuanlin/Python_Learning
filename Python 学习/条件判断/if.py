# -*- coding: utf-8 -*-

print('假设一场考试，80~100为优，60~80为良，60以下为不及格')


#grade=70

grade=input('请输入成绩')
grade=int(grade) #char --> int 

if grade < 100 and grade > 0:
	if grade < 60:
		print('不及格')
	elif grade < 80:
		print('良')
	else :
		print('优秀')
else:
	print('格式不规范')