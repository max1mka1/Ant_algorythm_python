
# Импортируем модуль numpy, sympy, random
import numpy as np
from sympy import *
from random import randint

# Инициализация генератора (seed = 7) для идентичности данных
# задаем граф (graph) 20х20 со значениями 1..50 (след)
# задаем size - размерность графа

size = 5
graph = [[0,  2,  30, 9,  1],[4,  0,  47, 7,  7],
                  [31, 33, 0,  33, 36],
                  [20, 13, 16, 0,  28],
                  [9,  36, 22, 22, 0]]
# size = 5
# np.random.seed = 7
# graph = np.random.randint(1, 50, size = (size, size))
# ---------------------------------------------------------------
# Инициализация параметров алгоритма:
# t0 - задаем начало отсчета времени
# tmax - задаем начало отсчета времени
# α (alpha),  β (beta) - два регулируемых параметра,
# задающие веса следа феромона (жадность) и видимости при выборе маршрута (стадность);
# e - количество элитных муравьев;
# p - параметр, отвечающий за высыхание феромона;
# Q - параметр порядка длины оптимального маршрута;
# τ (tau0) - начальное количество феромона;
# m -  количество муравьев (задаем равным количеству городов size*size);
# Lmin - начальное значение минимума длины оптимального маршрута;
# ro  - коэффициент испарения феромона;

t0 = 1
tmax = 100
alpha = 9
beta = 5
e = 1
p = 0.7
Q = 15*size
tau0 = 0.1
m = size*size
Lmin = 10000
ro = 0.001

# ---------------------------------------------------------------

# eta - инициализация матрицы видимости
#eta = np.zeros((size, size))
eta = [[0,  0,  0, 0,  0],[0,  0,  0, 0,  0],
                  [0, 0, 0,  0, 0],
                  [0, 0, 0, 0,  0],
                  [0,  0, 0, 0, 0]]
# tau - инициализация матрицы феромонов
#tau = np.zeros((size, size))
tau = [[0,  0,  0, 0,  0],[0,  0,  0, 0,  0],
                  [0, 0, 0,  0, 0],
                  [0, 0, 0, 0,  0],
                  [0,  0, 0, 0, 0]]
# Задаем начальное ненулевое значение феромона на всех ребрах графа,
# а также задаем матрицу видимости
for i in range (0, size):
    for j in range (0, size):
        if ( i != j):
            eta[i][j] = 1/graph[i][j]
            tau[i][j] = tau0
        else:
            tau[i][j] = 0

print(graph)
print(eta)
print(tau)

# ---------------------------------------------------------------

# функция m возвращает случайное число в диапазоне 0..100
def m():
    return randint(1, 101)

# функция нахождения вероятности
def P(x):
    #p = np.zeros(size, dtype = float)
    p = [0, 0, 0, 0, 0]
    print(p)
    sum = 0
    for c in range(0, size):
        if (c != x) and (f_list[x][c] == 0):
            sum += (eta[x][c] ** beta) * (tau[x][c] ** alpha)
    for c in range(0, size):
        if (c != x) and (f_list[x][c] == 0):
            p[c] = 100*((tau[x][c] ** alpha) * (eta[x][c] ** beta)) / (sum)
    print(p)
    roulette = m()
    print(roulette)
    summa = 0
    for c in range(0, size):
        print("p[c] = ")
        print(c)
        print(p[c])
        summa += p[c]
    print("summa = ")
    print(summa)
    sum_p = p[0]
    for c in range(0, size-1):
        if ( roulette <= sum_p ):
            return c
        sum_p += p[c]

L = 0
a = 0
# Основной цикл прохода по t
for t in range(t0, tmax):
    for ant in range (0, 2*size):
        ant %= size
        L = 0
        #path = np.zeros((size, size), dtype=int)
        path = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        #f_list = np.zeros((size, size), dtype=int)
        f_list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        print(path)
        print(f_list)
        for i in range(0, size):
            #i = i % size
            j1 = P(i)
            print("j1 = ")
            print(j1)
            path [i][j1] = 1
            f_list [i][j1] = 1
            a = graph[i][j1]
            print(a)
            L += a
            print("L = ")
            print(L)
        if (L < Lmin):
            Lmin = L
        for i in range(0, size):
            for j in range(0, size):
                if (i != j) and (path [i][j1] == 1):
                    tau[i][j1] = (1 - p)*tau[i][j1] + Q/L


print("Lmin = ")
print(Lmin)
print(L)
print(f_list)
print(graph)
print(eta)
print(tau)
