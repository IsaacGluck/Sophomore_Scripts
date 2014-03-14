def average():
    d = open('data2.csv', 'r')
    line = d.readline()
    line = d.readline()
    L4 = []
    while line:
        line = line.split('\n')
        L4.append(line)
        line = d.readline()
    print L4
    d.close()

average()
        
