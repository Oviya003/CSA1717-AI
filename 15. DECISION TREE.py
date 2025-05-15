from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

iris = load_iris()
X, y = iris.data, iris.target
clf = DecisionTreeClassifier()
clf.fit(X, y)

print(export_text(clf, feature_names=iris.feature_names))
