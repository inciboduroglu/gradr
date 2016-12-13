from sklearn.svm import SVR
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from sklearn.externals import joblib as jb
import pickle


def learn(X, y):
    # do pca

    # do svr
    svr_rbf = SVR(kernel='rbf', C=10)
    svr_rbf.fit(X, y)
    # print(model_rbf)

    y_rbf = svr_rbf.predict(X)
    print(y_rbf)
    print(y)

    # see difference
    y_rbf = np.transpose(y_rbf)
    deviation(y, y_rbf)

    # pickle model
    # jb.dump(svr_rbf, 'rbfmodel.pkl')
    with open('rbfmodel.pkl', 'wb') as f:
        pickle.dump(svr_rbf, f)


def test(X, y):
    model = jb.load('rbfmodel.pkl')
    y_pred = model.predict(X)
    print(y_pred)
    print(y)

    print('test')
    deviation(y, y_pred)


def deviation(y, y_pred):
    diff = np.absolute(np.subtract(y, y_pred))
    sigma = np.std(diff)
    mean = np.mean(diff)

    # print out mean and st. dev
    print('mean %f' % mean)
    print('sigma %f' % sigma)

    # x = np.linspace(-0.5, 0.5, 100)
    # plt.plot(x, mlab.normpdf(x, mean, sigma))
    #
    # plt.show()


# load data
data_num = 12978
data = np.load('traindata.npy')

# mix data
dummy = np.arange(data_num).reshape((data_num, 1))
dummy = np.concatenate((dummy, data), axis=1)
dummy = np.random.permutation(dummy)

# print(dummy)

# separate data
X = dummy[:, 1:dummy.shape[1] - 1]  # data num at[0]
y = dummy[:, dummy.shape[1] - 1]

# print(X.shape[1])
# print(y)

train_num = np.int(np.ceil(0.7 * data_num))
train_X = X[0:train_num, :]
train_y = y[0:train_num]

test_X = X[train_num:X.shape[0], :]
test_y = y[train_num:y.shape[0]]

learn(train_X, train_y)
test(test_X, test_y)
