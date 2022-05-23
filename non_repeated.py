from nltk.corpus import words
import random
from collections import defaultdict
import os
import subprocess
import csv


def input_schema_generator():
    for nameLength in range(2,11):
        a = words.words()
        for ncl in range(2,7):
            for nop in range(0,16):
                    fileName = 'evaluation/non_repeated_input_schema/name_length_'+str(nameLength)+'_nop_'+str(nop)+'_ncl_'+str(ncl)+'.txt'
                    f = open(fileName, "w")
                    f.write("netCert: Alice/Key")
                    f.write('\n')

                    dic = defaultdict(int)
                    temp = []

                    for i in range(0,nameLength-1):
                        word = random.choice([x for x in a if (len(x) == ncl and x not in dic)])
                        dic[word] += 1
                        temp.append(word)
                    #print(temp)

                    for i in range(0,nop+1):
                        pubName = random.choice([x for x in a if (len(x) == ncl and x not in dic)])
                        dic[pubName] += 1
                        pub = '#' + pubName + ': '
                        #for t in temp:
                            #pub += t + '/'
                        for t in range(0,nameLength):
                            component = random.choice([x for x in a if (len(x) == ncl and x not in dic)])
                            pub += component
                            dic[component] += 1
                            if(t != nameLength-1):
                                pub+= '/'
                        pub += '\n'
            

                        f.write(pub)
                        
                        tmpWord = random.choice([x for x in a if (len(x) == ncl and x not in dic)])
                        f.write(tmpWord + ': #' + pubName + ' <= netCert')
                        f.write('\n')


def schema_compile():
    with open('non_repeated_result.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Schema_Type', 'Name_Length', 'Name_Component_Length', 'Number_of_Publications', 'Schema_Size'])
        for nameLength in range(2,9):
            for ncl in range(2,7):
                for nop in range(0,15):
                    tok = nop * (nameLength+2) + 3
                    if(tok > 128):
                        writer.writerow(['Vans',str(nameLength),str(ncl),str(nop+1),'Cannot determine'])
                    else:
                        input_file = 'evaluation/non_repeated_input_schema/name_length_'+str(nameLength)+'_nop_'+str(nop)+'_ncl_'+str(ncl)+'.txt'
                        out_file = 'name_length_'+str(nameLength)+'_nop_'+str(nop)+'_ncl_'+str(ncl)+'.scm'
                        try:
                            cmd = "./schemaCompile -o " + ' evaluation/non_repeated_output_schema/'+out_file +' '+ input_file
                            os.system(cmd)
                            size = os.path.getsize('evaluation/non_repeated_output_schema/'+out_file)
                            writer.writerow(['Vans',str(nameLength),str(ncl),str(nop+1),str(size)])
                        except:
                            writer.writerow(['Vans',str(nameLength),str(ncl),str(nop+1),'Cannot determine'])
                    
                for nop in range(0,15):
                    try:
                        input_file = 'evaluation/non_repeated_input_schema/name_length_'+str(nameLength)+'_nop_'+str(nop)+'_ncl_'+str(ncl)+'.txt'
                        out_file = 'name_length_'+str(nameLength)+'_nop_'+str(nop)+'_ncl_'+str(ncl)+'.scm'
                        cmd = "python3 TSP.py " + input_file +' evaluation/non_repeated_simplified/'+out_file
                        os.system(cmd)
                        print(cmd)
                        size = os.path.getsize('evaluation/non_repeated_simplified/'+out_file)
                        writer.writerow(['Simplified',str(nameLength),str(ncl),str(nop+1),str(size)])
                    except:
                        writer.writerow(['Simplified',str(nameLength),str(ncl),str(nop+1),'Cannot determine'])
                  
                for nop in range(0,15):
                    try:
                        input_file = 'evaluation/non_repeated_input_schema/name_length_'+str(nameLength)+'_nop_'+str(nop)+'_ncl_'+str(ncl)+'.txt'
                        out_file = 'name_length_'+str(nameLength)+'_nop_'+str(nop)+'_ncl_'+str(ncl)+'.scm'
                        cmd = "python3 no_compression.py "+ input_file + ' evaluation/non_repeated_no_compression/'+out_file
                        os.system(cmd)
                        size = os.path.getsize('evaluation/non_repeated_no_compression/'+out_file)
                        writer.writerow(['NC',str(nameLength),str(ncl),str(nop+1), str(size)])
                    except:
                        writer.writerow(['NC',str(nameLength),str(ncl),str(nop+1),'Cannot determine'])
            
#input_schema_generator()
schema_compile()
    


