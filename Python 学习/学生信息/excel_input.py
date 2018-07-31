# -*- coding: utf-8 -*-

print(':')

import xlrd

workbook = xlrd.open_workbook(u'/Users/linyuxuan/Desktop/工作簿1.xlsx')

sheet_names= workbook.sheet_names()


#获取某一行数据的函数
def print_row(a):
	for sheet_name in sheet_names:
		print("工作表名称:",sheet_name)
		print("第",a,"行的数据:")
		sheet1 = workbook.sheet_by_name(sheet_name)
		print(sheet1.row_values(a-1))
		print(" ")

#获取某一列数据的函数
def print_col(b):
	for sheet_name in sheet_names:
		print("工作表名称:",sheet_name)
		print("第",b,"列的数据:")
		sheet1 = workbook.sheet_by_name(sheet_name)
		print(sheet1.col_values(b-1))
		print(" ")




#print_row(1)
#print_col(1)


n=1
while n<1000:
	print_row(n)
	n=n+1
