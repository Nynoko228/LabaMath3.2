import matplotlib.pyplot as plt #для графиков
from pylab import mpl
import math
# import numpy
from Form import Application
from threading import Thread
# Аппроксимация полиномиальной кривой с одной переменной


import tkinter as tk #для интерфейса

def Lagrandj(Xisc):
    global x, y
    Yisc = 0.0
    Sum = 0.0
    k = 12
    # k = 6
    for i in range(k):
        Proiz = y[i]
        for j in range(k):
            if (j != i):
                Proiz *= ((Xisc-x[j])/(x[i]-x[j]))
        Sum += Proiz
        Proiz = 0
    Yisc = Sum
    return Yisc

def Test():
    global x, y
    k = 12
    # k = 6
    h = float(x[1]-x[0])

    Yi = [] # Пятые производные
    Yi.append(1/(12*round(h,2))*(-3*round(Lagrandj(x[4]),2)+16*round(Lagrandj(x[3]),2)-36*round(Lagrandj(x[2]),2)+48*round(Lagrandj(x[1]),2)-25*round(Lagrandj(x[0]),2)))
    h = float(x[1]-x[0])
    Yi.append(1/(12*round(h,2))*(-3*round(Lagrandj(x[5]),2)+16*round(Lagrandj(x[3]),2)-36*round(Lagrandj(x[3]),2)+48*round(Lagrandj(x[2]),2)-25*round(Lagrandj(x[1]),2)))

    for i in range(2, k-2):
        h = (x[i + 2] - x[i - 2]) / 4
        Yi.append((round(Lagrandj(x[i-2]),2) - 8 * round(Lagrandj(x[i-1]),2) + 8 * round(Lagrandj(x[i+1]),2) - round(Lagrandj(x[i+2]),2)) / (12 * h))

    # h = (x[-2] - x[-6]) / 4
    h = x[-2] - x[-3]
    Yi.append(1 / (12 * round(h,2)) * (3 * round(Lagrandj(x[-6]),2) - 16 * round(Lagrandj(x[-5]),2) + 36 * round(Lagrandj(x[-4]),2) - 48 * round(Lagrandj(x[-3]),2) + 25 * round(Lagrandj(x[-2]),2)))
    # h = (x[-1] - x[-5]) / 4
    h = x[-1] - x[-2]
    Yi.append(1 / (12 * round(h,2)) * (3 * round(Lagrandj(x[-5]),2) - 16 * round(Lagrandj(x[-4]),2) + 36 * round(Lagrandj(x[-3]),2) - 48 * round(Lagrandj(x[-2]),2) + 25 * round(Lagrandj(x[-1]),2)))

    Yj = [] # Третьи производные
    h = x[1] - x[0]
    Yj.append(1/(2*round(h,2))*(-round(Lagrandj(x[2]),2)+4*round(Lagrandj(x[1]),2)-3*round(Lagrandj(x[0]),2)))

    for i in range(1, k-1):
        h = (x[i + 1] - x[i - 1]) / 2
        Yj.append((1/(2 * h)) * (-round(Lagrandj(x[i-1]),2)+round(Lagrandj(x[i+1]),2)))

    # h = (x[-1] - x[-3])/ 2
    h = x[-1] - x[-2]
    Yj.append(1/(2*round(h,2))*(round(Lagrandj(x[-3]),2)-4*round(Lagrandj(x[-2]),2)+3*round(Lagrandj(x[-1]),2)))
    draw(x, y, Yj, Yi)
    # thread.start()
