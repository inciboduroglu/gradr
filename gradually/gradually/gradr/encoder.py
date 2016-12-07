#!/usr/local/bin/python3
import cgi
import cgitb
cgitb.enable()
#import numpy as np
import sys, os

print ("Content-Type: text/plain")
print()
open("/Library/WebServer/CGI-Executables/gradr/learn/rbfmodel.pkl")
# sys.path.append('/Users/inciboduroglu/Code/gradr/')
sys.path.append('/Library/WebServer/CGI-Executables/gradr/')
from grade import predict
# print(sys.version)

form = cgi.FieldStorage()
data = form.getvalue("essay")
data = "gkfsl fdkla reio"
# write data
predict.predict(data)
data = "something"
spell = [0]
print ("[{\"essay\" : \"%s\" , \"spell\" : %s}]" % (data, spell))
#print "{\"spell\" : \"%s\"}" % spell
