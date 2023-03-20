#创建列表
names=['a1','a2']
names2=[]
names3=list()
names4=[0,[1,2,[3,4,5]]]

#添加 追加 插入
names.append('a3')
names.insert(2,'a2.2')

# 提取子列表，
a=names[0:1]
b=names[1:4]

# 重新赋值
names[1]='b2'
c=names[1:4]
print(b,c)
print(names4[1][2][0])
