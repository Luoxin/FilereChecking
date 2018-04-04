import getFileList
import verify

if __name__=="__main__":
    print("请输入路径：")
    path=input()
    print("获取到如下路径：")
    getFileList.listfiels(path)
    print("正在对比文件..........")
    temp=verify.verify()
    list=temp.verifymain()
    print("-----------------------")
    print(list)
    for i in list.keys():
        if list[i].__len__()>1:
            print("下列文件的重复文件({})：".format(i))
            for j in list[i]:
                print(j)
