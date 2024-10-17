import matplotlib.pyplot as plt
import numpy as np

# 1coev , 1coevrs, 1evolrs, 2coev, 2coevrs
pliki = ["1c.csv","1crs.csv","1ers.csv","2c.csv","2crs.csv"]
dane = []

def main():
    for i in range(len(pliki)):     #Odczytanie danych z plików
        dane.append([])
        with open(pliki[i]) as f:
            for line in f.readlines()[1:]:
                dane[i].append(line.split(',')[1:])
        # print(pliki[i],np.array(dane[i]),"\n")

    GrafMain = plt.figure(figsize=(10, 5))
    
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
            count = float(len(rows) - 1)
            osY[j].append(suma/count * 100.0)
        j += 1
    # print(np.array(osY))
    
    GrafLeft.plot(osX[0], osY[0],label="1-Coev", color='black',
              marker='s', markersize=7, markevery=25, markeredgecolor='black')
    
    GrafLeft.plot(osX[1], osY[1],label="1-Coev-RS", color='green',
              marker='v', markersize=7, markevery=25, markeredgecolor='black')
    
    GrafLeft.plot(osX[2], osY[2],label="1-Evol-RS", color='blue',
              marker='o', markersize=7, markevery=25, markeredgecolor='black')
    
    GrafLeft.plot(osX[3], osY[3],label="2-Coev", color='magenta',
              marker='d', markersize=7, markevery=25, markeredgecolor='black')
    
    GrafLeft.plot(osX[4], osY[4],label="2-Coev-RS", color='red',
              marker='D', markersize=7, markevery=25, markeredgecolor='black')

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


    
    plt.savefig('myplot.pdf')
    plt.close()

if __name__ == '__main__':
    main()