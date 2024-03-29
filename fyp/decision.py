import tensorflow as tf

# testing input format
# input = [[10,10,10,10,10,10,10,10,10,10]]


class Prediction:
    def __init__(self, data):
        self.dt = data

    def test(self):
        saved_model = tf.keras.models.load_model("fyp/saved_model/ins_model1")
        return (saved_model.predict(self.dt))[0][0]

