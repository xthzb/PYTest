# 界面显示

from tkinter import *

class HForm(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.text='HForm'
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        self.width=300
        self.height=250
        self.x=(self.sw-self.width) / 2
        self.y=(self.sh-self.height) / 2-60
        

    def __setattr__(self, __name: str, __value: any) -> None:
        returnVal=super().__setattr__(__name, __value)
        match __name:
            case 'text':
                self.title(__value)
            case 'width':
                self.geometry('%dx%d' %(__value,self.winfo_height()))
                self.update()
                pass
            case 'height':
                self.geometry('%dx%d' %(self.winfo_width(),__value))
                self.update()
                pass
            case 'x':
                self.geometry("%dx%d+%d+%d" %(self.width,self.height,__value,self.winfo_y()))
                self.update()
            case 'y':
                self.geometry("%dx%d+%d+%d" %(self.width,self.height,self.winfo_x(),__value))
                self.update()
        return returnVal
        
    
    def show(self):
        self.mainloop()
        pass

    def addButton(self,__text,__command,__x,__y):
        Button(self,text=__text,bg='Ivory',font=('微软雅黑',10),width=0,height=0,command=__command).place(x=__x,y=__y)
        pass