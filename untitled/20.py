from tkinter import *
import random
class TicTacToe:
    def again(self):
        for r in range(6):
            for c in range(7):
                self.buttonList[r*7+c]["image"]=self.imageList[2]
                self.buttonList[r*7+c]["text"]=''
    def pressed(self,Row,Col):
        for r in range(5,-1,-1):
            if self.buttonList[r*7+Col]["text"]=='':
                if self.turn:
                    self.buttonList[r*7+Col].configure(text='O',image=self.imageList[0])
                else:
                    self.buttonList[r*7+Col].configure(text='X',image=self.imageList[1])
                self.turn=not self.turn
                break
    def __init__(self):
        window=Tk()
        self.turn=True
        self.imageList=[]
        self.imageList.append(PhotoImage(file="image/o.gif"))
        self.imageList.append(PhotoImage(file="image/x.gif"))
        self.imageList.append(PhotoImage(file="image/empty.gif"))
        self.buttonList=[]
        frame1=Frame(window)
        frame1.pack()
        for r in range(6):
            for c in range(7):
                self.buttonList.append(Button(frame1,image=self.imageList[2],command=lambda Row=r,Col=c:self.pressed(Row,Col)))
                self.buttonList[r*7+c].grid(row=r,column=c)
        frame2=Frame(window)
        frame2.pack()
        Button(frame2,text="다시생성",command=self.again).pack()
        window.mainloop()

TicTacToe()