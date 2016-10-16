#!/usr/bin/python

from sklearn import tree
smooth      = 0
bumpy       = 1

Fruits = {"apple" : 0, "orange" : 1}

features    = [[140, smooth], [130, smooth], [150, bumpy], [170, bumpy]]
labels      = [Fruits["apple"], Fruits["apple"], Fruits["orange"], Fruits["orange"]]
classifier  = tree.DecisionTreeClassifier().fit(features, labels)

weight      = input("Whats the weight? ")
texture     = input("smooth(0) or bumpy(1)? ")

predicted   =  classifier.predict([[weight, texture]])

print Fruits.keys()[Fruits.values().index(predicted[0])]
