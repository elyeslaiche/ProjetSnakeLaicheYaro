import InterfaceGraphique
from CsvFunctions import *

if __name__ == '__main__':
    #csv = readScore('testCsv.csv')
    # csv = addRow(csv,50,"Pascal")
    # print(csv.iloc[:3]) #recup le top 3
    #print()
    # name = "Elyes"
    # personalBest = personalBestRead(csv,name)
# print(f'personal best of {name} = {personalBest} ')
    fenetre = InterfaceGraphique.initConfigWindow()
    fenetre.mainloop()
