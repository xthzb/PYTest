#集合
names=set([1,2,3])
names2=set('hezhengbo')

# 自动去重

# 并集、交集、差集 | & -。对称差集 ^
#a=names | names2
a1=set([1,2,3])
a2=set([2,3,4])
b1=a1 | a2
b2=a1 & a2
b3=a1 - a2
b4=a1 ^ a2
print(b4)

# 添加。add(),update()
names.add(4)
names.update([5,6,7])
