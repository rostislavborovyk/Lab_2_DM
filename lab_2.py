from tkinter import *
from random import randint, sample
import networkx as nx
import matplotlib.pyplot as plt
from PIL import ImageTk, Image




temp_relation = [('Ольга', 'Іван'), ('Тетяна', 'Світлана'), ('Ольга', 'Петро')]
U = set()
M = {"Володимир", "Віктор", "Кирило", "Вадим", "Михайло", "Петро", "Іван", "Олег"}
W = {"Марія", "Анна", "Анастасія", "Ольга", "Тетяна", "Світлана", "Вікторія", "Оксана"}
A = set()
B = set()
R = set()
S = set()


# --------------------------Functions----------------------------------

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
    if s == 0:
        ls_list[1].insert(0, ls_list[0].get(index))
    else:
        ls_list[2].insert(0, ls_list[0].get(index))


def create_relation_S(A, B):
    global M, W, S
    a = A.copy()
    b = B.copy()
    relation = []
    for i in range(len(a)):
        x = a.pop()
        done = False
        for k in range(len(b)):
            if done:
                continue
            y = b.pop()
            if (x in W) and (y in M):
                relation.append((x, y))
                done = True
    S = relation
    return relation


def create_relation_R(A, B):
    global M, W, S, R
    a = set()
    for i in S:
        a.add(S[0])
        a.add(S[1])
    a = set(A) - a
    b = B.copy()
    relation = []

    res = []

    for i in range(len(a)):
        x = a.pop()
        done = False
        for k in range(len(b)):
            if done:
                continue
            y = b.pop()

            if (x in W) and (y in M):
                relation.append((x, y))
                done = True
    R = relation
    return relation


def nodes_to_graph(relation):
    res = set()
    for i in relation:
        for j in i:
            res.add(j)
    return list(res)


def create_graph(name_of_set: str):
    global S, R, A, B
    relation = 0
    path = 0
    if name_of_set.lower() == 's':
        relation = create_relation_S(A, B)
        path = 's_fig.png'
        GG = nx.DiGraph()
        GG.add_nodes_from(nodes_to_graph(relation))
        for i in relation:
            GG.add_edge(*i)
        pos = nx.circular_layout(GG)
        nx.draw(GG, pos, with_labels=True)
        # plt.show()
        plt.savefig(path)

    if name_of_set.lower() == 'r':
        relation = create_relation_R(A, B)
        path = 'r_fig.png'
        G = nx.DiGraph()
        G.add_nodes_from(nodes_to_graph(relation))
        for i in relation:
            G.add_edge(*i)
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True)
        # plt.show()
        plt.savefig(path)
        plt.close()


# ---------------------windows----------------------
def window2():
    s = IntVar()
    global A, B
    win2 = Toplevel(root)
    win2.geometry('600x400')
    women_label = Label(win2, text="Список жінок")
    women_label.grid(row=0, column=0, sticky="s")
    ls_box_women = Listbox(win2, width=15, height=12)
    ls_box_women.grid(row=1, column=0, sticky="s")
    for i in list(W):
        ls_box_women.insert(0, i)
    men_label = Label(win2, text="Список чоловіків")
    men_label.grid(row=0, column=1, sticky="s")
    ls_box_men = Listbox(win2, width=15, height=12)
    ls_box_men.grid(row=1, column=1, sticky="s")
    for i in list(M):
        ls_box_men.insert(0, i)
    A_label = Label(win2, text="Множина А")
    A_label.grid(row=0, column=3, sticky="s")
    ls_box_A = Listbox(win2, width=15, height=12)
    ls_box_A.grid(row=1, column=3, sticky="s")
    ls_box_B = Listbox(win2, width=15, height=12)
    ls_box_B.grid(row=1, column=4, sticky="s")
    B_label = Label(win2, text="Множина B")
    B_label.grid(row=0, column=4, sticky="s")
    radio_choose1 = Radiobutton(win2, text="В нножину А", variable=s, value=0)
    radio_choose1.grid(row=0, column=2, rowspan=2)
    radio_choose2 = Radiobutton(win2, text="В множину В", variable=s, value=1)
    radio_choose2.grid(row=0, column=2, rowspan=2, sticky="s")
    push_button_women = Button(win2, text="Перенести жіноче ім'я")
    push_button_women.grid(row=1, column=0, sticky="s")
    push_button_men = Button(win2, text="Перенести чоловыче ім'я")
    push_button_men.grid(row=1, column=1, sticky="s")

    def take_from_women_box(index, ls_list):
        global A, B
        if s.get() == 0:
            ls_list[1].insert(0, ls_list[0].get(index))
            A.add(ls_list[0].get(index))
        else:
            ls_list[2].insert(0, ls_list[0].get(index))
            B.add(ls_list[0].get(index))

    def take_from_men_box(index, ls_list):
        global A, B
        if s.get() == 0:
            ls_list[1].insert(0, ls_list[0].get(index))
            A.add(ls_list[0].get(index))
        else:
            ls_list[2].insert(0, ls_list[0].get(index))
            B.add(ls_list[0].get(index))

    push_button_women.bind("<Button-1>", lambda event: take_from_women_box(ls_box_women.curselection()[0],
                                                                           [ls_box_women, ls_box_A, ls_box_B]))
    push_button_men.bind("<Button-1>", lambda event: take_from_men_box(ls_box_men.curselection()[0],
                                                                       [ls_box_men, ls_box_A, ls_box_B]))


