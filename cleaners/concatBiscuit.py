import os

outPath = os.getcwd() + '/Data/clean_biscuit.txt'
outfile = open(outPath,'w')
for filename in os.listdir(os.getcwd()+"/Data/BiscuitRaw/"):
    
    try:
        path = os.getcwd() + '/Data/BiscuitRaw/'+ filename
        infile = open(path, 'r')
        text = infile.readlines()
        
        if len(text) == 0:
            infile.close()
            os.remove(path)
        elif len(text[0]) == 0:
            infile.close()
            os.remove(path)
        else:
            outfile.write(text[0])
            outfile.write('\n')   
    except UnicodeDecodeError:
        pass
