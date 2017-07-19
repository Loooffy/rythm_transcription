from tkinter import *
from tkinter import ttk

def plot(time_hits):
    root=Tk()
    canvas=Canvas(root,width=1200,height=300,bg='white')
    canvas.grid()
    position=0
    #canvas.create_line(50,200,450,200,fill='black',width=1)
    #canvas.create_line(50,300,450,300,fill='black',width=1)

    for beat in range(119):
        canvas.create_line(10+10*beat,50,10+10*beat,250,fill='black',width=1)
        if beat%4==0:
            canvas.create_line(10+10*beat,50,10+10*beat,250,fill='black',width=2)
        else:
                pass
    for hit in time_hits:
        position +=hit
        canvas.create_line(10+10*position,125,10+10*position,175,fill='blue',width=2)
    root.mainloop()

#canvas.create_oval(225,225,275,275,fill='black')
