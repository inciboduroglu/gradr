from tempfile import TemporaryFile
import numpy as np
import xlrd
from procEssay import preproc as pr
from procEssay import featExt as fe

# Creates training data features
# create file
outfile = TemporaryFile()

# load excel sheet
workbook = xlrd.open_workbook('../data/training_set_rel3.xlsx', on_demand=True)
sheet = workbook.sheet_by_index(0)

# create training matrix
data_num = 12978
data_10 = 7821
feat_num = 6 + 1  # 6 features one label
feat_mtx = np.zeros((data_10, feat_num), dtype=np.double)

rubric_range = [[2, 12], [1, 6], [0, 3], [0, 3], [0, 4], [0, 4], [0, 30], [0, 60]]
i = 0
for j in range(data_num):
    # get essay from dataset
    set = sheet.cell(j + 1, 1).value
    set = int(set)
    print('set: ')
    print(set)
    if set in [2, 3, 4, 6, 8]:
        essay = sheet.cell(j + 1, 2).value
        label = sheet.cell(j + 1, 6).value
        print(label)

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

        # calculate new label
        xmin = rubric_range[set - 1][0]
        xmax = rubric_range[set - 1][1]
        new_label = (label - xmin) / (xmax - xmin)
        feat_mtx[i, 6] = new_label
        # data[i, data.shape[1] - 1] = new_label

        i += 1
        print(new_label)

# print(i)
print(feat_mtx)
np.savetxt('traindata.txt', feat_mtx)
np.save('traindata.npy', feat_mtx)
