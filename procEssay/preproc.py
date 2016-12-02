import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


def preproc(essay):
    """delete punctuation
    to lowercase
    make word list
    make word set
    delete stop words"""
    # stopword list
    gradr_stp = ['a', 'about', 'above', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all',
                 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst',
                 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway',
                 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes',
                 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides',
                 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant',
                 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due',
                 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough',
                 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few',
                 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty',
                 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt',
                 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers',
                 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'ie', 'if', 'in', 'inc',
                 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly',
                 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine',
                 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely',
                 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor',
                 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto',
                 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part',
                 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming',
                 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six',
                 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere',
                 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves',
                 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these',
                 'they', 'thickv', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout',
                 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two',
                 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what',
                 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein',
                 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole',
                 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your',
                 'yours', 'yourself', 'yourselves', 'the']

    # split to make list of the words
    essay_list = essay.split()

    # delete punctuation
    punc_tokenizer = RegexpTokenizer(r'\w+')
    no_punc_list = punc_tokenizer.tokenize(essay)

    # lowercase everything
    low_list = [word.lower() for word in no_punc_list]

    # word set
    essay_set = set(low_list)

    # delete stop words from lowercase no punctuation essay list
    no_stop_list = [word for word in low_list if word not in stopwords.words('english')]

    # a more comprehensive stopword deletion
    gradr_no_stop_list = [word for word in no_stop_list if word not in gradr_stp]

    # print block
    # print(essay_list)
    # print(no_punc_list)
    # print(low_list)
    # print(essay_list)
    # print(no_stop_list)
    # print(gradr_no_stop_list)

    return {'essay_list': essay_list, 'essay_set': essay_set, 'no_punc_list': no_punc_list, 'low_list': low_list,
            'no_stop_list': no_stop_list, 'gradr_no_stop_list': gradr_no_stop_list}
