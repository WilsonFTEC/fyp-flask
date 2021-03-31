from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0], [110, 1], [180, 0]] # let 1 = smooth & 0 = bumpy
fruits = [1, 1, 0, 0, 1, 0] # let 1 = apples & 0 = oranges

class Fruit:
    def __init__(self, weight, texture):
        self.clf = tree.DecisionTreeClassifier()
        self.wt = weight
        self.txt = 1 if texture == 'smooth' else 0

    def train(self):
        self.clf = self.clf.fit(features, fruits)

    def test(self):
        return 'Orange' if self.clf.predict([[self.wt, self.txt]]) == [0] else 'Apple'