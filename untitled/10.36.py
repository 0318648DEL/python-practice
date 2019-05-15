from tkinter import *
import tkinter.messagebox
import random

class Linear:
    def step(self):
        minIndex=self.index
        for i in range(self.index+1,20):
            if self.numbers[minIndex]>self.numbers[i]:
                minIndex=i
        self.numbers[self.index],self.numbers[minIndex]=self.numbers[minIndex],self.numbers[self.index]
        self.draw()
        barW=(self.width-10-10)/20
        self.canvas.delete("red")
        self.canvas.create_rectangle(10 + self.index * barW, 10 + (self.height - 20) * (1 - self.numbers[self.index] / 20),
                                     10 + (self.index + 1) * barW, self.height - 10, fill='red' ,tags="red")
        self.index+=1

    def draw(self):
        self.canvas.delete("grim")
        self.canvas.delete("red")
        barW = (self.width - 10 - 10) / 20
        for i in range(20):
            self.canvas.create_rectangle(10 + i * barW, 10 + (self.height - 20) * (1 - self.numbers[i] / 20),
                                         10 + (i + 1) * barW, self.height - 10, tags="grim")
            self.canvas.create_text(17 + i * barW, 7 + (self.height - 20) * (1 - self.numbers[i] / 20),
                                    text=str(self.numbers[i]), tags="grim")

    def reset(self):
        random.shuffle(self.numbers)
        self.canvas.delete("grim")
        self.canvas.delete("red")
        barW=(self.width-10-10)/20
        for i in range(20):
            self.canvas.create_rectangle(10+i*barW,10+(self.height-20)*(1-self.numbers[i]/20),10+(i+1)*barW,self.height-10,tags="grim")
            self.canvas.create_text(17+i*barW,7+(self.height-20)*(1-self.numbers[i]/20),text=str(self.numbers[i]),tags="grim")
        self.index=0

    def __init__(self):
        window=Tk()
        self.index=0
        self.width=400
        self.height=200
        self.canvas=Canvas(window,width=self.width,height=self.height,bg='white')
        self.canvas.pack()
        self.numbers=[x for x in range(1,21)]
        frame=Frame(window)
        frame.pack()
        Label(frame,text="키를 입력하세요").pack(side=LEFT)
        self.e=Entry(frame,text='',justify=RIGHT,width=3)
        self.e.pack(side=LEFT)
        Button(frame,text="다음단계",command=self.step).pack(side=LEFT)
        Button(frame,text="재설정",command=self.reset).pack(side=LEFT)

        window.mainloop()

Linear()
