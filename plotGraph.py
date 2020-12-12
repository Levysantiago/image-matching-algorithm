# Fonte: https://github.com/Mrpsousa/plot_graph_python/blob/main/plot.py

import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
                '%d' % int(height),
                ha='center', va='bottom')

# Cria eixo x para produto A e produto B com uma separação de 0.25 entre as barras
def plot_graph(algoritimo_A, algoritimo_B, algoritimo_C, quant_teste):
    x1 =  np.arange(len(algoritimo_A))
    x2 = [x + 0.25 for x in x1]
    x3 = [x + 0.25 for x in x2]

    # Plota as barras
    ax = plt.subplot()
    rect1 = ax.bar(x1, algoritimo_A, width=0.25, label = 'lr2m', color = 'c')
    autolabel(rect1, ax)
    rect2 = ax.bar(x2, algoritimo_B, width=0.25, label = 'lr2mRGB', color = 'orange')
    autolabel(rect2, ax)
    rect3 = ax.bar(x3, algoritimo_C, width=0.25, label = 'SIFT', color = 'b')
    autolabel(rect3, ax)
    plt.xlabel("Testes")
    plt.ylabel("Tempo (ms)")

    # coloca o nome dos meses como label do eixo x
    meses = []
    i = 0
    for i in range(quant_teste):
        meses.append('T'+str(i+1))

    
    plt.xticks([x + 0.25 for x in range(len(algoritimo_A))], meses)

    # inseri uma legenda no gráfico
    plt.legend()

    plt.title("Tempo de execução")
    plt.savefig("graph/comparison")
    # plt.show()
