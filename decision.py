from sklearn import tree
import tensorflow as tf
features = [[140, 1], [130, 1], [150, 0], [170, 0], [110, 1], [180, 0]] # let 1 = smooth & 0 = bumpy
fruits = [1, 1, 0, 0, 1, 0] # let 1 = apples & 0 = oranges


#saved_model.summary()

input = [[10,10,10,10,10,10,10,10,10,10]]
#print(saved_model.predict(input))

class Prediction:
    def __init__(self, data):
        #self.clf = tree.DecisionTreeClassifier()
        self.dt = data
        #self.txt = 1 if texture == 'smooth' else 0

    # def train(self):
    #     self.clf = self.clf.fit(features, fruits)

    def test(self):
        saved_model = tf.keras.models.load_model("saved_model/ins_model1")
        return (saved_model.predict(self.dt))[0][0]