def formula():
    global x, y
    fin = []
    k = 12
    # k = 6
    h = float(x[1]-x[0])
    Yi = [] # Пятые производные
    fin += [rf"Пятые производные: "]
    fin += [r"Левые: $y_{0}^'=\frac{{-3y_{4}+16y_{3}-36y_{2}+48y_{1}-25y_{0}}}{{12h}}$"]
    fin += [r"Левые: $y_{1}^'=\frac{{-3y_{5}+16y_{4}-36y_{3}+48y_{2}-25y_{1}}}{{12h}}$"]
    fin += [rf"$y_{0}^'=\frac{{-3({round(Lagrandj(x[4]),2)})+16({round(Lagrandj(x[3]),2)})-36({round(Lagrandj(x[2]),2)})+48({round(Lagrandj(x[1]),2)})-25({round(Lagrandj(x[0]),2)})}}{{12({(round(h,2))})}}$"]
    Yi.append(1/(12*h)*(0-3*Lagrandj(x[0]+4*h)+16*Lagrandj(x[0]+3*h)-36*Lagrandj(x[0]+2*h)+48*Lagrandj(x[0]+1*h)-25*Lagrandj(x[0])))
    h = float(x[1]-x[0])
    fin += [rf"$y_{1}^'=\frac{{-3({round(Lagrandj(x[5]),2)})+16({round(Lagrandj(x[4]),2)})-36({round(Lagrandj(x[3]),2)})+48({round(Lagrandj(x[2]),2)})-25({round(Lagrandj(x[1]),2)})}}{{12({round(h,2)})}}$"]
    Yi.append(1/(12*h)*(0-3*Lagrandj(x[1]+4*h)+16*Lagrandj(x[1]+3*h)-36*Lagrandj(x[1]+2*h)+48*Lagrandj(x[1]+1*h)-25*Lagrandj(x[1])))
    fin += [r"Центральные: $y_{2..n-3}^'=\frac{{y_{-2}-8y_{-1}+8y_{1}-y_{2}}}{{12h}}$"]
    for i in  range(2, k-2):
        h = (x[i + 2] - x[i - 2]) / 4
        fin += [rf"$y_{i}^'=\frac{{({round(Lagrandj(x[i-2]), 2)})-8({round(Lagrandj(x[i-1]), 2)})+8({round(Lagrandj(x[i+1]), 2)})-({round(Lagrandj(x[i+2]), 2)})}}{{12({round(h, 2)})}}$"]
        Yi.append((-Lagrandj(x[i] - 2 * h) - 8 * Lagrandj(x[i] - 1 * h) + 8 * Lagrandj(x[i] + 1 * h) + Lagrandj(x[i] + 2 * h)) / (12 * h))

    h = (x[k - 2] - x[k - 6]) / 4
    fin += [r"Правые: $y_{n-2}^'=\frac{{3y_{n-6}-16y_{n-5}+36y_{n-4}-48y_{n-3}+25y_{n-2}}}{{12h}}$"]
    fin += [rf"$y_{{{10}}}^'=\frac{{3({round(Lagrandj(x[-6]),2)})-16({round(Lagrandj(x[-5]),2)})+36({round(Lagrandj(x[-4]),2)})-48({round(Lagrandj(x[-3]),2)})+25({round(Lagrandj(x[-2]),2)})}}{{12({(round(h,2))})}}$"]
    Yi.append(1 / (12 * h) * (3 * Lagrandj(x[k - 2] - 4 * h) - 16 * Lagrandj(x[k - 2] - 3 * h) + 36 * Lagrandj(x[k - 2] - 2 * h) - 48 * Lagrandj(x[k - 2] - 1 * h) + 25 * Lagrandj(x[k - 2])))
    h = (x[k - 1] - x[k - 5]) / 4
    fin += [r"Правые: $y_{n-1}^'=\frac{{3y_{n-5}-16y_{n-4}+36y_{n-3}-48y_{n-2}+25y_{n-1}}}{{12h}}$"]
    fin += [rf"$y_{{{11}}}^'=\frac{{3({round(Lagrandj(x[-5]),2)})-16({round(Lagrandj(x[-4]),2)})+36({round(Lagrandj(x[-3]),2)})-48({round(Lagrandj(x[-2]),2)})+25({round(Lagrandj(x[-1]),2)})}}{{12({(round(h,2))})}}$"]
    Yi.append(1 / (12 * h) * (3 * Lagrandj(x[k - 1] - 4 * h) - 16 * Lagrandj(x[k - 1] - 3 * h) + 36 * Lagrandj(x[k - 1] - 2 * h) - 48 * Lagrandj(x[k - 1] - 1 * h) + 25 * Lagrandj(x[k - 1])))

    Yj = [] # Третьи производные

    h = x[1] - x[0]
    fin += [r"Левые: $y_{0}^'=\frac{{-y_{2}+4y_{1}-3y_{0}}}{{12h}}$"]
    Yj.append(1/(2*(x[1]-x[0]))*(-Lagrandj(x[0]+2*h)+4*Lagrandj(x[0]+1*h)-3*Lagrandj(x[0])))
    fin += [rf"$y_{0}^'=\frac{{-({round(Lagrandj(x[2]),2)})+4({round(Lagrandj(x[1]),2)})-3({round(Lagrandj(x[0]),2)})}}{{2({(round(h,2))})}}$"]
    fin += [r"Центральные: $y_{1..n-2}^'=\frac{-{y_{-1}+y_{1}}}{{12h}}$"]
    for i in range(1, k-1):
        h = (x[i + 1] - x[i - 1]) / 2
        fin += [rf"$y_{{{i}}}^'=\frac{{-({round(Lagrandj(x[i-1]), 2)})+({round(Lagrandj(x[i+1]), 2)})}}{{2({(round(h, 2))})}}$"]
        Yj.append(1/((x[i+1]-x[i-1]))*(-Lagrandj(x[i]-1*h)+Lagrandj(x[i]+1*h)))

    h = x[k - 1] - x[k - 2]
    fin += [r"Правые: $y_{n-1}^'=\frac{{y_{-2}-4y_{-1}+3y_{0}}}{{12h}}$"]
    fin += [rf"$y_{{{11}}}^'=\frac{{({round(Lagrandj(x[-3]), 2)})-4({round(Lagrandj(x[-2]), 2)})+3({round(Lagrandj(x[-1]), 2)})}}{{2({(round(h, 2))})}}$"]
    Yj.append(1/((x[k-1]-x[k-3]))*(Lagrandj(x[k-1]-2*h)-4*Lagrandj(x[k-1]-1*h)+3*Lagrandj(x[k-1])))

    root = tk.Toplevel()
    app = Application(fin, master=root)
    app.mainloop()

# Функция draw рисует наши кривые на координатной плоскости
def draw(xL, yL, y3, y5):
    thread = Thread(target=lambda: formula())
    thread.start()
    print(len(xL), len(yL), len(y3), len(y5))
    plt.plot(xL, y3, label="график по 3-им разностям")
    # plt.scatter(xL, y5, label="табличные данные")
    plt.plot(xL, y5, label="график по 5-ым разностям")
    plt.legend(loc="upper right")
    plt.show()


x = [0.00, 5.01, 10.09, 13.98, 16.62, 18.01, 22.53, 25.33, 28.03, 30.42, 32.06, 33.62]
y = [0.00, 0.18, 1.05, 1.73, 2.35, 2.96, 3.76, 4.48, 5.28, 6.12, 7.09, 8.00]
fin = []
Test()
