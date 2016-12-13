import os

for filename in os.listdir(os.getcwd()+"/Data/BiscuitRaw/"):
    
    try:
        path = os.getcwd() + '/Data/BiscuitRaw/'+ filename
        infile = open(path, 'r')
        newFile = open(os.getcwd() + '/Data/BiscuitRaw/clean'+filename, 'w')
        text = infile.readlines()
        newLines = []
        if len(text) < 2:
            infile.close()
            newFile.close()
            os.remove(path)
        else:
            outString = 'sarcastic '
            startedText = False
            for i,line in enumerate(text):
                startTag = False
                endTag = False
                line = line.rstrip()
                # if we're past where we want to copy
                if line.find("Sociable") != -1:
                    if outString[0] == "'":
                        outString = outString[1:]
                    if outString[len(outString)-1] == "'":
                        outString = outString[:-1]
                    try:
                        if len(outString) != len("sarcastic "):
                            newFile.write(outString)
                        newFile.close()
                        infile.close()
                        os.remove(path)
                    except ValueError:
                        pass
                   
                    break
                # empty line
                if len(line) == 0:
                    continue
                # not copying titles
                elif i == 0:
                    continue
                
                if line.find('<p>') == 0:
                    line = line.replace('<p>','')
                    startTag = True
                if line.find('</p>') != -1:
                    line = line.replace('</p>','')
                    endTag = True
                if startTag and endTag:
                    startedText = True
                    outString = outString + ' ' + line
                   
                else:
                    if startedText:
                        if outString[0] == "'":
                            outString = outString[1:]
                        if outString[len(outString)-1] == "'":
                            outString = outString[:-1]
                        try:
                            if len(outString) != len("sarcastic "):
                                newFile.write(outString)
                            newFile.close()
                            infile.close()
                            os.remove(path)
                        except ValueError:
                            pass
                        break
    except UnicodeDecodeError:
        pass
