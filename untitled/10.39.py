from tkinter import *
import random
import tkinter.messagebox
import tkinter.simpledialog
import re


class CardGame:
    def __init__(self):
        window=Tk()
        frame1=Frame(window)
        frame1.pack()
        Button(frame1,text="새로고침",command=self.reset).pack()
        frame2=Frame(window)
        frame2.pack()
        self.index=[x for x in range(52)]
        self.imageList=[]
        for i in range(1,53):
            self.imageList.append(PhotoImage(file="card/"+str(i)+".gif"))

        self.labelList=[]
        for i in range(4):
            self.labelList.append(Label(frame2,image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)
        frame3=Frame(window)
        frame3.pack()
        Label(frame3,text="수식을 입력하세요").pack(side=LEFT)
        self.e=Entry(frame3,text='')
        self.e.pack(side=LEFT)
        Button(frame3,text="확인",command=self.check).pack(side=LEFT)
        window.mainloop()

    def reset(self):
        random.shuffle(self.index)
        for i in range(4):
            self.labelList[i].configure(image=self.imageList[self.index[i]])

    def check(self):
        cardNumbers=[]
        for i in range(4):
            cardNumbers.append(self.index[i]%13+1)
        cardNumbers.sort()
        expression=self.e.get()
        answer=eval(expression)
        expression=re.sub('[()/\+\-\*]',' ',expression)
        userNumbers=expression.split()
        userNumbers=[eval(x) for x in userNumbers]
        print(userNumbers)
        userNumbers.sort()
        if userNumbers==cardNumbers:
            if answer==24:
                tkinter.messagebox.showinfo("정확","맞는 값입니다.")
            else:
                tkinter.messagebox.showinfo("틀림",self.e.get()+"는 24가 아님.")
        else:
            tkinter.messagebox.showinfo("틀림","보여지는 카드를 사용해야 합니다.")

CardGame()