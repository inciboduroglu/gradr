
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from gradually.grade import predict
from gradually.grade import grammar
import sys
import ast

def index(request):
    print(sys.path)
    return HttpResponseRedirect("/static/web/index.html")

def grade(request):
    essay_text = request.POST.get("essay")
    print(essay_text)
    #predict_result = predict.predict(essay_text)
    predict_result = predict.predict(essay_text)[0]
    print (predict_result)
    
    grammar_errors = grammar.grammar(essay_text)
    grammar_list = []
    correction_list = []
    for match in grammar_errors:
        m = match.msg
        c = match.replacements
        print(match)
        grammar_list.append(m)
        correction_list.append(c)
    grammar_list_j = json.dumps(grammar_list, default=obj_dict)
    correction_list_j = json.dumps(correction_list, default=obj_dict)
    
    words = []
    apperances = {}
    for match in grammar_errors:
        word = []
        for letter in range(match.fromx, match.tox):
            word.append(essay_text[letter])
        apperances[match.fromx] = match.tox
        words.append(word)
        word = []
    
    i = 0
    for word in words:
        words[i] = ''.join(map(str,words[i]))
        i = i+1
    print (words)
    wrong_words = json.dumps(words, default=obj_dict)
    dict_of_apperances = json.dumps(apperances, default=obj_dict)
    print ()
    dict_of_apperances = dict_of_apperances.replace("\"", " ")
    dict_of_apperances = dict_of_apperances.replace(" ", "")
    print(type(dict_of_apperances))
    print (dict_of_apperances)
    print ()
    #testing 1 2 3
    #for match in grammar_errors:
    #    print(match)
    
    #"Nope. Not even going to bother analyzing that. Good luck. \
                     #<br> (actually I would but it does not work yet.)"
    return JsonResponse({'essay'     			: essay_text,
                         'spell'     			: "<img src=http://cultofthepartyparrot.com/parrots/parrot.gif>",
                         'grade'     			: predict_result,
						 'grammar'   			: grammar_list_j,
						 'correction'			: correction_list_j,
						 'wrong_words'			: wrong_words,
						 'dict_of_apperances'	: dict_of_apperances
                         # "aundera - that <b>cunt</b> <br> also <b>dat</b> <i>non-escaped</i> output\
                         # <br> <img src=http://cultofthepartyparrot.com/parrots/parrot.gif> "
                        }, safe=False)

def obj_dict(obj):
    return obj.__dict__
						
def gradefile(request):
    file_contents = str(request.FILES.get("fileToUpload").read(), "utf-8")
    print(file_contents)
    return JsonResponse({"fcontent": file_contents})


''' CHANGES FROM ENCODER:
    - Going to homepage (localhost:8000) redirects to index.html.
    - On index.html, instead of getting the result from an array first, directly grab it from a dict
    - Stop getting jQuery from Google. Poor Google.
    
    - When importing something you wrote, use gradually.somethingyouwrote, it's the main package now.
        + Or whatever you decide to name it I dunno how would I
        + Adi degistirirsen predict.py'de de degistir bak unutma
    
    - Şincik print'le basiyoduk ya? He artik basmiyoz. Onu kullan hop terminale yazaya.
      Debug içün kullanabilün. 
        + Return your results in either a HttpResponse() or a JsonResponse() object.

    PROBLEMOS:
    - DOESN'T WORK! Ogretirken 4 vermisin de simdi 6 istemisin bilmem ne diye miziklaniyor, anlamiyom.
    
'''