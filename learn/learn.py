from sklearn.svm import SVR
from sklearn import svm
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from sklearn.externals import joblib as jb
import pickle
from heapq import nlargest
from sklearn.metrics import r2_score


def learn(X, y):
    # data = X
    # main svm labels
    svm_y = y[:, -1]
    svr_y = y[:, -2]

    # do pca
    # pca = PCA(n_components=6)
    # pca_6 = pca.fit(X)

    # print('variance ratio')
    # print(pca_6.explained_variance_ratio_)
    # X = pca.fit_transform(X)

    # do svm
    svm_0 = svm.SVC(probability=True)
    svm_0.fit(X, svm_y)

    # do svr for each
    X_1 = X[svm_y[:] == 1]
    X_2 = X[svm_y[:] == 2]
    X_3 = X[svm_y[:] == 3]
    X_4 = X[svm_y[:] == 4]

    y_1 = svr_y[svm_y[:] == 1]
    y_2 = svr_y[svm_y[:] == 2]
    y_3 = svr_y[svm_y[:] == 3]
    y_4 = svr_y[svm_y[:] == 4]

    # do svr
    svr_1 = SVR(kernel='rbf', C=10)
    svr_1.fit(X_1, y_1)

    svr_2 = SVR(kernel='rbf', C=10)
    svr_2.fit(X_2, y_2)

    svr_3 = SVR(kernel='rbf', C=10)
    svr_3.fit(X_3, y_3)

    svr_4 = SVR(kernel='rbf', C=10)
    svr_4.fit(X_4, y_4)
    # print(model_rbf)

    # pickle model
    with open('svm_0.pkl', 'wb') as f:
        pickle.dump(svm_0, f)
    with open('svr_1.pkl', 'wb') as f:
        pickle.dump(svr_1, f)
    with open('svr_2.pkl', 'wb') as f:
        pickle.dump(svr_2, f)
    with open('svr_3.pkl', 'wb') as f:
        pickle.dump(svr_3, f)
    with open('svr_4.pkl', 'wb') as f:
        pickle.dump(svr_4, f)

    # with open('pcamodel.pkl', 'wb') as f:
    #     pickle.dump(pca_6, f)

    ### predict ###
    evaluate(X, y)

    # see difference
    # y_rbf = np.transpose(y_rbf)
    # deviation(svm_y, y_rbf)


def evaluate(X, y):
    index = [0, 1, 2, 3]
    # load files
    # decomp = jb.load('pcamodel.pkl')
    svm_0 = jb.load('svm_0.pkl')

    svr_1 = jb.load('svr_1.pkl')
    svr_2 = jb.load('svr_2.pkl')
    svr_3 = jb.load('svr_3.pkl')
    svr_4 = jb.load('svr_4.pkl')

    # labels
    svm_y = y[:, -1]
    svr_y = y[:, -2]

    # pca
    # X = decomp.fit_transform(X)

    # svm & svr
    pred_y = svm_0.predict(X)
    prob_y = svm_0.predict_proba(X)

    fin_y = np.zeros(svm_y.shape)
    for i in range(pred_y.shape[0]):
        grade = 0
        weight = 0

        prob = prob_y[i, :]
        max_prob = nlargest(2, index, key=lambda j: prob[j])
        dat = X[i, :].reshape(1, X.shape[1])
        # print(max_prob)
        # print(prob)

        for k in max_prob:
            if k == 0:
                grade += svr_1.predict(dat) * prob[k]
                weight += prob[k]
                # print(grade)
            elif k == 1:
                grade += svr_2.predict(dat) * prob[k]
                weight += prob[k]
                # print(grade)
            elif k == 2:
                grade += svr_3.predict(dat) * prob[k]
                weight += prob[k]
                # print(grade)
            elif k == 3:
                grade += svr_4.predict(dat) * prob[k]
                weight += prob[k]
                # print(grade)
            else:
                print('no class label assigned')
                # print(k)

        grade *= (1 / weight)
        # print('Predicted grade: ', grade)
        # print('Actual: ', svr_y[i])

        fin_y[i] = grade
    # fin_y = np.asarray(fin_y)
    # print(fin_y.shape)
    # print(svm_y.shape)

    # write to file
    svr_y = svr_y.reshape(svr_y.shape[0], 1)
    fin_y = fin_y.reshape(fin_y.shape[0], 1)
    svm_y = svm_y.reshape(svm_y.shape[0], 1)
    temp = np.concatenate((fin_y, svr_y, svm_y), axis=1)
    np.savetxt('results.txt', temp)
    np.save('results.npy', temp)

    # error rate
    print('SVM predictions:')
    deviation(svm_y, pred_y)
    print('SVR predictions:')
    deviation(fin_y, svr_y)


def test(X, y):
    model = jb.load('rbfmodel.pkl')
    decomp = jb.load('pcamodel.pkl')

    X = decomp.fit_transform(X)
    y_pred = model.predict(X)
    print(y_pred)
    print(y)

    deviation(y, y_pred)
    plotdat(X, X[:, 5])


def deviation(y, y_pred):
    diff = np.absolute(np.subtract(y, y_pred))
    sigma = np.std(diff)
    mean = np.mean(diff)
    r2 = r2_score(y, y_pred)

    # print out mean and st. dev
    print('Mean Square Root Error (MSRE): ', mean)
    print('Root Mean Square Deviation (RMSD): %f' % sigma)
    print('Coefficient of Determination (R2): ', r2)

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
print('Data loaded..')

# mix data  0 - datanumber, 7 - label
dummy = np.arange(data_num).reshape((data_num, 1))
dummy = np.concatenate((dummy, data), axis=1)

# ##################### separate to 4 label bins
temp = np.zeros((dummy.shape[0], 1))
temp[dummy[:, 7] < 0.25] = 1
temp[(dummy[:, 7] >= 0.25) & (dummy[:, 7] < 0.5)] = 2
temp[(dummy[:, 7] >= 0.5) & (dummy[:, 7] < 0.75)] = 3
temp[dummy[:, 7] >= 0.75] = 4

dummy = np.concatenate((dummy, temp), axis=1)
dummy = np.random.permutation(dummy)
# X = new_dummy[:, 0:7]
# y = new_dummy[:, 7]
#############################

# separate data
X = dummy[:, 1:-2]  # data num at[0]
y = dummy[:, -2:]  # last two columns

train_num = np.int(np.ceil(0.7 * data_num))
train_X = X[0:train_num, :]
train_y = y[0:train_num, :]

test_X = X[train_num:, :]
test_y = y[train_num:]

print('Starting learning algorithm..')
learn(train_X, train_y)
# test(test_X, test_y)
print('Starting testing..')
evaluate(test_X, test_y)
# plot
# plotdat(train_X, train_y)
# plotdat(test_X, test_y)

np.savetxt('testind.txt', dummy[train_num:, 0])
