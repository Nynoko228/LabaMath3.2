import matplotlib.pyplot as plt #для графиков
from pylab import mpl
import math
# import numpy
from Form import Application
from threading import Thread
# Аппроксимация полиномиальной кривой с одной переменной


import tkinter as tk #для интерфейса

# Функция Lagrandj высчитывает значение для 5ых разностей
def Lagrandj(Xisc, x, y):
    Yisc1 = (4*pow(Xisc, 3)-3*x[1]*pow(Xisc, 2)-3*x[2]*pow(Xisc, 2)-3*x[3]*pow(Xisc, 2)-3*x[4]*pow(Xisc, 2)+2*x[1]*x[2]*Xisc+2*x[1]*x[3]*Xisc+2*x[1]*x[4]*Xisc+2*x[2]*x[3]*Xisc+2*x[2]*x[4]*Xisc+2*x[3]*x[4]*Xisc-x[1]*x[2]*x[3]-x[1]*x[2]*x[4]-x[1]*x[3]*x[4]-x[2]*x[3]*x[4])*y[0]/(((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3])*(x[0]-x[4])))
    # Yisc1 *= y[0]
    # Yisc1 /= ((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3])*(x[0]-x[4]))
    Yisc2 = (4*pow(Xisc, 3)-3*x[0]*pow(Xisc, 2)-3*x[2]*pow(Xisc, 2)-3*x[3]*pow(Xisc, 2)-3*x[4]*pow(Xisc, 2)+2*x[0]*x[2]*Xisc+2*x[0]*x[3]*Xisc+2*x[0]*x[4]*Xisc+2*x[2]*x[3]*Xisc+2*x[2]*x[4]*Xisc+2*x[3]*x[4]*Xisc-x[0]*x[2]*x[3]-x[0]*x[2]*x[4]-x[0]*x[3]*x[4]-x[2]*x[3]*x[4])*y[1]/(((x[1]-x[0])*(x[1]-x[2])*(x[1]-x[3])*(x[1]-x[4])))
    # Yisc2 *= y[1]
    # Yisc2 /= ((x[1]-x[0])*(x[1]-x[2])*(x[1]-x[3])*(x[1]-x[4]))
    Yisc3 = (4*pow(Xisc, 3)-3*x[0]*pow(Xisc, 2)-3*x[1]*pow(Xisc, 2)-3*x[3]*pow(Xisc, 2)-3*x[4]*pow(Xisc, 2)+2*x[0]*x[1]*Xisc+2*x[0]*x[3]*Xisc+2*x[0]*x[4]*Xisc+2*x[1]*x[3]*Xisc+2*x[1]*x[4]*Xisc+2*x[3]*x[4]*Xisc-x[0]*x[1]*x[3]-x[0]*x[1]*x[4]-x[0]*x[3]*x[4]-x[1]*x[3]*x[4])*y[2]/(((x[2]-x[0])*(x[2]-x[1])*(x[2]-x[3])*(x[2]-x[4])))
    # Yisc3 *= y[2]
    # Yisc3 /= ((x[2]-x[0])*(x[2]-x[1])*(x[2]-x[3])*(x[2]-x[4]))
    Yisc4 = (4*pow(Xisc, 3)-3*x[0]*pow(Xisc, 2)-3*x[1]*pow(Xisc, 2)-3*x[2]*pow(Xisc, 2)-3*x[4]*pow(Xisc, 2)+2*x[0]*x[1]*Xisc+2*x[0]*x[2]*Xisc+2*x[0]*x[4]*Xisc+2*x[1]*x[2]*Xisc+2*x[1]*x[4]*Xisc+2*x[2]*x[4]*Xisc-x[0]*x[1]*x[2]-x[0]*x[1]*x[4]-x[0]*x[2]*x[4]-x[1]*x[2]*x[4])*y[3]/(((x[3]-x[0])*(x[3]-x[1])*(x[3]-x[2])*(x[3]-x[4])))
    # Yisc4 *= y[3]
    # Yisc4 /= ((x[3]-x[0])*(x[3]-x[1])*(x[3]-x[2])*(x[3]-x[4]))
    Yisc5 = (4*pow(Xisc, 3)-3*x[0]*pow(Xisc, 2)-3*x[1]*pow(Xisc, 2)-3*x[2]*pow(Xisc, 2)-3*x[3]*pow(Xisc, 2)+2*x[0]*x[1]*Xisc+2*x[0]*x[2]*Xisc+2*x[0]*x[3]*Xisc+2*x[1]*x[2]*Xisc+2*x[1]*x[3]*Xisc+2*x[2]*x[3]*Xisc-x[0]*x[1]*x[2]-x[0]*x[1]*x[3]-x[0]*x[2]*x[3]-x[1]*x[2]*x[3])*y[4]/(((x[4]-x[0])*(x[4]-x[1])*(x[4]-x[2])*(x[4]-x[3])))
    # Yisc5 *= y[4]
    # Yisc5 /= ((x[4]-x[0])*(x[4]-x[1])*(x[4]-x[2])*(x[4]-x[3]))
    Yisc = Yisc1+Yisc2+Yisc3+Yisc4+Yisc5
    return Yisc

