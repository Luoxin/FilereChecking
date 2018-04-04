import hashlib
import temp_list as FileList

class verify(object):

    def __init__(self):
        pass

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

    def verifymain(self):
        pathList=FileList.getFileList()
        re={}
        for i in pathList:
            try:
                print(i)
                re[i]=self.__verifySHA512(i)
            except:
                pass
        # print(pathList)
        # print(re)
        FileList.delFileList()
        re=FileList.saveVerify(re)
        # print(re)
        return re

if __name__=="__main__":
    a=verify()
    a.verifymain()