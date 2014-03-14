#!/usr/bin/python
print 'Content-Type: text/html'
print ''

head='''<!DOCTYPE HTML>
<html>
<head>
   <title>DATA</title>
</head>
<body bgcolor = "#9199FF">
<h1> Team iSac</h1>
<h1> Gluck, Isaac</h1>
<h1> MKS22 - Mr. Jaishankar</h1>
<h1> Period-9</h1>
<h2> DATASET: Carbon Dioxide Information Analysis Center (CDIAC) Data</h2>
<h2> DATA SOURCE: </h2> <a href="http://datahub.io/dataset/cdiac"> CDIAC </a>
<h2> Chosen because I feel like the environment is a very important issue and something that I'm extremely interested in, especially with what is happening nowadays.</h2>
<p> See the analysis: <a href = "Analysis.py">Analysis</a></p>
<p> Go home: <a href = "http://marge.stuy.edu/~isaac.gluck/Profile/Profile.html"><img src="Home.jpeg" height="50" width="50"/></a></p>
<table border = "1"; cellpadding = "5">
'''

f = open('data1.csv', 'r')

def makeBody():
     line = f.readline()
     while line:
          print '<tr>'
          for i in line.split(',')[:-1]:
               print ('<td bgcolor = "#EBB6FA">' + str(i) + '</td>')
          print '</tr>'
          line = f.readline()


foot= '''</body>
</html>'''

print head
makeBody()
print '</table>'
print '<img src="data.jpg" height = "1000" width = "1000">'
print foot

f.close()
