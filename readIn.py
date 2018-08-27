import re

def readFile(filename):
    #filename = 'data1.csv'
    
    
    lines = open(filename).read().split("\n")
    
    n = 0
    r = [0]
    b = [0]
    d = [0]
    g = [0]
    h = [0]
    s = [0]
    temp = []
    
    counter = 0
    
    for line in lines:
        if line.strip():
            line = line.rstrip()
            
            counter = counter + 1
            
            if(counter == 1):
                n = int(re.split('\s+', line)[1])
            elif(len(re.split('\s+', line)) >= 6 and re.match("^\d+?\.\d+?$", re.split('\s+', line)[5]) is not None):
                r.append(int(re.split('\s+', line)[2]))
                b.append(int(re.split('\s+', line)[3]))
                d.append(int(re.split('\s+', line)[4]))
                g.append(int(re.split('\s+', line)[5].replace('.00','')))
                h.append(int(re.split('\s+', line)[6].replace('.00','')))
            else:
                temp1 = re.split('\s+', line)[1:]
                temp1 = list(map(int, temp1))
                for item in temp1:
                    temp.append(item)
                if(len(temp) == n):
                    # 0 added at position zero, to allow index shifting (we need to start at i=1)
                    s.append([0]+temp)
                    temp = []
                
                
    #print(s)

    return n, r, b, d, g, h, s

#readFile('airland2.txt')