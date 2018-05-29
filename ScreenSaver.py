from random import randint
from tkinter import *

class RandomBall:

    __doc__ = "球"

    def __init__(self,canvas,scrnwidth,scrnheight):
        #绘图
        self.canvas=canvas

        #球心坐标
        self.xpos=randint(10,int(scrnwidth))
        self.ypos=randint(10,int(scrnheight))
        #移动速度
        self.xvelocity=randint(6,12)
        self.yvelocity=randint(6,12)
        #绘图坐标
        self.scrnwidth=scrnwidth
        self.scrnheight=scrnheight
        #半径
        self.radius=randint(40,70)
        #颜色
        r=lambda :randint(0,255)
        self.color="#%02x%02x%02x"%(r(),r(),r())

    def create_ball(self):
        x1=self.xpos-self.radius
        y1=self.ypos-self.radius
        x2=self.xpos+self.radius
        y2=self.ypos+self.radius
        self.itm=self.canvas.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)

    def move_ball(self):
        self.xpos+=self.xvelocity
        self.ypos+=self.yvelocity
        if self.ypos>=self.scrnheight-self.radius:
            self.yvelocity=-self.yvelocity
        if self.ypos<=self.radius:
            self.yvelocity=abs(self.yvelocity)
        if self.xpos>=self.scrnwidth-self.radius or self.xpos<=self.radius:
            self.xvelocity=-self.xvelocity
        self.canvas.move(self.itm,self.xvelocity,self.yvelocity)

class ScreenSaver:
    balls=[]

    def __init__(self,num_balls):
        self.root=Tk()
        self.root.geometry(str(self.root.winfo_screenwidth())+"x"+str(self.root.winfo_screenheight()))#将窗口大小设置为【屏幕大小

        w,h=self.root.winfo_screenwidth(),self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.attributes('-alpha',0.3)
        self.root.bind("<Any-KeyPress>",self.myquit)
        # self.root.bind("<Any-Button>",self.myquit)
        self.root.bind("<Motion>",self.myquit)
        self.canvas=Canvas(self.root,width=w,height=h)
        self.canvas.pack()
        for i in range(num_balls):
            ball=RandomBall(self.canvas,scrnheight=h,scrnwidth=w)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(20,self.run_screen_saver)

    def myquit(self,event):
        self.root.destroy()


if __name__ == '__main__':
    try:
        i=open(".\setting.ini","r")
        count=int(i.readline())
        i.close()
        if count>50:
            count=50
        print(count)
        ScreenSaver(int(count))
        print("successful")
    except:
        ScreenSaver(18)


