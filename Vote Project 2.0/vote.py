#!/usr/bin/python
print 'Content-Type: text/html\n'
print ''
import cgi,cgitb
cgitb.enable()

form = cgi.FieldStorage()

page = '<!DOCTYPE HTML><html><head><title>Form Lab</title><link type="text/css" rel="stylesheet" href="style.css"/></head><body bgcolor = "#1B67E0">'

r = open('registered.txt', 'r')

v = open('voted.txt', 'r')
vot = v.read().split(',')
v.close()

f = open('results.txt','r')
res = f.read().split('\n')
f.close()

def out():
    username = form['username'].value
    pswd = form['pswd'].value
    subject = form['subject'].value
    planet = form['planet'].value
    utensil = form['utensil'].value

    if subject == 'Math':
        res[1] = (res[1][:-1] + str(int(res[1][-1]) + 1))
    elif subject == 'Science':
        res[2] = (res[2][:-1] + str(int(res[2][-1]) + 1))
    elif subject == 'English':
        res[3] = (res[3][:-1] + str(int(res[3][-1]) + 1))
    elif subject == 'History':
        res[4] = (res[4][:-1] + str(int(res[4][-1]) + 1))
    else:
        res[5] = (res[5][:-1] + str(int(res[5][-1]) + 1))

    if planet == 'Sun':
        res[8] = (res[8][:-1] + str(int(res[8][-1]) + 1))
    elif planet == 'Nile':
        res[9] = (res[9][:-1] + str(int(res[9][-1]) + 1))
    elif planet == 'Moon':
        res[10] = (res[10][:-1] + str(int(res[10][-1]) + 1))
    elif planet == 'Zimbabwe':
        res[11] = (res[11][:-1] + str(int(res[11][-1]) + 1))
    else:
        res[12] = (res[12][:-1] + str(int(res[12][-1]) + 1))

    if utensil == 'Tongs':
        res[15] = (res[15][:-1] + str(int(res[15][-1]) + 1))
    elif utensil == 'Whisk':
        res[16] = (res[16][:-1] + str(int(res[16][-1]) + 1))
    elif utensil == 'Ladle':
        res[17] = (res[17][:-1] + str(int(res[17][-1]) + 1))
    elif utensil == 'Spork':
        res[18] = (res[18][:-1] + str(int(res[18][-1]) + 1))
    else:
        res[19] = (res[19][:-1] + str(int(res[19][-1]) + 1))

    resX = '\n'.join(res)
    nr = open('results.txt','w')
    nr.write(resX)
    nr.close()
    final = open('results.txt','r')
    nrX = final.read()
    final.close()
    return nrX
    

def register():
    b = r.read().split('\n')
    username = form['username'].value
    pswd = form['pswd'].value
    for i in b:
        if username in i.split(':'):
            return 'Username already taken, please enter a different username.<br>'
    r.close()
    a = open('registered.txt','a')
    a.write(username + ':' + pswd + '\n')
    a.close()
    return 'Thank you for registering, you may now go back and <a href="http://149.89.161.100/~isaac.gluck/Vote%20Project%202.0/VoteX.html"> vote!</a><br>'

def vote():
    b = r.read().split('\n')
    r.close()
    username = form['username'].value
    pswd = form['pswd'].value
    subject = form['subject'].value
    planet = form['planet'].value
    utensil = form['utensil'].value
    for i in b:
        if username in i.split(':'):
            if username in vot:
                return 'This username has already been used to vote. Sorry, try <a href="http://149.89.161.100/~isaac.gluck/Vote%20Project%202.0/VoteX.html"> again?</a><br>'
            v.close()
            k = open('voted.txt','a')
            k.write(username + ',')
            k.close()
            return out()
    return 'Sorry, you are not registered. Please go back, register, than try again.<br>'
        
        
if 'register' in form:
    page += register()

if 'vote' in form:
    page += vote()

page += '<hr><br><a href="http://149.89.161.100/~isaac.gluck/Profile/Profile.html" text-decoration="none"> Go on home.</a></body></html>'

print page
