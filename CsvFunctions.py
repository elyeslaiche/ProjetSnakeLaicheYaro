import pandas as pd

def readScore(csvPath):
    csv = pd.read_csv(csvPath, sep=",")
    csv.sort_values(csv.columns[1], ascending=False, inplace=True)
    csv.reset_index(inplace=True)
    csv.drop(columns="index", inplace=True)
    return csv

def addRow(csvPath,score,name):

    csvoriginal = pd.read_csv(csvPath, sep=",")
    if(name == ""):
        df = pd.DataFrame({str(csvoriginal.columns[0]): ["Unamed player"], str(csvoriginal.columns[1]): [score]})
    else:
        df = pd.DataFrame({str(csvoriginal.columns[0]):[name],str(csvoriginal.columns[1]):[score]})

    csv = pd.concat([csvoriginal, df])
    csv.sort_values(csv.columns[1], ascending=False, inplace=True)

    csv.to_csv("testCsv.csv", index=False)


def personalBestRead(csv,name):
    return csv[csv[csv.columns[0]] == name].iloc[0].Score



