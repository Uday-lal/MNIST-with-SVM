import mnist
from matplotlib import pyplot
# from sklearn.svm import LinearSVC
import pickle


X_train = mnist.train_images()
y_train = mnist.train_labels()
X_test = mnist.test_images()
y_test = mnist.test_labels()

# Shaping the datasets
n_sample, nx, ny = X_train.shape
n_sample_test, nx_test, ny_test = X_test.shape
clean_datasets = X_train.reshape((n_sample, nx*ny))
clean_x_test = X_test.reshape((n_sample_test, nx_test*ny_test))

# Starting training
# svm = LinearSVC()
# svm.fit(clean_datasets, y_train)
# print(svm.score(clean_datasets, y_train))
file = open("mnist.pickel", "rb")
svm = pickle.load(file)
predict = svm.predict(clean_x_test)

# Plotting the data
for i in range(len(X_test)):
    pyplot.imshow(X_test[i], cmap=pyplot.cm.get_cmap("binary"))
    print("Predict: ", predict[i])
    pyplot.show()
