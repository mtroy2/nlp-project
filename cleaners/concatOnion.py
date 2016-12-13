import os

outPath = os.getcwd() + '/Data/clean_onion.txt'
outfile = open(outPath,'w')
for filename in os.listdir(os.getcwd()+"/Data/OnionRaw/"):
    
    try:
        path = os.getcwd() + '/Data/OnionRaw/'+ filename
        infile = open(path, 'r')
        text = infile.readlines()
        
        if len(text) == 0:
            infile.close()
            os.remove(path)
        elif len(text[1]) == 0:
            infile.close()
            os.remove(path)
        else:
            outline = 'sarcastic ' + text[1]
            outfile.write(outline)
            outfile.write('\n')   
    except UnicodeDecodeError:
        pass
