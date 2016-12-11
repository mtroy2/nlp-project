import os

for filename in os.listdir(os.getcwd()+"/Data/OnionRaw"):
    print(filename)
    try:
        path = os.getcwd() + '/Data/OnionRaw/'+ filename
        infile = open(path, 'r')
        text = infile.readlines()
        if len(text) < 2:
            infile.close()
            os.remove(path)
        else:
            title = text[0]
            print(title)
            body = text[1]
        
            print(body)
            if 'class=' in body:
                infile.close()
                os.remove(path)
    except UnicodeDecodeError:
        print("ERROR")
        print(infile)
