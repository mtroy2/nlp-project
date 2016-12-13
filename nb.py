# Rosalyn Tan
# Naive Bayes Classifier

import math
import autograd.scipy.misc as ag

trainDocs = []
testDocs = []
speakerCount = {}
speakerProb = {}
speakerWordCount = {}
speakerWordProb = {}
uniqueWords = set()

def readTrainDocs():
	f = open("./Data/clean_train.txt", "r")
	line = f.readline()
	line = line.strip()
	while line != "":
		trainDocs.append(line)
		line = f.readline()
	f.close()

def readTestDocs():
	f = open("./Data/clean_test.txt", "r")
	line = f.readline()
	line = line.strip()
	while line != "":
		testDocs.append(line)
		line = f.readline()
	f.close()

def collectCounts():
	for doc in trainDocs:
		words = doc.split()
		if len(words) != 0:
			# number of documents each speaker has
			if words[0] in speakerCount:
				speakerCount[words[0]] += 1
			else:
				speakerCount[words[0]] = 1
				speakerWordCount[words[0]] = {}
			# number of each word each speaker has
			for word in words[1:]:
				if word in speakerWordCount[words[0]]:
					speakerWordCount[words[0]][word] += 1
				else:
					speakerWordCount[words[0]][word] = 1
				uniqueWords.add(word)
					
def trainProbabilities():
	speakerSum = 0
	delta = .1 # unseen word types, set equal to 0 for training set probabilites

	for speaker in list(speakerCount.keys()):
		speakerSum = speakerSum + speakerCount[speaker]

	# probability that any document belongs to a speaker
	for speaker in list(speakerCount.keys()):
		speakerProb[speaker] = speakerCount[speaker] / speakerSum

	# probability of a word given a speaker
	for speaker in list(speakerWordCount.keys()):
		speakerWordProb[speaker] = {}
		wordSum = delta * (len(uniqueWords) + 1)
		for word in list(speakerWordCount[speaker].keys()):
			wordSum = wordSum + speakerWordCount[speaker][word]
		for word in list(speakerWordCount[speaker].keys()):
			speakerWordProb[speaker][word] = (speakerWordCount[speaker][word] + delta) / wordSum
		speakerWordProb[speaker]['unk'] = delta / wordSum
	
	for speaker in list(speakerWordProb.keys()):
		for word in list(speakerWordProb[speaker].keys()):
			print(speaker + ' ' + word + ' ' + str(speakerWordProb[speaker][word]))
		print(speaker + ' unk ' + str(speakerWordProb[speaker]['unk']))

def classifySpeakerGivenDoc(doc):
	words = doc.split()
	sumSpeakProb = 0
	logProbSpeakerAndDoc = []
	probSpeakerGivenDoc = {}
	logProbSpeakerGivenDoc = {}
	sumProb = 0
	maxProb = 0

	for speaker in list(speakerCount.keys()):
		sumLogWordProb = 0
		for word in words[1:]:
			if word not in speakerWordProb[speaker]:
				sumLogWordProb = sumLogWordProb + math.log(speakerWordProb[speaker]['unk'])
			else:
				sumLogWordProb = sumLogWordProb + math.log(speakerWordProb[speaker][word])
		logProbSpeakerAndDoc.append(sumLogWordProb + math.log(speakerProb[speaker]))

	for speaker in list(speakerCount.keys()):
		sumLogWordProb = 0
		for word in words[1:]:
			if word not in speakerWordProb[speaker]:
				sumLogWordProb = sumLogWordProb + math.log(speakerWordProb[speaker]['unk'])
			else:
				sumLogWordProb = sumLogWordProb + math.log(speakerWordProb[speaker][word])
		logProbSpeakerGivenDoc[speaker] = (sumLogWordProb + math.log(speakerProb[speaker])) - ag.logsumexp(logProbSpeakerAndDoc)
		probSpeakerGivenDoc[speaker] = math.exp(logProbSpeakerGivenDoc[speaker])

	for speaker in list(speakerCount.keys()):
		sumProb = sumProb + probSpeakerGivenDoc[speaker]
		if probSpeakerGivenDoc[speaker] > maxProb:
			maxProb = probSpeakerGivenDoc[speaker]
			guess = speaker

# uncomment below to get probabilities per speaker for a document

#		print("probability of %s given document: %f" % (speaker, probSpeakerGivenDoc[speaker]))
#	print ("\n")
#	print("probability sum over all speakers: %f" % sumProb)

	if guess == words[0]:
		return 1
	else:
		return 0

if __name__ == '__main__':
	numCorrect = 0

	readTrainDocs()
	readTestDocs()

	collectCounts()
	trainProbabilities()

	numCorrect = 0
	for doc in testDocs:
		numCorrect = numCorrect + classifySpeakerGivenDoc(doc)
	print("Accuracy for test is: %f" % (numCorrect / len(testDocs)))
