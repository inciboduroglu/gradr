from nltk.stem.snowball import SnowballStemmer
import enchant


def featext(prep_res):
    """Processes pre processing results
    Extracts data features for grading"""
    #print(prep_res)

    # define essay properties
    essay_list = prep_res['essay_list']
    essay_set = prep_res['essay_set']
    no_punc_list = prep_res['no_punc_list']
    low_list = prep_res['low_list']
    no_stop_list = prep_res['no_stop_list']
    gradr_no_stop_list = prep_res['gradr_no_stop_list']

    lex_div = lexical_diversity(essay_set, essay_list)
    w_cnt = word_cnt(low_list, 0)
    lng_w_cnt = word_cnt(low_list, 6)
    spl = spell_err_check(low_list)
    dst_wrd_cnt = len(essay_set)
    stm_cnt = len(stem_(low_list))

    return {'lexical_div': lex_div, 'word_cnt': w_cnt, 'long_word_cnt': lng_w_cnt, 'spell_err_cnt': spl,
            'distinct_word_cnt': dst_wrd_cnt, 'stem_cnt': stm_cnt}


def lexical_diversity(essay_set, essay_list):
    """Calculates lexical diversity
    Lexical diversity is a measure of how many different words that are used in a text,
    while lexical density provides a measure of the proportion of lexical items
    (i.e. nouns, verbs, adjectives and some adverbs) in the text."""
    return len(essay_set) / len(essay_list)


def word_cnt(text, num):
    """Call with list of essay. For all words give num=0
    Doesn't count numerics"""
    text = [word for word in text if word.isalpha()]  # take alpha
    return len([word for word in text if len(word) > num])


def spell_err_check(text):
    """Checks spelling of essay ad returns number of misspelled words."""
    dct = enchant.Dict("en_US")

    text = [word for word in text if word.isalpha()]  # take alpha
    incor = [word for word in text if dct.check(word) == False]
    return len(incor)


def stem_(text):
    stemmer = SnowballStemmer("english")
    return [stemmer.stem(word) for word in text]
