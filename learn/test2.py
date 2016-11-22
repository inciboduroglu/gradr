import nltk
from nltk.probability import FreqDist
import xlrd
import enchant
import numpy as np
from tempfile import TemporaryFile

# create file
outfile = TemporaryFile()

# create dictionary
d = enchant.Dict("en_US")
data_num = 10
feat_num = 4

def lexical_diversity(text):
    """Call with list of essay"""
    return len(set(text)) / len(text)


def word_cnt(text):
    """Call with list of essay"""
    text = [word for word in text if word.isalnum()]  # take alphanumerical
    return len(text)


def long_wrd_cnt(text):  # words longer than 6 characters
    """Call with list of essay"""
    text = [word for word in text if word.isalpha()]  # take alpha
    return len([word for word in text if len(word) > 6])


def spell_err_check(text):
    text = [word for word in text if word.isalpha()]  # take alpha
    incor = [word for word in text if d.check(word) == False]
    return len(incor)


# load excel sheet
workbook = xlrd.open_workbook('training_set_rel3.xlsx', on_demand = True)
sheet = workbook.sheet_by_index(0)

# get rid of numbers and punctuation
#essay_set = sorted(set(word.lower() for word in essay_list if word.isalpha()))

#print(essay_set)

feat_mtx = np.zeros((data_num, feat_num), dtype=np.double)

for i in range(data_num):
    essay = sheet.cell(i+1, 2).value
    essay_list = essay.split()  # split to have list

    essay_list = [word.lower() for word in essay_list if word.isalpha()]

    # print('word cnt:', word_cnt(essay_list))
    # print('lexical diversity of essay:', lexical_diversity(essay_list))
    # print('long word cnt:', long_wrd_cnt(essay_list))
    # print('spell error cnt:', spell_err_check(essay_list))

    feat_mtx[i, 0] = word_cnt(essay_list)
    feat_mtx[i, 1] = long_wrd_cnt(essay_list)
    feat_mtx[i, 2] = lexical_diversity(essay_list)
    feat_mtx[i, 3] = spell_err_check(essay_list)

# fdist = FreqDist(essay_list)
# print(fdist.most_common(10))
print(feat_mtx)

np.save('outfile.npy', feat_mtx)
