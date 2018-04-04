import os

def saveFileList(pt):
    file=open('Fist.txt','a')
    file.write(pt)
    file.close()

def getFileList():
    file=open('Fist.txt',"r")
    pt=[]
    for pti in file.readlines():
        pt.append(pti.strip("\n"))
        # print(pti)
    file.close()
    # print(pt)
    return pt

def delFileList():
    try:
        os.remove("Fist.txt")
    except:
        pass

def saveVerify(list):
    # print(list)
    result={}
    for i in list.keys():
        result[list[i]]=[]
    # print(result)
    for i in list:
        result[list[i]].append(i)
    # print(result)
    return result
