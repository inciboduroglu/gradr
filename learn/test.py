# load data from excel sheet
import xlrd
#import textmining
from nltk import MWETokenizer



def gradr_tokenize(essay):
    '''Tokenizes text'''

    tok_text = tokenizer.tokenize(essay.split())
    return tok_text


def replace_newline(essay):
    '''Replace character / with space
    :type essay: string
    '''
    return essay.replace("/", " ")


# load excel sheet
workbook = xlrd.open_workbook('training_set_rel3.xlsx', on_demand = True)
sheet = workbook.sheet_by_index(0)

# create tokenizer
tokenizer = MWETokenizer()

# get essay
essay = sheet.cell(1, 2).value
#print('essay', essay)

# tokenize with MWETokenizer
tok_essay = gradr_tokenize(essay)
#print(tok_essay)

# # Create document matrix
# tdm = textmining.TermDocumentMatrix()
# tdm.add_doc(essay)
# # write to file
# tdm.write_csv('matrix.csv', cutoff=1)

