from tkinter import *
from random import randint, sample
import networkx as nx
import func as f



def window2():
    win2 = Toplevel(root)
    win2.geometry('600x400')
    ls_box_women = Listbox(win2, width=15, height=12)
    ls_box_women.grid(row=0, column=0,sticky="s")
    for i in list(f.W):
        ls_box_women.insert(0, i)
    ls_box_men= Listbox(win2, width=15, height=12)
    ls_box_men.grid(row=0, column=3,sticky="s")
    for i in list(f.M):
        ls_box_men.insert(0, i)
    radio_choose1=RADIOBUTTON(win2,text="В нножину А",variable=f.s,value=f.s)
    radio_choose.grid(row=0,column=1)



def window3():
    win3 = Toplevel(root)
    win3.geometry('600x400')


def window4():
    win4 = Toplevel(root)
    win4.geometry('600x400')


root = Tk()
# root.geometry('600x400')

l1 = Label(root, text="Моя група: ІО -", font=("Arial", 20))
l1.grid(row=0, sticky=W)
l2 = Label(root, text="Мій номер у групі:", font=("Arial", 20))
l2.grid(row=1, sticky=W)
l3 = Label(root, text="Мій варіант:", font=("Arial", 20))
l3.grid(row=2, sticky=W)


mainMenu = Menu(root)
root.config(menu=mainMenu)

win2 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=win2, label='Вікно 2')
win2.add_command(label='Відкрити', command=window2)

win3 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=win3, label='Вікно 3')
win3.add_command(label='Відкрити', command=window3)

win4 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=win4, label='Вікно 4')
win4.add_command(label='Відкрити', command=window4)

root.mainloop()
