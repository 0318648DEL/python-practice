from tkinter import *
import random

class Histogram:
    def display(self):
        self.canvas.delete("grim")
        histogram=[0]*26
        for i in range(1000):
            histogram[random.randint(0,25)]+=1
        maxCount=int(max(histogram))
        self.canvas.create_line(10,self.height-10,self.width-10,self.height-10)
        barWid=(self.width-20)/26
        for i in range(26):
            self.canvas.create_rectangle(i*barWid+10,self.height-((self.height-20)*histogram[i]/maxCount),(i+1)*barWid+10,self.height-10,tags="grim")
            self.canvas.create_text(i*barWid+10+10,self.height-10+5,text=chr(i+ord('a')),tags="grim")
            self.canvas.create_text(i*barWid+10+10,self.height-((self.height-13)*histogram[i]/maxCount),text = str(histogram[i]),tags="grim")

    def __init__(self):
        window=Tk()
        window.title("빈도수")
        self.width=500
        self.height=300
        self.canvas=Canvas(window,width=self.width,height=self.height,bg="white")
        self.canvas.pack()
        Button(window,text="히스토그램 그리기",command=self.display).pack()

        window.mainloop()

Histogram()