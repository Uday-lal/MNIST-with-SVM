import mnist  # pip install mnist
from matplotlib import pyplot
from sklearn.svm import LinearSVC
import pickle

# MNIST module provide mnist dataset.
# But the problem is it has three dimensional array so you need to make it into correct shape before start using it.


X_train = mnist.train_images()
y_train = mnist.train_labels()
X_test = mnist.test_images()
y_test = mnist.test_labels()

# Shaping the datasets
n_sample, nx, ny = X_train.shape
n_sample_test, nx_test, ny_test = X_test.shape
clean_datasets = X_train.reshape((n_sample, nx * ny))
clean_x_test = X_test.reshape((n_sample_test, nx_test * ny_test))


# Starting training
def training():
    """
    Training the model
    :return: Accuracy of model
    """
    svm = LinearSVC()
    svm.fit(clean_datasets, y_train)
    acc = svm.score(clean_datasets, y_train)
    return acc


def save_model(model_obj):
    """
    For saving the model
    :param model_obj: AI algorithm.
    :return: None
    """
    file = open("mnist.pickle", "wb")
    pickle.dump(model_obj, file)
    return None


def prediction(data):
    """
    Making prediction.
    :param data: Input data or testing data
    :return: list
    """
    file = open("mnist.pickle", "rb")
    model = pickle.load(file)
    predict = model.predict(data)
    return predict


def visualization(data, y=None):
    """
    For Visualize the data
    :param y: If y doesn't provided then by default it is None
    :param data: X dataset
    :return: None
    """
    for i in range(len(data)):
        pyplot.imshow(data[i], cmap=pyplot.cm.get_cmap("binary"))
        if y:
            print(y)
        pyplot.show()
    return None
