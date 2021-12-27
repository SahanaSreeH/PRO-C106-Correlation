import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    attendance = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            attendance.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Prcentage"]))

    return {"x" : marks, "y" : attendance}

def findCorrlation(datasource):
    correlation = np.coorrcoef(datasource["x"], datasource["y"])
    print("Correlation between Days Present and Marks In Percentage :-   \n--->", correlation[0,1])

def setup(): 
    data_path = "C:\Projects\PRO-C106-Correlation\data\Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)
    findCorrlation(data_source)

setup()