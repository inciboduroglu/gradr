#!/usr/local/bin/python3
import cgi
import cgitb
cgitb.enable()
import numpy as np
import sys, os

print ("Content-Type: text/plain")
print ()

# sys.path.append('/Users/inciboduroglu/Code/gradr/')
sys.path.append('/Library/WebServer/CGI-Executables/gradr/')
from grade import predict as pr
# print(sys.version)

form = cgi.FieldStorage()
data = form.getvalue("essay")

# write data
grade = pr.predict(data)
spell = list(np.zeros(2))
print ("[{\"essay\" : \"%s\" , \"spell\" : %s, \"grade\" : %d}]" % (data, spell, grade))
