from nltk.corpus import words
import random
from collections import defaultdict
import os
import subprocess


#pub = '#iotPub: '

a = words.words()
nameLength = 8

for k in range(0,16):

    fileName = 'input_schema/exp1_'+str(k)+'.txt'
    f = open(fileName, "w")
    f.write("netCert: Alice/Key")
    f.write('\n')

    dic = defaultdict(int)
    temp = []

    for i in range(0,nameLength-1):
        word = random.choice([x for x in a if (len(x) == 4 and x not in dic)])
        dic[word] += 1
        temp.append(word)
    print(temp)

    for i in range(0,k+1):
        pubName = random.choice([x for x in a if (len(x) == 4 and x not in dic)])
        dic[pubName] += 1
        pub = '#' + pubName + ': '
        for t in temp:
            pub += t + '/'
        component = random.choice([x for x in a if (len(x) == 4 and x not in dic)])
        pub += component
        pub += '\n'
        dic[component] += 1

        f.write(pub)
        
        tmpWord = random.choice([x for x in a if (len(x) == 4 and x not in dic)])
        f.write(tmpWord + ': #' + pubName + ' <= netCert')
        f.write('\n')

    #os.system(cmd)
    #subprocess.call([cmd])
'''for i in range(0,15):
    cmd = "./schemaCompile -o " + "output_schema/exp1_"+str(i)+".scm " + "input_schema/exp1_" + str(i)+".txt"
    os.system(cmd)'''
    
for i in range(0,15):
    #print(cmd)
    cmd = "python3 TSP.py input_schema/exp1_" + str(i)+".txt " + "simplified/exp1_" + str(i)+ ".scm"
    os.system(cmd)
    

