import os
import re
from bs4 import BeautifulSoup
clean_guardian = open(os.getcwd()+"/just_guard_text.txt",'w')

cleanr = re.compile('<[^p].*[^(\/p)]>')
for filename in os.listdir(os.getcwd()+"/guardian_content/"):
    
    try:
        path = os.getcwd() + '/guardian_content/'+ filename
        infile = open(path, 'r')
        text = infile.readlines()
        
        for line in text:
            soup = BeautifulSoup(line,'html.parser')
            rel_text = soup.text
            #line = re.sub(cleanr, '',line)
            #line = 'serious ' + line
            clean_guardian.write('serious ' + rel_text)
            #clean_guardian.write('\n')
   
    except UnicodeDecodeError:
        pass
clean_guardian.close()
