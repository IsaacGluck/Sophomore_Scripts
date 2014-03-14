#!/usr/bin/python
print 'Content-Type: text/html'
print ''

head ='''<!DOCTYPE HTML>
<html>
<head>
   <title>ANALYSIS</title>
</head>
<body bgcolor = "#9199FF">
<h1 align = "center">Team iSac</h1>
<h1 align = "center">Gluck, Isaac</h1>
<h1 align = "center">MKS22 - Mr. Jaishankar</h1>
<h1 align = "center">Period-9</h1>
<h3>What I attempted to do here was to examine human kind's carbon emissions and see/validate whether we are putting more C into the atmosphere faster. I first made a table of the amount of change between every two years. One of the major difficulties I had was numerous conversions of data from "str" form to "int" form. I also had difficulties in printing the year ranges as one box in the table even though they came from seperate boxes in the first data.</h3>

<h1 align = "center"> Conclusion: </h1>
<p>
The Analysis being done here is only on the first column of data after the date column in the data portion, it deals with the "Total carbon emissions from fossil-fuels (million metric tons of C)". What my analysis does is examine the amount of carbon emiisions between every two years. The first thing you see on this page is the table of the data that I extracted. I also graphed the data in excel and included it. Below the excel graph is a graph of the data from the table, each  "=" sign is a million metric tons of C and it is showing how much the emmissions went up (or down) every two years. What I have found is a known, but sad truth: Not only is there more C in the atmosphere thean there has ever been, we are putting it into the atmosphere faster. That is a very disturbing fact. Finally, I had a pretty tought problem with Filezilla. It wouldn't let me transfer any files to marge, when I would try the file would appear as an empty file on marge which was extremely aggravating. Finally, I figured it out. In my room, where I work, I have my own router that extends the signal of the main raouter in the living room. For some reason Filezilla does not like this extra jump. The solution to this problem was all too simple. All I had to do was work from the living room. Solved.</p>

<p>     I also have some POSSIBLE explanations for certain trends in the data:</p>
	<p>          The reason that C emissions are increasing, and increasing faster, is becasue of the industrial revolution.</p>
	<p>          Around 1919 there was a large negative value because of the end of World War 1 and the decrease in military production.</p>
	<p>          In 1929-1930 there was also a very large negative number because of the Great Depression.</p>
	<p>          In 1939-1940 there was a large jump in C emissions becasue of the start of World War 2 and the increased military production.</p>
	<p>          In 1944-1945 there was another large negative number, the biggest so far, becasue of the end of World War 2 and the decrease in military production.</p>
	<p>          In 1974-1975 there was a negative number becasue of the OPEC oil embargo.</p>
	<p>          In 1979-1982 there are all negative numbers because of the U.S. and European economic recession and the small oil crisis resulting from the Iranian Revolution.</p>
	<p>          In 1991-1993 there were all negative numbers again because of the collapse of the Soviet Union and their heavy industry.</p>
	<p>          In 1997-1999 there were negative numbers again because of the Asian financial crisis.</p>
	<p>          In 2002-2004 there was a giant increase because of the beginning of the U.S. war on terror and invasions of Afganhistan and Iraq.</p>
<br>
<br>
<p> See the data: <a href = "http://marge.stuy.edu/~isaac.gluck/Analysis/data.py">Data</a></p>
<p> Go home: <a href = "http://marge.stuy.edu/~isaac.gluck/Profile/Profile.html"><img src="Home.jpeg" height="50" width="50"/></a></p>
<table border = "1"; cellpadding = "5"; align="center">'''

k = open('data1.csv', 'r')
f = open('data2.csv', 'w')
L = []
L2 = []
L3 = []
Lyear = []

def reading():
    line = k.readline()
    line = k.readline()
    while line:
        L.append(line.split(',')[1])
        Lyear.append(line.split(',')[0])
        line = k.readline()
    k.close()

def writing():
    f.write('Year Interval' + ',' + 'Amount of change between every two years' + '\n')
    for i in range(1,len(Lyear)):
        L2.append(int(L[i]) - int(L[i-1]))
        L3.append(str(Lyear[i-1]) + '-' + str(Lyear[i]))
        f.write(Lyear[i-1] + '-' + Lyear[i] + ',' + str(int(L[i]) - int(L[i-1])) + '\n')
    f.close()

reading()
writing()

def makeBody():
    w = open('data2.csv', 'r')
    line = w.readline()
    while line:
        print '<tr>'
        for i in line.split(','):
            print ('<td bgcolor = "#EBB6FA">' + str(i) + '</td>')
        print '</tr>'
        line = w.readline()
    w.close()


foot= '''
</body>
</html>'''




L2 = L2[1:]
def graph():
    for i in range(0,len(L2)):
        if L2[i] >= 0:
            print '<p>' + L3[i] + ': ' + (L2[i] * '=') + '</p>'
        else:
            print '<p>' + L3[i] + ': negative' + '</p>'

    
print head
makeBody()
print '</table>'
print '<img src="Analysis.jpg" height = "1000" width = "1000">'
graph()
print foot
