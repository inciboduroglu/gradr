#!/usr/bin/python
import cgi
import cgitb
import numpy as np
cgitb.enable()

print "Content-Type: text/plain"
print
form = cgi.FieldStorage()
data = form.getvalue("essay")
data = "something"
spell = list(np.zeros(2))
print "[{\"essay\" : \"%s\" , \"spell\" : %s}]" % (data, spell)
#print "{\"spell\" : \"%s\"}" % spell
