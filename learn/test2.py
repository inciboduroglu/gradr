import nltk
from nltk.probability import FreqDist
import xlrd


def lexical_diversity(text):
    return len(set(text)) / len(text)

# load excel sheet
workbook = xlrd.open_workbook('training_set_rel3.xlsx', on_demand = True)
sheet = workbook.sheet_by_index(0)
essay = sheet.cell(1, 2).value
essay_list = essay.split()   # split to have list

# get rid of numbers and punctuation
essay_set = sorted(set(word.lower() for word in essay_list if word.isalpha()))

print(essay_set)

print('lexical diversity of essay', lexical_diversity(essay_list))

fdist = FreqDist(essay_list)
print(fdist.most_common(10))