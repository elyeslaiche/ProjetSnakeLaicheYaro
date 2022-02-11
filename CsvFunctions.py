import pandas as pd
import requests
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


def addRow(score, name):
    csvoriginal = pd.read_csv('CsvForSnake.csv', sep=",")
    if name == "":
        df = pd.DataFrame({str(csvoriginal.columns[0]): ["Unamed player"], str(csvoriginal.columns[1]): [score]})
    else:
        df = pd.DataFrame({str(csvoriginal.columns[0]): [name], str(csvoriginal.columns[1]): [score]})

    csv = pd.concat([csvoriginal, df])
    csv.sort_values(csv.columns[1], ascending=False, inplace=True)
    csv.to_csv('CsvForSnake.csv', index=False)

