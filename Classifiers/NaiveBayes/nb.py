from sklearn.naive_bayes import GaussianNB
import csv

def getDataSet(mode):
    dataset = csv.reader(open(mode, 'rb'))
    Features, Lables = [], []
    for row in dataset:
        Features.append(map(int, row[0]))
        if mode is 'train':
            Lables.append(int(row[1]))
    if mode is 'train':
        return Features, Lables
    else:
        return Features

def printAns(f, l):
    for i in range(0, len(l)):
        s = ''.join(str(j) for j in f[i])
        if l[i] == 0: v = "Sports"
        else: v = "Informatics"
        print s, v

if __name__ == '__main__':
    Features, Lables = getDataSet('train')
    naive_bayes = GaussianNB().fit(Features, Lables)
    Features = getDataSet('test')
    output = naive_bayes.predict(Features)
    printAns(Features, output)
