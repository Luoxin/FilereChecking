import getFileList
import verify
from temp_list import File

if __name__=="__main__":
    tempFile=File()
    a=tempFile.creatTempTool()
    print("")
    print("请输入路径(以#为输入结束标志）：", end="")
    while True:
        print("请输入路径：",end="")
        path = input()

        if path == "#":
            break
        else:
            tempFile.saveToolPath(path)


    print("获取到如下路径：")
    path=tempFile.getToolPath()#获取需要对比的文件夹路径
    for i in path:
        getFileList.listfiels(i)


    print("正在对比文件..........")
    temp=verify.verify()
    list=temp.verifymain()
    print("-----------------------")
    # print(list)
    for i in list.keys():
        if list[i].__len__()>1:
            print("下列文件的重复文件({})：".format(i))
            for j in list[i]:
                print(j)
    a=tempFile.deleteTempTool()
