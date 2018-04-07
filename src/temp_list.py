import os
import shutil
import win32api
import win32con


class File():

    __doc__ = "对临时文件的相关操作"

    def __init__(self):
        self.tempFilePath="./temp/File.list"#临时的存储待对比的文件路径
        self.ToolPath="./temp/Tool.list"#存储需要查重的文件夹路径

    def creatTempTool(self):#创建临时文件夹
        print("正在尝试创建临时缓存目录",end=" ")
        for i in range(1,10):
            try:
                print(".",end=" ")
                os.mkdir("temp")
                win32api.SetFileAttributes('temp', win32con.FILE_ATTRIBUTE_HIDDEN)#设置文件夹为隐藏
                return True
            except:
                pass

    def deleteTempTool(self):#删除临时文件
        print("正在尝试删除临时缓存目录",end=" ")
        for i in range(1, 10):
            try:
                print(".",end=" ")
                shutil.rmtree("temp")
                return True
            except:
                pass


    def saveToolPath(self,path):#保存待查重的文件路径
        file = open(self.ToolPath, 'a')
        file.write(path+"\n")
        file.close()

    def getToolPath(self):#获取待查询的文件夹路径
        file = open(self.ToolPath, "r")
        path = []
        for pti in file.readlines():
            path.append(pti.strip("\n"))
        file.close()
        return path


    def saveFileList(self,pt):#保存已获取的待对比的文件列表
        file=open(self.tempFilePath,'a')
        file.write(pt)
        file.close()

    def getFileList(self):#读取待对比的文件列表
        file=open(self.tempFilePath,"r")
        pt=[]
        for pti in file.readlines():
            pt.append(pti.strip("\n"))
            # print(pti)
        file.close()
        # print(pt)
        return pt




    def saveVerify(self,list):#对比校验值
        # print(list)
        result={}
        for i in list.keys():
            result[list[i]]=[]
        # print(result)
        for i in list:
            result[list[i]].append(i)
        # print(result)
        return result
