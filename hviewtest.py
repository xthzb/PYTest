from hview import *

def g():
    frm.x+=10
    frm.y+=10

frm=HForm()
frm.text='窗口'
frm.addButton('asdf',g,10,1)
frm.addButton('asdf',g,10,50)
frm.show()

