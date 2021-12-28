from CsvFunctions import*

if __name__ == '__main__':
    csv = readScore('C:\\Users\\Elyes\\Desktop\\testCsv.csv')
    print(csv.iloc[:3]) #recup le top 3
    print()
    name = "Elyes"
    personalBest = personalBestRead(csv,name)
    print(f'personal best of {name} = {personalBest} ')