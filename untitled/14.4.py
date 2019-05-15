from tkinter import*
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

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
            histogram[ord(c)-ord('a')]+=1

    text.delete(1.0,END)
    for i in range(26):
        text.insert(END,"{0} - 빈도 수 : {1}\n".format(chr(ord('a')+i),histogram[i]))



window=Tk()
frame1=Frame(window)
frame1.pack()
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=Y)
text=Text(frame1,width=40,height=10,wrap=WORD,yscrollcommand=scrollbar.set)
text.pack()
scrollbar.configure(command=text.yview)

frame2=Frame(window)
frame2.pack()
Label(frame2,text="파일명을 입력하세요 : ").pack(side=LEFT)
e=Entry(frame2,width=20,text="")
e.pack(side=LEFT)

Button(frame2,text="열기",command=fileopen).pack(side=LEFT)
Button(frame2,text="보여주기",command=handle).pack(side=LEFT)

window.mainloop()
# f.close()