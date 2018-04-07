import datetime
import hashlib
import os
import shutil
import win32api
import win32con


class FileChecking():

    def __init__(self):
        print("正在进行初始化设置......")
        #默认的配置信息
        self.searchHeavyPaths=set()#等待查重的文件夹路径
        self.WaitForComparisonFiles=set()#等待对比的文件
        self.FileCheckValue={}#文件及其校验值
        self.result={}
        self.saveReaultPath="Result"


        #初始化

        #初始化临时文件夹
        # print("  正在尝试创建临时缓存目录......")
        # for i in range(1, 10):
        #     try:
        #         os.mkdir("temp")
        #         win32api.SetFileAttributes('temp', win32con.FILE_ATTRIBUTE_HIDDEN)  # 设置文件夹为隐藏
        #         print("  初始化临时文件夹成功")
        #         break
        #     except:
        #         print("  第{}次初始化失败，正在重试......".format(i))
        #         pass

        #重命名存储结果的文件
        nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+".txt"
        self.saveReaultPath+=str(nowTime)
        print(self.saveReaultPath)

        print("初始化完成！")

        #执行主程序
        self.__main()

        #清理垃圾
        # print("正在尝试删除临时缓存目录......")
        # for i in range(1, 10):
        #     try:
        #         print(".", end=" ")
        #         shutil.rmtree("temp")
        #         break
        #     except:
        #         print("第{}次删除失败，正在重试......".format(i))

        print("程序执行完成，按任意键退出程序")
        a=input()



    def __getSearchHeavyPaths(self):#获取需要进行查重的文件夹目录
        print("请输入路径(以#为输入结束标志）：", end="")
        while True:
            print("请输入路径：", end="")
            path = input()
            if path == "#":
                break
            else:
                if path not in self.searchHeavyPaths:
                    self.searchHeavyPaths.add(path)
                else:
                    print("输入的路径重复，请检查路径。")

    def __findFileTree(self,path):#获取需要对比的文件完整路径
        path = path.replace("\\", "/")
        mlist = os.listdir(path)  # 获取目录下的所有文件
        for m in mlist:
            try:
                mpath = os.path.join(path, m)
                if os.path.isfile(mpath):
                    pt = os.path.abspath(mpath)
                    if pt not in self.WaitForComparisonFiles:
                        self.WaitForComparisonFiles.add(pt)
                    print("  "+pt)
                else:
                    pt = os.path.abspath(mpath)
                    print("  "+pt)
                    self.__findFileTree(pt)
            except:
                pass

    def __findAllFileTree(self):#查找每一个待查重的文件的所有的子文件
        print("\n\n\n\n准备获取所有待对比的文件完整路径......")
        for path in self.searchHeavyPaths:
            try:
                self.__findFileTree(path)
            except:
                pass
        print("获取文件目录树完成！")

    def __getAllMessageDigestAlgorithm(self):#通过信息摘要算法计算文件的校验值
        print("\n\n\n\n准备进行文件校验值的计算")
        for filePath in self.WaitForComparisonFiles:
            try:
                print(filePath)
                self.FileCheckValue[filePath]=self.__mdavMD5(filePath)
                print("\n")
            except:
                pass
        print("获取全部校验码完毕！")

    def __contrastCheckValue(self):
        print("正在处理数据......")
        self.result = {}
        for i in self.FileCheckValue.values():
            self.result[i] = []
        for i in self.FileCheckValue.keys():
            self.result[self.FileCheckValue[i]].append(i)
        print(self.FileCheckValue)
        print("查重完成，正在生成结果......")

    def __saveReault(self,pt):
        file=open(self.saveReaultPath,"a")
        file.write(pt+"\n")
        file.close()

    def __showReault(self):
        for i in self.result.keys():
            if self.result[i].__len__()>1:
                print("下列文件的重复文件(校验码{})：".format(i))
                self.__saveReault("\n\n\n下列文件的重复文件(校验码{})：".format(i))
                for j in self.result[i]:
                    print(j)
                    self.__saveReault(j)


    def __main(self):
        self.__getSearchHeavyPaths()
        self.__findAllFileTree()
        self.__getAllMessageDigestAlgorithm()
        self.__contrastCheckValue()
        self.__showReault()


    #相关的信息摘要算法
    def __mdavMD5(self, path):
        md5file = open(path, 'rb')
        md5 = hashlib.md5(md5file.read()).hexdigest()
        md5file.close()
        print(md5)
        return md5

    def __mdavSHA1(self, path):
        sha1file = open(path, 'rb')
        sha1 = hashlib.sha1(sha1file.read()).hexdigest()
        sha1file.close()
        print(sha1)
        return sha1

    def __mdavSHA128(self, path):
        sha1file = open(path, 'rb')
        sha128 = hashlib.shake_128(sha1file.read()).hexdigest()
        sha1file.close()
        print(sha128)
        return sha128

    def _mdavSHA256(self,path):
        sha1file = open(path, 'rb')
        sha256 = hashlib.sha_256(sha1file.read()).hexdigest()
        sha1file.close()
        print(sha256)
        return sha256


    def __mdavSHA512(self, path):
        sha512file = open(path, 'rb')
        sha512 = hashlib.sha512(sha512file.read()).hexdigest()
        sha512file.close()
        print(sha512)
        return sha512


if __name__ == '__main__':
    a=FileChecking()
