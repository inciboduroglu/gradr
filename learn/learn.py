from sklearn.svm import SVR
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from sklearn.externals import joblib as jb
import pickle


def learn(X, y):
    # do pca
    pca = PCA(n_components=6)
    pca_6 = pca.fit(X)

    print('variance ratio')
    print(pca_6.explained_variance_ratio_)
    X = pca.fit_transform(X)

    # X = np.concatenate((X_pca[:, 0].reshape(X.shape[0], 1), X_pca[:, 5].reshape(X.shape[0], 1)), axis=1)
    # do svr
    svr_rbf = SVR(kernel='rbf', C=1)
    svr_rbf.fit(X, y)
    # print(model_rbf)

    y_rbf = svr_rbf.predict(X)
    print(y_rbf)
    print(y)

    # see difference
    y_rbf = np.transpose(y_rbf)
    deviation(y, y_rbf)

    # pickle model
    with open('rbfmodel.pkl', 'wb') as f:
        pickle.dump(svr_rbf, f)

    with open('pcamodel.pkl', 'wb') as f:
        pickle.dump(pca_6, f)


def test(X, y):
    model = jb.load('rbfmodel.pkl')
    decomp = jb.load('pcamodel.pkl')

    X = decomp.fit_transform(X)
    y_pred = model.predict(X)
    print(y_pred)
    print(y)

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


def plotdat(X, y):
    x_axis = X[:, 0]
    y_axis = X[:, 1]

    # print(y)
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x_axis, y_axis, y, c='darkorange', label='data')

    ax.set_xlabel('pc1')
    ax.set_ylabel('pc2')
    ax.set_zlabel('target')

    plt.legend()
    plt.show()


# load data
data = np.load('traindata.npy')
data_num = data.shape[0]

# mix data
dummy = np.arange(data_num).reshape((data_num, 1))
dummy = np.concatenate((dummy, data), axis=1)
dummy = np.random.permutation(dummy)

# separate data
X = dummy[:, 1:dummy.shape[1] - 1]  # data num at[0]
y = dummy[:, dummy.shape[1] - 1]

train_num = np.int(np.ceil(0.7 * data_num))
train_X = X[0:train_num, :]
train_y = y[0:train_num]

test_X = X[train_num:X.shape[0], :]
test_y = y[train_num:y.shape[0]]

learn(train_X, train_y)
test(test_X, test_y)

# plot
# plotdat(train_X, train_y)
# plotdat(test_X, test_y)
