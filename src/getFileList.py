import os
from temp_list import File

def listfiels(path):
    path = path.replace("\\", "/")
    mlist = os.listdir(path)#获取目录下的所有文件
    tempFile=File()
    for m in mlist:
        try:
            mpath = os.path.join(path, m)
            if os.path.isfile(mpath):
                pt = os.path.abspath(mpath)
                tempFile.saveFileList(pt+"\n")
                print(pt)
            else:
                pt = os.path.abspath(mpath)
                print(pt)
                listfiels(pt)
        except:
            pass

if __name__=="__main__":
    listfiels("D:/")
