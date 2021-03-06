import xlrd
import numpy as np
from gradually.procEssay import preproc as pr
from gradually.procEssay import featExt as fe
from tempfile import TemporaryFile

# Creates training data features

# create file
outfile = TemporaryFile()

# load excel sheet
workbook = xlrd.open_workbook('../data/training_set_rel3.xlsx', on_demand=True)
sheet = workbook.sheet_by_index(0)

# create training matrix
data_num = 12978
feat_num = 6 + 1  # 6 features one label
feat_mtx = np.zeros((data_num, feat_num), dtype=np.double)

for i in range(data_num):
    # get essay from dataset
    essay = sheet.cell(i + 1, 2).value
    label = sheet.cell(i + 1, 6).value

    # pre process and extract features
    essay = pr.preproc(essay)
    feat = fe.featext(essay)

    # {'lexical_div': lex_div, 'word_cnt': w_cnt, 'long_word_cnt': lng_w_cnt, 'spell_err_cnt': spl,
    #        'distinct_word_cnt': dst_wrd_cnt, 'stem_cnt': stm_cnt}

    feat_mtx[i, 0] = feat['word_cnt']
    feat_mtx[i, 1] = feat['long_word_cnt']
    feat_mtx[i, 2] = feat['spell_err_cnt']
    feat_mtx[i, 3] = feat['lexical_div']
    feat_mtx[i, 4] = feat['distinct_word_cnt']
    feat_mtx[i, 5] = feat['stem_cnt']
    feat_mtx[i, 6] = label

    print(i)

print(feat_mtx)
np.savetxt('traindata.txt', feat_mtx)
np.save('traindata.npy', feat_mtx)
