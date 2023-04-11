from hview import *

def g():
    frm.x+=10
    frm.y+=10

frm=HForm()
frm.text='窗口'
Button(frm,text='确 定',bg='Ivory',font=('微软雅黑',12),width=0,height=0,command=g).place(x=5,y=5)
frm.show()