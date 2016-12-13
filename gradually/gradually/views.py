
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from gradually.grade import predict
import sys

def index(request):
    print(sys.path)
    return HttpResponseRedirect("/static/web/index.html")

def grade(request):
    essay_text = request.POST.get("essay")
    print(essay_text)
    #predict_result = predict.predict(essay_text)
    predict_result = predict.predict(essay_text)

    if isinstance(predict_result, float) or isinstance(predict_result, int):
        grade = predict_result
    else:
        grade = predict_result[0]

    print (grade)
    #"Nope. Not even going to bother analyzing that. Good luck. \
                     #<br> (actually I would but it does not work yet.)"
    return JsonResponse({'essay': essay_text,
                        'parrot': "<img src=http://cultofthepartyparrot.com/parrots/parrot.gif>",
                         'spell': spell,
                         'grade': grade
                         # "aundera - that <b>cunt</b> <br> also <b>dat</b> <i>non-escaped</i> output\
                         # <br> <img src=http://cultofthepartyparrot.com/parrots/parrot.gif> "
                        }, safe=False)

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