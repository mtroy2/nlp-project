# Rosalyn Tan
# Logistic Regression Classifier

import autograd.numpy as np
import autograd.scipy.misc as ag
import random
from autograd import grad

trainDocs = []
testDocs = []
wordSet = set()
speakerSet = set()
wordDict = {}
speakerDict = {}

def readTrainDocs():
	f = open("./Data/clean_train.txt", "r")
	lines = f.readlines()
	#line = line.strip()
	for i in range(0,10000):
		line = lines[i]
		line = line.strip()
		trainDocs.append(line)
	f.close()

def readTestDocs():
	f = open("./Data/clean_test.txt", "r")
	lines = f.readlines()
	#line = line.strip()
	for i in range(0,2300):
	#while line != "":
		line = lines[i]
		line = line.strip()
		testDocs.append(line)
		#line = f.readline()
	f.close()

def initializeLambdas():
	# initialize lambdas to 0
	for doc in trainDocs:
		words = doc.split()
		if len(words) > 0:
			speakerSet.add(words[0])
			for word in words[1:]:
				wordSet.add(word)
#	wordSet.add('unk')
	wordSet.add('<bias>')

	i = 0
	for word in wordSet:
		wordDict[word] = i
		i += 1

	i = 0
	for speaker in speakerSet:
		speakerDict[speaker] = i
		i += 1

	lambdaArray = np.zeros((len(speakerSet), len(wordSet)))
	return lambdaArray

def negLogProbSpeakerGivenDoc(model, doc, speaker):
	words = doc.split()

	wordVec = np.zeros([len(list(wordDict.keys())), 1])

	for i in range(1, len(words)):
		if words[i] not in wordDict:
	#		wordVec[wordDict['unk']] += 1
			pass
		else:
			wordVec[wordDict[words[i]]] += 1
	wordVec[wordDict['<bias>']] = 1
	
	z_d = np.dot(model, wordVec)

	s_k_d = z_d[speakerDict[speaker]]
	
	p_k_d = s_k_d - ag.logsumexp(z_d)
	
	return (p_k_d * -1)

def stochGradDescent(func, model, doc, speaker):
	g_logProb = grad(func)
	model -= .01 * g_logProb(model, doc, speaker)

def classify(model, doc):
	maxProb = 0

	words = doc.split()

	for speaker in list(speakerDict.keys()):
		neg_p_k_d = negLogProbSpeakerGivenDoc(model, doc, speaker)
		p_k_d = np.exp(neg_p_k_d * -1)
		if p_k_d > maxProb:
			maxProb = p_k_d
			guess = speaker

	if guess == words[0]:
		return 1
	else:
		return 0		

def computeProb(model, doc):
	for speaker in list(speakerDict.keys()):
		neg_p_k_d = negLogProbSpeakerGivenDoc(model, doc, speaker)
		p_k_d = np.exp(neg_p_k_d * -1)
		print("P(%s|d) = %f" % (speaker, p_k_d))

if __name__ == "__main__":
	readTrainDocs()
	readTestDocs()

	sumLogProb = 0
	totalCorrect = 0

	lambdaArray = initializeLambdas()

	for j in range(1, 8):
		for i in range(0, len(trainDocs)):
			if len(trainDocs[i]) > 0:
				try: 
					sumLogProb += negLogProbSpeakerGivenDoc(lambdaArray, trainDocs[i], trainDocs[i].split()[0])
					stochGradDescent(negLogProbSpeakerGivenDoc, lambdaArray, trainDocs[i], trainDocs[i].split()[0])			
				except IndexError:
					print('line = ' + trainDocs[i])
				if i % 1000 == 0:
					print("Line %d" % i)
		print("Negative log-probability of train after iteration %d: %f" % (j, sumLogProb))
		sumLogProb = 0
		totalCorrect = 0
		random.shuffle(trainDocs)
	for doc in testDocs:
		totalCorrect += classify(lambdaArray, doc)
	print("Accuracy on test: %f" % (totalCorrect / len(testDocs)))
