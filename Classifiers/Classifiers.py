from sklearn import datasets, tree 
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

Iris = datasets.load_iris()
x = Iris.data
y = Iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

classifier_1 = tree.DecisionTreeClassifier()
classifier = KNeighborsClassifier() 

classifier.fit(x_train, y_train)
predicted = classifier.predict(x_test)
print accuracy_score(y_test, predicted)
