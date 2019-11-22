import pandas as pd
import os

fileList = os.listdir(".")
yearList = [f for f in fileList if f.startswith('Mortality_Yearly_')]
origList = [f for f in fileList if (f.startswith('Mortality_')) and ('Monthly' not in f) and ('Yearly' not in f)]
origList = sorted(origList)
yearList = sorted(yearList)

y = 2006
for fpair in zip(origList, yearList):
    old = pd.read_csv(fpair[0])
    new = pd.read_csv(fpair[1])
    old['Year']=y
    if (old.equals(new)):
        print('Passed!')
    else:
        print('failed!')
    y += 1