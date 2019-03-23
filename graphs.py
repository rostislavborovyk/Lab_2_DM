from tkinter import *
from random import randint, sample
import networkx as nx
import matplotlib.pyplot as plt
from PIL import ImageTk, Image


def nodes_to_graph(relation):
    res = set()
    for i in relation:
        for j in i:
            res.add(j)
    return list(res)


path = r'C:\Users\Ростислав\PycharmProjects\Lab_2_DM\fig.png'


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
    img = ImageTk.PhotoImage(path)
    return img
