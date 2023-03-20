import os
def getAllImg(path):
    result = []
    filelist = os.listdir(path)
    for file in filelist:
        aName=os.path.join(path, file)
        if os.path.isfile(aName):
            if file.split('.')[1] in ('jpg', 'png'):
                print(aName)
                #result.append(aName)
    return result

getAllImg(r'C:\Users\xthzb\Desktop\PYDOWN\img')