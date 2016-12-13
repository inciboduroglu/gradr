import numpy as np
from gradually.procEssay import preproc as pr
from gradually.procEssay import featExt as fe
from sklearn.externals import joblib as jb
from sklearn.svm import SVR
import pickle


def predict(essay):
    with open('gradually/learn/rbfmodel.pkl', 'rb') as f:
        model = jb.load(f)

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

    feat_mtx.reshape((1,6))
    # print('feature matrix: ')
    # print(feat_mtx)

    grade = model.predict(feat_mtx)

    if feat['spell_err_cnt']/feat['word_cnt'] > 0.3:
        grade = 0
    
    return grade * 100

# predict('essay')
