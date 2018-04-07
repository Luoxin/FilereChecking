#对比文件

import hashlib
from temp_list import File


class verify(object):

    __doc__ = "计算文件的目录并校验"

    def __init__(self):
        self.tempFile = File()

    def __verifyMD5(self,path):
        md5file = open(path, 'rb')
        md5 = hashlib.md5(md5file.read()).hexdigest()
        md5file.close()
        print("md5"+md5)
        return md5

    def __verifySHA1(self,path):
        sha1file = open(path, 'rb')
        sha1 = hashlib.sha1(sha1file.read()).hexdigest()
        sha1file.close()
        print("sha1"+sha1)
        return sha1

    def __verifySHA512(self,path):
        sha512file = open(path, 'rb')
        sha512 = hashlib.sha512(sha512file.read()).hexdigest()
        sha512file.close()
        print("sha512"+sha512)
        return sha512

    def verifymain(self):#获取校验值并对比
        pathList=self.tempFile.getFileList()
        re={}
        for i in pathList:
            try:
                print(i)
                re[i]=self.__verifyMD5(i)
            except:
                pass
        # print(pathList)
        # print(re)
        re=self.tempFile.saveVerify(re)
        # print(re)
        return re

if __name__=="__main__":
    a=verify()
    a.verifymain()