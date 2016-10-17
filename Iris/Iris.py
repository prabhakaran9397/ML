#BEGIN
from sklearn import tree
import csv
import re
Dataset     = csv.reader(open("Data",  "rb"), delimiter=' ')
Int         = "^[0-9]+$"
Float       = "^[0-9]+.?[0-9]*$"
Features    = []
Labels      = []
Index       = 0
NumberRepo  = {}
for row in Dataset:
    Arr  = []
    for i in range(len(row)-1):
        if re.search(Int, row[i]):
            Arr.append(int(row[i]))
        elif re.search(Float, row[i]):
            Arr.append(float(row[i]))
        else:
            NumberRepo.setdefault(row[i], Index)
            Arr.append(NumberRepo[row[i]])
            if NumberRepo[row[i]] == Index:
                Index += 1
    Features.append(Arr) 
    NumberRepo.setdefault(row[len(row)-1], Index)
    Labels.append(NumberRepo[row[len(row)-1]])
    if NumberRepo[row[len(row)-1]] == Index:
        Index += 1
classifier  = tree.DecisionTreeClassifier().fit(Features, Labels)
#END

#DRIVER
Input       = map(float, raw_input("SL SW PL PW: ").split())
predicted   =  classifier.predict([Input])
print NumberRepo.keys()[NumberRepo.values().index(predicted[0])]
