from tkinter import *
from random import randint, sample
import networkx as nx

U = set()
M = {"Володимир", "Віктор", "Кирило", "Вадим", "Михайло", "Петро", "Іван", "Олег"}
W = {"Марія", "Анна", "Анастасія", "Ольга", "Тетяна", "Світлана", "Вікторія", "Оксана"}
A = set()
B = set()
R = set()
S = set()


def window2():
    s=IntVar()
    global A,B
    win2 = Toplevel(root)
    win2.geometry('600x400')
    ls_box_women = Listbox(win2, width=15, height=12)
    ls_box_women.grid(row=0, column=0,sticky="s")
    for i in list(W):
        ls_box_women.insert(0, i)
    ls_box_men= Listbox(win2, width=15, height=12)
    ls_box_men.grid(row=0, column=2,sticky="s")
    for i in list(M):
        ls_box_men.insert(0, i)
    ls_box_A=Listbox(win2,width=15,height=12)
    ls_box_A.grid(row=0,column=3,sticky="s")
    ls_box_B=Listbox(win2,width=15,height=12)
    ls_box_B.grid(row=0,column=4,sticky="s")
    radio_choose1=Radiobutton(win2,text="В нножину А",variable=s ,value=0)
    radio_choose1.grid(row=0,column=1,sticky="s")
    radio_choose2=Radiobutton(win2,text="В множину В",variable=s ,value=1)
    radio_choose2.grid(row=0,column=1)
    push_button_women=Button(win2,text="Перенести жіноче ім'я")
    push_button_women.grid(row=1,column=0,sticky="s")
    push_button_men = Button(win2, text="Перенести чоловыче ім'я")
    push_button_men.grid(row=1, column=2, sticky="s")


    def take_from_women_box(index, ls_list):
        global A,B
        if s.get() == 0:
            ls_list[1].insert(0, ls_list[0].get(index))
            A.add(ls_list[0].get(index))
        else:
            ls_list[2].insert(0, ls_list[0].get(index))
            B.add(ls_list[0].get(index))

    def take_from_men_box(index, ls_list):
        global A,B
        if s.get()==0:
            ls_list[1].insert(0,ls_list[0].get(index))
            A.add(ls_list[0].get(index))
        else:
            ls_list[2].insert(0, ls_list[0].get(index))
            B.add(ls_list[0].get(index))

    push_button_women.bind("<Button-1>",lambda event: take_from_women_box(ls_box_women.curselection()[0],[ls_box_women,ls_box_A,ls_box_B]))
    push_button_men.bind("<Button-1>", lambda event: take_from_men_box(ls_box_men.curselection()[0],[ls_box_men,ls_box_A,ls_box_B]))





def window3():
    win3 = Toplevel(root)
    win3.geometry('600x400')


def window4():
    win4 = Toplevel(root)
    win4.geometry('600x400')


root = Tk()
# root.geometry('600x400')

l1 = Label(root, text="Моя група: ІО -", font=("Arial", 20))
l1.grid(row=0, sticky="w")
l2 = Label(root, text="Мій номер у групі:", font=("Arial", 20))
l2.grid(row=1, sticky="w")
l3 = Label(root, text="Мій варіант:", font=("Arial", 20))
l3.grid(row=2, sticky="W")


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

U = set()
M = {"Володимир", "Віктор", "Кирило", "Вадим", "Михайло", "Петро", "Іван", "Олег"}
W = {"Марія", "Анна", "Анастасія", "Ольга", "Тетяна", "Світлана", "Вікторія", "Оксана"}
A = set()
B = set()
R = set()
S = set()
s=0


def universal(a, b):
    a = list(a)
    b = list(b)
    k = 0
    global U
    while k <= 1:
        if k == 1:
            z = a
            a = b
            b = z
        for i in a:
            for j in b:
                U.add((i, j))
        k += 1
    return U


def take_from_women_box(index, ls_list):
    global s
    if s==0:
        ls_list[1].insert(0,ls_list[0].get(index))
    else:
        ls_list[2].insert(0,ls_list[0].get(index))





