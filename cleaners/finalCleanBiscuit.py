import os
import re
infile = open(os.getcwd()+'/Data/clean_biscuit.txt','r')
outfile = open(os.getcwd()+'/Data/really_clean_biscuit.txt','w')
cleanr = re.compile('<.*?>')

text = infile.readlines()

for line in text:
    cleantext = re.sub(cleanr, '', line)
    outfile.write(cleantext)

infile.close()
outfile.close()