def Lagrandje(Xisc):
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
# Функция Test высчитывает 3и и 5е разности
def Test(x, y):
    k = 12
    h = float(x[1]-x[0])

    Yi = [] # Пятые разности
    Yi.append(1/(12*round(h,2))*(-3*round(Lagrandje(x[4]),2)+16*round(Lagrandje(x[3]),2)-36*round(Lagrandje(x[2]),2)+48*round(Lagrandje(x[1]),2)-25*round(Lagrandje(x[0]),2)))
    h = float(x[2]-x[1])
    Yi.append(1/(12*round(h,2))*(-3*round(Lagrandje(x[5]),2)+16*round(Lagrandje(x[3]),2)-36*round(Lagrandje(x[3]),2)+48*round(Lagrandje(x[2]),2)-25*round(Lagrandje(x[1]),2)))

    for i in range(2, k-2):
        h = (x[i + 2] - x[i - 2]) / 4
        Yi.append((round(Lagrandje(x[i-2]),2) - 8 * round(Lagrandje(x[i-1]),2) + 8 * round(Lagrandje(x[i+1]),2) - round(Lagrandje(x[i+2]),2)) / (12 * h))

    # h = (x[-2] - x[-6]) / 4
    h = x[-2] - x[-3]
    Yi.append(1 / (12 * round(h,2)) * (3 * round(Lagrandje(x[-6]),2) - 16 * round(Lagrandje(x[-5]),2) + 36 * round(Lagrandje(x[-4]),2) - 48 * round(Lagrandje(x[-3]),2) + 25 * round(Lagrandje(x[-2]),2)))
    # h = (x[-1] - x[-5]) / 4
    h = x[-1] - x[-2]
    Yi.append(1 / (12 * round(h,2)) * (3 * round(Lagrandje(x[-5]),2) - 16 * round(Lagrandje(x[-4]),2) + 36 * round(Lagrandje(x[-3]),2) - 48 * round(Lagrandje(x[-2]),2) + 25 * round(Lagrandje(x[-1]),2)))

    # for i in range(len(x)):
    #     Yi.append(Lagrandj(x[i], x, y))

    Yj = [] # Третьи разности
    h = x[1] - x[0]
    Yj.append(1/(2*round(h,2))*(-round(Lagrandje(x[2]),2)+4*round(Lagrandje(x[1]),2)-3*round(Lagrandje(x[0]),2)))

    for i in range(1, k-1):
        h = (x[i + 1] - x[i - 1]) / 2
        Yj.append((1/(2 * h)) * (-round(Lagrandje(x[i-1]),2)+round(Lagrandje(x[i+1]),2)))

    # h = (x[-1] - x[-3])/ 2
    h = x[-1] - x[-2]
    Yj.append(1/(2*round(h,2))*(round(Lagrandje(x[-3]),2)-4*round(Lagrandje(x[-2]),2)+3*round(Lagrandje(x[-1]),2)))

    # for i in range(len(x)):
    #     Yj.append(((2*x[i]-x[1]-x[2])*y[0]/((x[0]-x[1])*(x[0]-x[2])))+((2*x[i]-x[0]-x[2])*y[1]/((x[1]-x[0])*(x[1]-x[2])))+((2*x[i]-x[0]-x[1])*y[2]/((x[2]-x[0])*(x[2]-x[1]))))
        # Yj.append(Lagrandj(x[i], x, y))

    draw(x, y, Yj, Yi)

