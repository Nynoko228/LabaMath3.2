import matplotlib.pyplot as plt #для графиков



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

def Math():
    global x, y
    k = 12
    h = float(x[1]-x[0])
    Y5 = [] # Пятые производные
    Y5.append(1/(12*h)*(0-3*Lagrandj(x[0]+4*h)+16*Lagrandj(x[0]+3*h)-36*Lagrandj(x[0]+2*h)+48*Lagrandj(x[0]+1*h)-25*Lagrandj(x[0])))
    h = float(x[1]-x[0])
    Y5.append(1/(12*h)*(0-3*Lagrandj(x[1]+4*h)+16*Lagrandj(x[1]+3*h)-36*Lagrandj(x[1]+2*h)+48*Lagrandj(x[1]+1*h)-25*Lagrandj(x[1])))

    for i in  range(2, k-2):
        h = (x[i + 2] - x[i - 2]) / 4
        Y5.append((-Lagrandj(x[i] - 2 * h) - 8 * Lagrandj(x[i] - 1 * h) + 8 * Lagrandj(x[i] + 1 * h) + Lagrandj(x[i] + 2 * h)) / (12 * h))

    h = (x[k - 2] - x[k - 6]) / 4
    Y5.append(1 / (12 * h) * (3 * Lagrandj(x[k - 2] - 4 * h) - 16 * Lagrandj(x[k - 2] - 3 * h) + 36 * Lagrandj(x[k - 2] - 2 * h) - 48 * Lagrandj(x[k - 2] - 1 * h) + 25 * Lagrandj(x[k - 2])))
    h = (x[k - 1] - x[k - 5]) / 4
    Y5.append(1 / (12 * h) * (3 * Lagrandj(x[k - 1] - 4 * h) - 16 * Lagrandj(x[k - 1] - 3 * h) + 36 * Lagrandj(x[k - 1] - 2 * h) - 48 * Lagrandj(x[k - 1] - 1 * h) + 25 * Lagrandj(x[k - 1])))

    Y3 = [] # Третьи производные
    h = x[1] - x[0]
    Y3.append(1/(2*(x[1]-x[0]))*(-Lagrandj(x[0]+2*h)+4*Lagrandj(x[0]+1*h)-3*Lagrandj(x[0])))

    for i in range(1, k-1):
        h = (x[i + 1] - x[i - 1]) / 2
        Y3.append(1/((x[i+1]-x[i-1]))*(-Lagrandj(x[i]-1*h)+Lagrandj(x[i]+1*h)))

    h = x[k - 1] - x[k - 2]
    Y3.append(1/((x[k-1]-x[k-3]))*(Lagrandj(x[k-1]-2*h)-4*Lagrandj(x[k-1]-1*h)+3*Lagrandj(x[k-1])))
    draw(x, y, Y3, Y5)

# Функция draw рисует наши кривые на координатной плоскости
def draw(xL, yL, y3, y5):
    # print(len(xL), len(yL), len(y3), len(y5))
    plt.plot(xL, y3, label="график по 3-им разностям")
    # plt.scatter(xL, y5, label="табличные данные")
    plt.plot(xL, y5, label="график по 5-ым разностям")
    plt.legend(loc="upper right")
    plt.show()

h = 2
x = [0.00, 5.01, 10.09, 13.98, 16.62, 18.01, 22.53, 25.33, 28.03, 30.42, 32.06, 33.62]
y = [0.00, 0.18, 1.05, 1.73, 2.35, 2.96, 3.76, 4.48, 5.28, 6.12, 7.09, 8.00]
y3, y5, xL, yL = [], [], [], []
Math()