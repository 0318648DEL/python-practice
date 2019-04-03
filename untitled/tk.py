from tkinter import *

x=10
y=10
def common(index):
    global x,y
    if index==0:
        if (0< x < 300 and 0 < y-5 < 205):
            y -= 5
            canvas.delete("ball")
            canvas.create_oval(x, y, x + 10, y + 10, fill='red', tags='ball')
    elif index==1:
        if (0 < x < 300 and 0 < y+5 < 195):
            y += 5
            canvas.delete("ball")
            canvas.create_oval(x, y, x + 10, y + 10, fill='red', tags='ball')
    elif index==2:
        if (0 < x-5 < 305 and 0 < y < 200):
            x -= 5
            canvas.delete("ball")
            canvas.create_oval(x, y, x + 10, y + 10, fill='red', tags='ball')
    else:
        if (0< x+5 < 295 and 0< y < 200):
            x += 5
            canvas.delete("ball")
            canvas.create_oval(x, y, x + 10, y + 10, fill='red', tags='ball')

window = Tk()
canvas=Canvas(window,width=300,height=200,bg='white')
canvas.pack()
canvas.create_oval(10,10,20,20,fill='red',tags='ball')
frame=Frame(window)
frame.pack()
for i in range(4):
    Button(frame,text=str(i),command=lambda index=i : common(index)).pack(side=LEFT)
window.mainloop()