# Функция formula формирует TeX код формул
def formula(x, y):
    fin = []
    fin += ["Пятые разности: "]
    fin += [r"$P^{'}(x)=\frac{(4x^{3}-3x_{1}x^{2}-3x_{2}x^{2}-3x_{3}x^{2}-3x_{4}x^{2}+2x_{1}x_{2}x+2x_{1}x_{3}x+2x_{1}x_{4}x+2x_{2}x_{3}x+2x_{2}x_{4}x+2x_{3}x_{4}x-x_{1}x_{2}x_{3}-x_{1}x_{2}x_{4}-x_{1}x_{3}x_{4}-x_{2}x_{3}x_{4})y_{0}}{(x_{0}-x_{1})(x_{0}-x_{2})(x_{0}-x_{3})(x_{0}-x_{4})}$"]
    fin += [r"$+\frac{(4x^{3}-3x_{0}x^{2}-3x_{2}x^{2}-3x_{3}x^{2}-3x_{4}x^{2}+2x_{0}x_{2}x+2x_{0}x_{3}x+2x_{0}x_{4}x+2x_{2}x_{3}x+2x_{2}x_{4}x+2x_{3}x_{4}x-x_{0}x_{2}x_{3}-x_{0}x_{2}x_{4}-x_{0}x_{3}x_{4}-x_{2}x_{3}x_{4})y_{1}}{(x_{1}-x_{0})(x_{1}-x_{2})(x_{1}-x_{3})(x_{1}-x_{4})}$"]
    fin += [r"$+\frac{(4x^{3}-3x_{0}x^{2}-3x_{1}x^{2}-3x_{3}x^{2}-3x_{4}x^{2}+2x_{0}x_{1}x+2x_{0}x_{3}x+2x_{0}x_{4}x+2x_{1}x_{3}x+2x_{1}x_{4}x+2x_{3}x_{4}x-x_{0}x_{1}x_{3}-x_{0}x_{1}x_{4}-x_{0}x_{3}x_{4}-x_{1}x_{3}x_{4})y_{2}}{(x_{2}-x_{0})(x_{2}-x_{1})(x_{2}-x_{3})(x_{2}-x_{4})}$"]
    fin += [r"$+\frac{(4x^{3}-3x_{0}x^{2}-3x_{1}x^{2}-3x_{2}x^{2}-3x_{4}x^{2}+2x_{0}x_{1}x+2x_{0}x_{2}x+2x_{0}x_{4}x+2x_{1}x_{2}x+2x_{1}x_{4}x+2x_{2}x_{4}x-x_{0}x_{1}x_{2}-x_{0}x_{1}x_{4}-x_{0}x_{2}x_{4}-x_{1}x_{2}x_{4})y_{3}}{(x_{3}-x_{0})(x_{3}-x_{1})(x_{3}-x_{2})(x_{3}-x_{4})}$"]
    fin += [r"$+\frac{(4x^{3}-3x_{0}x^{2}-3x_{1}x^{2}-3x_{2}x^{2}-3x_{3}x^{2}+2x_{0}x_{1}x+2x_{0}x_{2}x+2x_{0}x_{3}x+2x_{1}x_{2}x+2x_{1}x_{3}x+2x_{2}x_{3}x-x_{0}x_{1}x_{2}-x_{0}x_{1}x_{3}-x_{0}x_{2}x_{3}-x_{1}x_{2}x_{3})y_{4}}{(x_{4}-x_{0})(x_{4}-x_{1})(x_{4}-x_{2})(x_{4}-x_{3})}$"]

    fin += ["Третьи разности: "]
    fin += [r"$P^{'}(x)=\frac{(2x-x_{1}-x_{2})y_{0}}{(x_{0}-x_{1})(x_{0}-x_{2})}+\frac{(2x-x_{0}-x_{2})y_{1}}{(x_{1}-x_{0})(x_{1}-x_{2})}+\frac{(2x-x_{0}-x_{1})y_{2}}{(x_{2}-x_{0})(x_{2}-x_{1})}$"]

    fin += ["Пятые разности: "]
    for i in range(len(x)):
        fin += [
            rf"$P^{{'}}({x[i]})=\frac{{(4*{x[i]}^{3}-3*{x[1]}*{x[i]}^{2}-3*{x[2]}*{x[i]}^{2}-3*{x[3]}*{x[i]}^{2}-3*{x[4]}*{x[i]}^{2}+2*{x[1]}*{x[2]}*{x[i]}+2*{x[1]}*{x[3]}*{x[i]}+2*{x[1]}*{x[4]}*{x[i]}+2*{x[2]}*{x[3]}*{x[i]}+2*{x[2]}*{x[4]}*{x[i]}+2*{x[3]}*{x[4]}*{x[i]}-{x[1]}*{x[2]}*{x[3]}-{x[1]}*{x[2]}*{x[4]}-{x[1]}*{x[3]}*{x[4]}-{x[2]}*{x[3]}*{x[4]}){y[0]}}}{{({x[0]}-{x[1]})({x[0]}-{x[2]})({x[0]}-{x[3]})({x[0]}-{x[4]})}}$"]
        fin += [
            rf"$+\frac{{(4*{x[i]}^{3}-3*{x[0]}*{x[i]}^{2}-3*{x[2]}*{x[i]}^{2}-3*{x[3]}*{x[i]}^{2}-3*{x[4]}*{x[i]}^{2}+2*{x[0]}*{x[2]}*{x[i]}+2*{x[0]}*{x[3]}*{x[i]}+2*{x[0]}*{x[4]}*{x[i]}+2*{x[2]}*{x[3]}*{x[i]}+2*{x[2]}*{x[4]}*{x[i]}+2*{x[3]}*{x[4]}*{x[i]}-{x[0]}*{x[2]}*{x[3]}-{x[0]}*{x[2]}*{x[4]}-{x[0]}*{x[3]}*{x[4]}-{x[2]}*{x[3]}*{x[4]}){y[1]}}}{{({x[1]}-{x[0]})({x[1]}-{x[2]})({x[1]}-{x[3]})({x[1]}-{x[4]})}}$"]
        fin += [
            rf"$+\frac{{(4*{x[i]}^{3}-3*{x[0]}*{x[i]}^{2}-3*{x[1]}*{x[i]}^{2}-3*{x[3]}*{x[i]}^{2}-3*{x[4]}*{x[i]}^{2}+2*{x[0]}**{x[1]}*{x[i]}+2*{x[0]}*{x[3]}*{x[i]}+2*{x[0]}*{x[4]}*{x[i]}+2*{x[1]}*{x[3]}*{x[i]}+2*{x[1]}*{x[4]}*{x[i]}+2*{x[3]}*{x[4]}*{x[i]}-{x[0]}*{x[1]}*{x[3]}-{x[0]}*{x[1]}*{x[4]}-{x[0]}*{x[3]}*{x[4]}-{x[1]}*{x[3]}*{x[4]}){y[2]}}}{{({x[2]}-{x[0]})({x[2]}-{x[1]})({x[2]}-{x[3]})({x[2]}-{x[4]})}}$"]
        fin += [
            rf"$+\frac{{(4*{x[i]}^{3}-3*{x[0]}*{x[i]}^{2}-3*{x[1]}*{x[i]}^{2}-3*{x[2]}*{x[i]}^{2}-3*{x[4]}*{x[i]}^{2}+2*{x[0]}*{x[1]}*{x[i]}+2*{x[0]}*{x[2]}*{x[i]}+2*{x[0]}*{x[4]}*{x[i]}+2*{x[1]}*{x[2]}*{x[i]}+2*{x[1]}*{x[4]}*{x[i]}+2*{x[2]}*{x[4]}*{x[i]}-{x[0]}*{x[1]}*{x[2]}-{x[0]}*{x[1]}*{x[4]}-{x[0]}*{x[2]}*{x[4]}-{x[1]}*{x[2]}*{x[4]}){y[3]}}}{{({x[3]}-{x[0]})({x[3]}-{x[1]})({x[3]}-{x[2]})({x[3]}-{x[4]})}}$"]
        fin += [
            rf"$+\frac{{(4*{x[i]}^{3}-3*{x[0]}*{x[i]}^{2}-3*{x[1]}*{x[i]}^{2}-3*{x[2]}*{x[i]}^{2}-3*{x[3]}*{x[i]}^{2}+2*{x[0]}*{x[1]}*{x[i]}+2*{x[0]}*{x[2]}*{x[i]}+2*{x[0]}*{x[3]}*{x[i]}+2*{x[1]}*{x[2]}*{x[i]}+2*{x[1]}*{x[3]}*{x[i]}+2*{x[2]}*{x[3]}*{x[i]}-{x[0]}*{x[1]}*{x[2]}-{x[0]}*{x[1]}*{x[3]}-{x[0]}*{x[2]}*{x[3]}-{x[1]}*{x[2]}*{x[3]}){y[4]}}}{{({x[4]}-{x[0]})({x[4]}-{x[1]})({x[4]}-{x[2]})({x[4]}-{x[3]})}}$"]

    fin += ["Третьи разности: "]
    for i in range(len(x)):
        fin += [
            rf"$P^{{'}}({x[i]})=\frac{{(2*{x[i]}-{x[1]}-{x[2]}){y[0]}}}{{({x[0]}-{x[1]})({x[0]}-{x[2]})}}+\frac{{(2*{x[i]}-{x[0]}-{x[2]}){y[1]}}}{{({x[1]}-{x[0]})({x[1]}-{x[2]})}}+\frac{{(2*{x[i]}-{x[0]}-{x[1]}){y[1]}}}{{({x[2]}-{x[0]})({x[2]}-{x[1]})}}$"]
    root = tk.Toplevel()
    app = Application(fin, master=root)
    app.mainloop()

# Функция draw рисует наши кривые на координатной плоскости
def draw(xL, yL, y3, y5):
    thread = Thread(target=lambda: formula(xL, yL))
    thread.start()
    print(len(xL), len(yL), len(y3), len(y5))
    plt.scatter(xL, y3)
    plt.plot(xL, y3, label="график по 3-им разностям")
    plt.scatter(xL, y5)
    plt.plot(xL, y5, label="график по 5-ым разностям")
    plt.legend(loc="upper right")
    plt.show()


x = [0.00, 5.01, 10.09, 13.98, 16.62, 18.01, 22.53, 25.33, 28.03, 30.42, 32.06, 33.62]
y = [0.00, 0.18, 1.05, 1.73, 2.35, 2.96, 3.76, 4.48, 5.28, 6.12, 7.09, 8.00]
fin = []
Test(x, y)