def window3():
    global IMAGE_GRAPH_S
    global IMAGE_GRAPH_R
    create_graph('s')
    create_graph('r')
    Image_graph_S()
    Image_graph_R()
    global A, B, S, R
    win3 = Toplevel(root)
    win3.geometry('1000x500')
    lbl_A = Label(win3, text='Множина А')
    lbl_A.grid(row=0, column=0)
    lbl_B = Label(win3, text='Множина B')
    lbl_B.grid(row=0, column=1)
    show_A = Listbox(win3)
    for i in A:
        show_A.insert(END, i)
    show_A.grid(row=1, column=0)
    show_B = Listbox(win3)
    for i in B:
        show_B.insert(END, i)
    show_B.grid(row=1, column=1)
    graph_lbl1 = Label(win3)
    graph_lbl1.grid(row=0, column=3, rowspan=4)
    graph_lbl = Label(win3)
    graph_lbl.grid(row=1, column=4, rowspan=4)
    calc_S_btn = Button(win3, text='Обрахувати відношення S')
    calc_S_btn.grid(row=2, column=0)
    calc_S_btn.bind("<Button-1>", lambda event: graph_lbl1.configure(image=IMAGE_GRAPH_S))
    calc_R_btn = Button(win3, text='Обрахувати відношення R')
    calc_R_btn.grid(row=2, column=1)
    calc_R_btn.bind("<Button-1>", lambda event: graph_lbl.configure(image=IMAGE_GRAPH_R))


def window4():
    win4 = Toplevel(root)
    # win4.geometry('600x400')



root = Tk()
# root.geometry('600x400')
IMAGE_GRAPH_S = None
IMAGE_GRAPH_R = None


def Image_graph_S():
    global IMAGE_GRAPH_S
    image = Image.open('s_fig.png')
    photo = ImageTk.PhotoImage(image)
    IMAGE_GRAPH_S = photo


def Image_graph_R():
    global IMAGE_GRAPH_R
    image = Image.open(r'r_fig.png')
    photo = ImageTk.PhotoImage(image)
    IMAGE_GRAPH_R = photo


group_lbl = Label(root, text="Моя група: ", font=("Arial", 20))
group_lbl.grid(row=0, column=0, sticky="w")
group_lbl_show = Label(root, text='ІВ-82', font=('Arial', 20))
group_lbl_show.grid(row=0, column=1, sticky='e')
number_lbl = Label(root, text="Мій номер у групі: ", font=("Arial", 20))
number_lbl.grid(row=1, column=0, sticky="w")
number_lbl_show = Label(root, text="3", font=("Arial", 20))
number_lbl_show.grid(row=1, column=1, sticky="e")
var_lbl = Label(root, text="Мій варіант: ", font=("Arial", 20))
var_lbl.grid(row=2, column=0, sticky="W")
var_lbl_show = Label(root, text="26", font=("Arial", 20))
var_lbl_show.grid(row=2, column=1, sticky="e")

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
