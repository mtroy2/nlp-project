import os

for filename in os.listdir(os.getcwd()+"/Data/OnionRaw"):
    
    try:
        path = os.getcwd() + '/Data/OnionRaw/'+ filename
        infile = open(path, 'r')
        text = infile.readlines()
        if len(text) < 2:
            infile.close()
            os.remove(path)
        else:
            title = text[0]
         
            body = text[1]
        
            
            if 'class=' in body:
                infile.close()
                os.remove(path)
    except UnicodeDecodeError:
        print("ERROR")
        print(infile)
