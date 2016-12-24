import numpy as np
from procEssay import preproc as pr
from procEssay import featExt as fe
from sklearn.externals import joblib as jb
from sklearn.svm import SVR
import pickle
from heapq import nlargest


def evaluate(X):
    index = [0, 1, 2, 3]
    # load files
    # decomp = jb.load('pcamodel.pkl')
    # with open('/Users/inciboduroglu/Code/gradr/learn/rbfmodel.pkl', 'rb') as f:
    svm_0 = jb.load('../learn/svm_0.pkl')

    svr_1 = jb.load('../learn/svr_1.pkl')
    svr_2 = jb.load('../learn/svr_2.pkl')
    svr_3 = jb.load('../learn/svr_3.pkl')
    svr_4 = jb.load('../learn/svr_4.pkl')

    # svm & svr
    pred_y = svm_0.predict(X)
    prob_y = svm_0.predict_proba(X)

    grade = 0
    weight = 0

    prob = prob_y[0,:]
    max_prob = nlargest(2, index, key=lambda j: prob[j])
    dat = X.reshape(1, X.shape[1])
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

    return grade


def predict(essay):
    # preproc returns {'essay_list': essay_list, 'essay_set': essay_set, 'no_punc_list': no_punc_list, 'low_list': low_
    # list, 'no_stop_list': no_stop_list, 'gradr_no_stop_list': gradr_no_stop_list}
    prep_res = pr.preproc(essay)

    # featext returns {'lexical_div': lex_div, 'word_cnt': w_cnt, 'long_word_cnt': lng_w_cnt, 'spell_err_cnt': spl,
    # 'distinct_word_cnt': dst_wrd_cnt, 'stem_cnt': stm_cnt}
    feat = fe.featext(prep_res)

    feat_mtx = np.zeros((1, 6))
    feat_mtx[0, 0] = feat['word_cnt']
    feat_mtx[0, 1] = feat['long_word_cnt']
    feat_mtx[0, 2] = feat['spell_err_cnt']
    feat_mtx[0, 3] = feat['lexical_div']
    feat_mtx[0, 4] = feat['distinct_word_cnt']
    feat_mtx[0, 5] = feat['stem_cnt']

    feat_mtx.reshape((1, 6))
    print('feature matrix: ')
    print(feat_mtx)

    # grade = model.predict(feat_mtx.reshape((1, 6)))
    grade = evaluate(feat_mtx)
    print(grade * 100)

    if feat['spell_err_cnt'] / feat['word_cnt'] > 0.3:
        return 0
    else:
        return grade * 100

predict('Dear local newspaper, I think effects computers have on people are great learning skills/affects because they'
        ' give us time to chat with friends/new people, helps us learn about the globe(astronomy) and keeps us out of '
        'troble! Thing about! Dont you think so? How would you feel if your teenager is always on the phone with '
        'friends! Do you ever time to chat with your friends or buisness partner about things. Well now - there\'s a '
        'new way to chat the computer, theirs plenty of sites on the internet to do so: @ORGANIZATION1, @ORGANIZATION2,'
        ' @CAPS1, facebook, myspace ect. Just think now while your setting up meeting with your boss on the computer, '
        'your teenager is having fun on the phone not rushing to get off cause you want to use it. How did you learn '
        'about other countrys/states outside of yours? Well I have by computer/internet, it\'s a new way to learn '
        'about what going on in our time! You might think your child spends a lot of time on the computer, but ask '
        'them so question about the economy, sea floor spreading or even about the @DATE1\'s you\'ll be surprise at '
        'how much he/she knows. Believe it or not the computer is much interesting then in class all day reading out '
        'of books. If your child is home on your computer or at a local library, it\'s better than being out with '
        'friends being fresh, or being perpressured to doing something they know isnt right. You might not know where '
        'your child is, @CAPS2 forbidde in a hospital bed because of a drive-by. Rather than your child on the computer'
        ' learning, chatting or just playing games, safe and sound in your home or community place. Now I hope you have'
        ' reached a point to understand and agree with me, because computers can have great effects on you or child '
        'because it gives us time to chat with friends/new people, helps us learn about the globe and believe or not '
        'keeps us out of troble. Thank you for listening.')
