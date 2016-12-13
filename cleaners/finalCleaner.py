import sys
import os
sys.path.insert(0,os.getcwd()+'/stemming')
import porter2 as p2


train = open('./Data/clean_train.txt','r')
test = open('./Data/clean_test.txt','r')
cleanedTrain = []
cleanedTest = []

punctuationList = ["'",'"']
for i,line in enumerate(train.readlines()):
    cleanLine =[]
    newSen = ''
    for char in line:
        if char in punctuationList:
            newSen += ' ' + char
        else:
            newSen += char
    if i % 1000 == 0:
        print("Train Line = %d" % i)
    try:
        splitLine = newSen.split()
        if len(splitLine) < 2:
            continue
        else:
            cleanLine.append(splitLine[0])
            for word in newSen.split()[1:]:
                if word in stopWords:
                    continue
                else:
                    word = p2.stem(word)
                    cleanLine.append(word)
    except IndexError:
        print("ERRoR on line %d" % i)
    cleanedTrain.append(cleanLine)
for j,line in enumerate(test.readlines()):
    cleanLine =[]
    newSen = ''
    for char in line:
        if char in punctuationList:
            newSen += ' ' + char
        else:
            newSen += char
    if j % 500 == 0:
        print("Test Line = %d" % j )
    cleanLine.append(newSen.split()[0])
    for word in newSen.split()[1:]:
        if word in stopWords:
            continue
        else:
            word = p2.stem(word)
            cleanLine.append(word)
    cleanedTest.append(cleanLine)

trainout = open('./Data/stemmed_train.txt','w')
testout = open('./Data/stemmed_test.txt','w')

for line in cleanedTrain:
    outline = ''
    for word in line:
        outline += word + ' '
    trainout.write(outline)
    trainout.write('\n')
for line in cleanedTest:
    outline = ''
    for word in line:
        outline += word + ' '
    testout.write(outline)
    testout.write('\n')

trainout.close()
testout.close()
train.close()
test.close()

