#!/usr/bin/python
print 'Content-Type: text/html'
print ''

head='''<!DOCTYPE HTML>
<html>
<head>
   <title>My Page</title>
</head>
<body bgcolor = "blue">
<p>Team iSac</p>
<p>Gluck, Isaac</p>
<p>MKS22 - Mr. Jaishankar</p>
<p>Period-9</p> (xx is the period number)
<p>DATASET: _______</p>
<p>DATA SOURCE: _______</p>
<p>Chosen because</p>
<table border = "1"; cellpadding = "5"; >
'''

f = open('data1.csv', 'r')

def makeBody():
     line = f.readline()
     while line:
          print '<tr>'
          for i in line.split(',')[:-1]:
               print ('<td bgcolor = "purple">' + str(i) + '</td>')
          print '</tr>'
     line = f.readline()



foot= '''</table></body>
</html>'''

print head
makeBody()
print foot

f.close()
