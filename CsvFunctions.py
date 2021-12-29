import pandas as pd


def readScore(csvPath):
    csv = pd.read_csv(csvPath, sep=",")
    csv.sort_values(csv.columns[1], ascending=False, inplace=True)
    csv.reset_index(inplace=True)
    csv.drop(columns="index", inplace=True)
    return csv

def addRow(csv,score,name):
    df = pd.DataFrame({str(csv.columns[0]):[name],str(csv.columns[1]):[score]})
    csv = pd.concat([csv,df])
    csv.sort_values(csv.columns[1], ascending=False, inplace= True)
    csv.reset_index(inplace= True)
    csv.drop(columns="index", inplace=True)
    #csv.to_csv("testCsv.csv",inplace = True)
    return csv

def personalBestRead(csv,name):
    return csv[csv[csv.columns[0]] == name].iloc[0].Score