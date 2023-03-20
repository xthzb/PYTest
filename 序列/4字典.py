# 字典，最完善的数据类型
hzb1={}
hzb2=dict()

hzb={
    'name':'贺正波',
    'sex':'男',
    'age':37
}
name='name'
hzbName=hzb['name']
hzbName=hzb.get('name')

# 转为列表
hzb3=list(hzb)

# 删除项
del hzb['age']

