import matplotlib.pyplot as plt
import numpy as np

pliki = ["1ers.csv","1crs.csv","2crs.csv","1c.csv","2c.csv"]
nazwy = ["1-Evol-RS","1-Coev-RS", "2-Coev-RS","1-Coev", "2-Coev"]
dane = []

def main():
    for i in range(len(pliki)):    
        dane.append([])
        with open(pliki[i]) as f:
            for line in f.readlines()[1:]:
                dane[i].append(line.split(',')[1:])
        # print(pliki[i],np.array(dane[i]),"\n")

    plt.style.use("classic")

    GrafMain = plt.figure(figsize=(10, 7))
    
    GrafLeft = GrafMain.add_subplot(121)
    osX = []
    i = 0

    for rows in dane:
        osX.append([])
        for row in rows:
            osX[i].append(float(row[0])/1000.0)
        i += 1
    # print(np.array(osX))

    osY = []
    j = 0
    for rows in dane:
        osY.append([])
        for row in rows:
            suma = sum(list(map(float,row[1:])))
            count = float(len(row) - 1)
            osY[j].append(((suma/count) * 100.0))
        j += 1
    # print(np.array(osY))
    
    GrafLeft.plot(osX[0], osY[0], label=nazwy[0], color='blue',
              marker='o', markersize=7, markevery=25, markeredgecolor='black')
        
    GrafLeft.plot(osX[1], osY[1],label=nazwy[1], color='green',
              marker='v', markersize=7, markevery=25, markeredgecolor='black')
    
    GrafLeft.plot(osX[2], osY[2],label=nazwy[2], color='red',
              marker='D', markersize=7, markevery=25, markeredgecolor='black')
        
    GrafLeft.plot(osX[3], osY[3],label=nazwy[3], color='black',
              marker='s', markersize=7, markevery=25, markeredgecolor='black')
    
    GrafLeft.plot(osX[4], osY[4],label=nazwy[4], color='magenta',
              marker='d', markersize=7, markevery=25, markeredgecolor='black')

    GrafLeft.legend(loc=4)
    GrafLeft.set_xlabel(r"Rozegranych gier ($\times$1000)", fontfamily='Times New Roman', fontsize = 12)
    GrafLeft.set_ylabel(r"Odsetek wygranych gier [$\%$]", fontfamily='Times New Roman', fontsize = 12)
    GrafLeft.set_xlim(0, 500)
    GrafLeft.grid()


    GrafTop = plt.twiny()
    GrafTop.set_xlim(0,200)
    GrafTop.set_xticks([0, 100, 200, 300, 400, 500])
    GrafTop.set_xticklabels(["0", "40", "80", "120", "160", "200"])
    GrafTop.set_xlabel("Pokolenie", fontfamily='Times New Roman', fontsize = 12)
    
    GrafRight = GrafMain.add_subplot(122)

    srednie = []
    l = 0
    for rows in dane:
        wynik = []
        for x in rows[-1][1:]:
            wynik.append(float(x) * 100)
        srednie.append(wynik)
        l += 1
    # print(np.array(srednie))

    srednie_pudelkowe = [ sum(srednie[0]) / len(srednie[0]),
                         sum(srednie[1]) / len(srednie[1]), 
                         sum(srednie[2]) / len(srednie[2]), 
                         sum(srednie[3]) / len(srednie[3]), 
                         sum(srednie[4]) / len(srednie[4])]
    
    GrafRight.scatter([1, 3, 5, 7, 9], srednie_pudelkowe, s=40)

    bp = GrafRight.boxplot(srednie, positions = [1, 3, 5, 7, 9], boxprops = dict(linewidth=1.5), medianprops = dict(linewidth=1.5), widths = 1, notch=True,
                                                                                                          sym='+', flierprops = dict(marker='+',
                                                                                                          markeredgecolor='blue',
                                                                                                          markersize=8,
                                                                                                          markeredgewidth=0.5))
    
    for whisker in bp['whiskers']:
        whisker.set(color='b',
                    linewidth=1.5,
                    linestyle=(0,(5,5)))
        
    GrafRight.grid(linestyle = (0, (1, 5)))
    GrafRight.set_xticks([1, 3, 5, 7, 9])
    GrafRight.set_xticklabels(nazwy, rotation=20, fontsize = 14)
    GrafRight.set_ylim(60, 100)
    GrafRight.set_xlim(0, 10)
    GrafRight.yaxis.tick_right()
    GrafRight.yaxis.set_label_position("right")
    
    plt.savefig('myplot.pdf')
    plt.close()

if __name__ == '__main__':
    main()