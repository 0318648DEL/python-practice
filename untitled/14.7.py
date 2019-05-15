from tkinter import*
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

string=""
fname=""
def fileopen():
    global fname
    fname=askopenfilename()
    e.delete(0,END)
    e.insert(END,fname)

def handle():
    try:
        f=open(fname)
        content=f.read()
    except FileNotFoundError:
        tkinter.messagebox.showerror("FileErrorMessageBox","잘못된 파일명입니다.")
        return

    histogram=[0]*26
    new=content.lower()

    for c in new:
        if c.isalpha():
            histogram[ord(c) - ord('a')]+=1

    maxCount=max(histogram)
    barW=(500-10-10)/26

    canvas.delete("grim")
    for i in range(26):
        canvas.create_rectangle(10+(i*barW),10+170*(1-histogram[i]/maxCount),10+(i+1)*barW,180,tags="grim")
        canvas.create_text(10+(i*barW)+7,180+5,text=chr(i+ord('a')),tags="grim")
        canvas.create_text(10+(i*barW)+7,5+170*(1-histogram[i]/maxCount),text=str(histogram[i]),tags="grim")


window=Tk()
frame1=Frame(window)
frame1.pack()
canvas=Canvas(frame1,width=500,height=200,bg="white")
canvas.pack()

frame2=Frame(window)
frame2.pack()
Label(frame2,text="문자열을 입력하세요 : ").pack(side=LEFT)
e=Entry(frame2,width=20,text="")
e.pack(side=LEFT)

Button(frame2,text="열기",command=fileopen).pack(side=LEFT)
Button(frame2,text="보여주기",command=handle).pack(side=LEFT)

window.mainloop()
