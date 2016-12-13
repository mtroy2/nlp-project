import os
import re
infile = open(os.getcwd()+'/Data/clean_onion.txt','r')
outfile = open(os.getcwd()+'/Data/really_clean_onion.txt','w')
cleanr = re.compile('<.*?>')

text = infile.readlines()

for line in text:
    line = line.rstrip()
    cleantext = re.sub(cleanr, '', line)
    if len(line) >0:
        outfile.write(cleantext)
        outfile.write('\n')
infile.close()
outfile.close()
