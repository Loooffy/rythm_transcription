from tkinter import *
from tkinter import ttk
import time

def plot_the_notes(rhythm_raw):

    root=Tk()
    canvas=Canvas(root,width=1000,height=500,bg='white')
    canvas.grid()

    notePos=1 #note的順位
    seq_notePos=[] #紀錄note順位的陣列

    noteLocation=0 #note的位置
    seq_noteLoc=[] #紀錄note位置的陣列

    seq_trunkLoc=[] #trunk的位置

    barPos=0 #初始化bar的順位為0
    seq_barLoc=[] #紀錄bar位置的陣列

    d_note=20; d_bar=20
    x0=10; y0=100

    for trunkPos in range(sum(rhythm_raw)):
        seq_trunkLoc.append((trunkPos+1)*d_note+trunkPos//4*d_bar) #nd+(n/4)D
        #依序將trunk的位置存到seq_trunkPos
        #int(a/b) 改成 a//b

    for barPos in range((sum(rhythm_raw)//4)+1): #sum(rhythm_raw/4)為小節數
        seq_barLoc.append(barPos*(4*d_note+d_bar))

    for span in rhythm_raw:
        notePos=notePos+span
        seq_notePos.append(notePos-1)
        #依序將note的順位存到seq_notePos

    for notePos in seq_notePos:
        noteLocation=(notePos)*d_note+((notePos-1)//4)*d_bar #nd+(n/4)D
        seq_noteLoc.append(noteLocation)
        #依序將note的位置存到seq_notePos

    for noteLoc in seq_noteLoc:
        plot_note(canvas,x0+noteLoc,y0)
    for trunkLoc in seq_trunkLoc:
        plot_trunk(canvas,x0+trunkLoc,y0)
    for barLoc in seq_barLoc:
        plot_bar(canvas,x0+barLoc,y0)
    #印出音符和音符桿

    print("notes: ",seq_notePos)

    root.mainloop()

def plot_note(canvas,x,y):
    canvas.create_oval(x-5,y-4,x+5,y+4,fill='black')
def plot_trunk(canvas,x,y):
    canvas.create_line(x+5,y-20,x+5,y,fill='black')
def plot_bar(canvas,x,y):
    canvas.create_line(x,y-25,x,y+10,fill='blue',width=3)
