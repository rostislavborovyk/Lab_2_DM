from tkinter import *
from random import randint, sample
import networkx as nx
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

def create_relation_S(A, B):
    global M, W
    a = A
    b = B
    relation = []
    for i in range(len(a)):
        x = a.pop()
        for k in range(len(b)):
            y = b.pop()
            if (x in W) and (y in M):
                relation.append((x, y))
                break

    return relation

def nodes_to_graph(relation):
    res = set()
    for i in relation:
        for j in i:
            res.add(j)
    return list(res)


path = r'C:\Users\Ростислав\Desktop\Py progs\Lab_2_DM_\fig.png'
M = {"Володимир", "Віктор", "Кирило", "Вадим", "Михайло", "Петро", "Іван", "Олег"}
W = {"Марія", "Анна", "Анастасія", "Ольга", "Тетяна", "Світлана", "Вікторія", "Оксана"}


def graph(path):
    relation = [('Ольга', 'Іван'), ('Тетяна', 'Світлана'), ('Ольга', 'Петро')]
    G = nx.DiGraph()
    G.add_nodes_from(nodes_to_graph(relation))
    for i in relation:
        G.add_edge(*i)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)
    # plt.show()
    plt.savefig(path)


A = {"Володимир", "Віктор", "Кирило", "Марія", "Анна", "Анастасія", "Ольга"}
B = {"Михайло", "Петро", "Іван", "Світлана", "Вікторія", "Оксана"}

print(create_relation_S(A, B))
