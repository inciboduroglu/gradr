import enchant
from procEssay import preproc as pr

d = enchant.Dict("en_US")

def check(essay):
    prep = pr.preproc(essay)

    essay_list = prep['essay_list']

    err = [word for word in essay_list if d.check(word)==False]
    sug = [d.suggest(word) for word in err]

    return [err, sug]