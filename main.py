
# Импортируем модуль numpy, sympy, random
import numpy as np
from sympy import *
from random import randint

# Инициализация генератора (seed = 7) для идентичности данных
# задаем граф (graph) 20х20 со значениями 1..50 (след)
# задаем size - размерность графа

size = 5
graph = [[0,  2,  30, 9,  1],
         [4,  0,  47, 7,  7],
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
alpha = 1
beta = 1
e = 1
p = 0.01
Q = 15*size
tau0 = 0.001
m = size
Lmin = 10000.0
ro = 0.01
# ---------------------------------------------------------------

# eta - инициализация матрицы видимости
# tau - инициализация матрицы феромонов
eta = np.zeros((size, size), dtype = float)
tau = np.zeros((size, size), dtype = float)

# Задаем матрицы феромона и видимости
for i in range (0, size):
    for j in range (0, size):
        if ( i != j):
            eta[i][j] = 1/graph[i][j]
            tau[i][j] = tau0
        else:
            tau[i][j] = 0
# ---------------------------------------------------------------

# функция m возвращает случайное число в диапазоне 0..100
def rand_m():
    return randint(0, 101)
# ---------------------------------------------------------------

# функция нахождения вероятности
def P(x):
    p = np.zeros(size, dtype = float)
    print("p =", p)
    sum = 0.0
    for c in range(0, size):
        if (c != x) and (f_list [c] == 0):
            sum += (eta[x][c] ** beta) * (tau[x][c] ** alpha)
    for c in range(0, size):
        if (c != x) and (f_list [c] == 0):
            p[c] = 100*((tau[x][c] ** alpha) * (eta[x][c] ** beta)) / (sum)
    print("p = ", p)
    roulette = rand_m()
    print("roulette =", roulette)
    summa = 0.0
    for c in range(0, size):
        print("p = ", p)
        print("c = ", c)
        print("p[c] = ",p[c])
        summa += p[c]
    print("summa = ", summa)
    sum_p = p[0]
    for c in range(0, size):
        if ( roulette <= sum_p ):
            return c
        sum_p += p[c]
# ---------------------------------------------------------------

# Основной цикл прохода по t
for t in range(t0, tmax):
    for ant in range (0, size):
        L = 0
        path = np.zeros((size, size), dtype = float)
        f_list = np.zeros(size, dtype = int)
        print("path0= ", path)
        print("f_list = ", f_list)
        for i in range(0, size):
            j1 = P(i)
            print("j1 = ", j1)
            path [i][j1] = 1
            f_list [j1] = 1
            L += graph[i][j1]
            print("L = ", L)
        if (L < Lmin):
            Lmin = L
        for i in range(0, size):
            for j in range(0, size):
                if (i != j) and (path [i][j] == 1):
                    tau[i][j] = (1 - p)*tau[i][j] + Q/L
# ---------------------------------------------------------------

print("Lmin = ", Lmin)
print("L = ", L)
print("f_list = ", f_list)
print("graph = ", graph)
print("eta = ", eta)
print("tau = ", tau)
