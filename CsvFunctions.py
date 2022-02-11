import pandas as pd
import requests
import io
import Github_push
def readScore(Table):
    csv = pd.read_csv('CsvForSnake.csv', sep=",")
    print(csv)
    csv.sort_values(csv.columns[1], ascending=False, inplace=True)
    csv.reset_index(inplace=True)
    csv.drop(columns="index", inplace=True)
    df = pd.DataFrame(csv)
    ListOfScores = df.head(10).values.tolist()
    for Score in ListOfScores:
       Table.insert(parent='', index='end', values=(Score[0], Score[1]))


def addRow(csvPath, score, name):
    url = "https://raw.githubusercontent.com/eugenepascalyaro/HostCsvForSnake/main/CsvForSnake.csv"
    s = requests.get(url).content
    csvoriginal = pd.read_csv(io.StringIO(s.decode('utf-8')), sep=",")
    print(csvoriginal)
    if name == "":
        df = pd.DataFrame({str(csvoriginal.columns[0]): ["Unamed player"], str(csvoriginal.columns[1]): [score]})
    else:
        df = pd.DataFrame({str(csvoriginal.columns[0]): [name], str(csvoriginal.columns[1]): [score]})

    csv = pd.concat([csvoriginal, df])
    print(csv)
    csv.sort_values(csv.columns[1], ascending=False, inplace=True)
    csv.to_csv('CsvForSnake.csv', index=False)
    Github_push.Git_Push_Csv_File()

