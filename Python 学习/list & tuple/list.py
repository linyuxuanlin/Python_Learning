# -*- coding: utf-8 -*-

print('列出 list:')
abc = ['a', 'b', 'c']
print(abc)


print('元素个数:')
print(len(abc))


print('索引访问某个元素(从0编号):')
print(abc[0])
print(abc[1])
print(abc[-1])  # 最后一个元素
print(abc[-2])  # 倒数第二个元素


print('追加元素到末尾:')
abc.append('insert-last')
print(abc)


print('在某位置插入元素:')
abc.insert(1, 'insert-somewhere')
print(abc)


print('删除末尾元素:')
print(abc.pop())  # 执行一次，同时显示被删除的元素
print(abc)


print('删除指定元素:')
print(abc.pop(1))  # 执行一次，同时显示被删除的元素
print(abc)


print('替换某个元素:')
abc[1] = 'B'
print(abc)
