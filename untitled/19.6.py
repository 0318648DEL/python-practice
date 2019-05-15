from tkinter import *
import random

class Box:
    handle=None
    imageList=[]

    @staticmethod
    def initClassBox(handle):
        Box.imageList=[]
        Box.imageList.append(PhotoImage(file="image/o.gif"))
        Box.imageList.append(PhotoImage(file="image/x.gif"))
        Box.imageList.append(PhotoImage(file="image/empty.gif"))
        Box.handle=handle

    def __init__(self,frame,row,col):
        self.row=row
        self.col=col
        self.button=Button(frame,image=Box.imageList[2],command=lambda box=self:self.handle.pressed(box))
        self.button.grid(row=col,column=row)
        self.token=2

    def enable(self):
        if self.token==2:
            return True
        return False

    def press(self,player):
        self.token=player
        self.button.configure(image=self.imageList[player])

    def unable(self):
        self.token=3

class TicTacToe:
    def checkAll(self):
        for box in self.boxList:
            if box.token==2:
                return False
        return True
    def winnerCheck(self):
        for r in range(3):
            if self.boxList[0*3+r].token==self.boxList[1*3+r].token==self.boxList[2*3+r].token:
                return self.boxList[0*3+r].token

        for c in range(3):
            if self.boxList[c*3+0].token==self.boxList[c*3+1].token==self.boxList[c*3+2].token:
                return self.boxList[c*3+0].token

        if self.boxList[0].token==self.boxList[4].token==self.boxList[8].token:
            return self.boxList[0].token

        if self.boxList[2].token==self.boxList[4].token==self.boxList[6].token:
            return self.boxList[0].token

        if self.checkAll():
            return 4
    def endGame(self):
        for box in self.boxList:
            box.unable()
    def pressed(self,box):
        if box.enable():
            if self.turn==0:
                box.press(0)
                self.label.configure(text="0차례")

            elif self.turn==1:
                box.press(1)
                self.label.configure(text="X차례")

            self.turn=not self.turn
        isGameEnd=self.winnerCheck()
        if isGameEnd==0:
            self.label.configure(text="0의 승리")
            self.endGame()
        elif isGameEnd==1:
            self.label.configure(text="X의 승리")
            self.endGame()
        elif isGameEnd==4:
            self.label.configure(text="무승부")
            self.endGame()
    def __init__(self):
        window=Tk()
        Box.initClassBox(self)
        frame1=Frame(window)
        frame1.pack()
        self.turn=0
        self.boxList=[]
        for c in range(3):
            for r in range(3):
                self.boxList.append(Box(frame1,r,c))
        frame2=Frame(window)
        frame2.pack()
        self.label=Label(frame2,text="O차례")
        self.label.pack()
        window.mainloop()

TicTacToe()
