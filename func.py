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





