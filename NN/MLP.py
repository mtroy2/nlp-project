import random
import numpy as np
import tensorflow as tf
import keras as K
from keras.layers import Dense
from keras.models import Sequential

def main():
	##################
	# Amazon Dataset #
	##################
	x,y = importData('../Data/clean_data.txt', 0)
	# split data into train and test data
	train_x, train_y, test_x, test_y = splitData(x,y)
	# train and test network on data
	createNetwork(train_x, train_y, test_x, test_y, 'adam')


def splitData(x, y):
	indices = random.sample(list(range(len(x))), len(x))	# shuffle test and training data
	n = int(0.8*len(x))	# 80% of data is train and the rest is test
	train = indices[0:n]
	train_x = np.array([x[i] for i in train])
	train_y = np.array([y[i] for i in train])
	test = indices[n:len(x)]
	test_x = np.array([x[i] for i in test])
	test_y = np.array([y[i] for i in test])
	return train_x, train_y, test_x, test_y


def createNetwork(train_x, train_y, test_x, test_y, optimization):
	#########################################
	# step 2: build simple network in keras #
	#########################################
	n_feats = len(train_x[0])
	n_class = len(train_y[0])
	# define the network
	network = Sequential()
	network.add(Dense(16, input_dim=n_feats, activation='sigmoid'))	# sigmoidal activation layer
	network.add(Dense(n_class, activation='softmax'))	# hidden softmax layer
	# define the loss and compile
	opt = optimization	# optimization strategy of stochastic gradient descent
	obj = 'categorical_crossentropy'	# what we are trying to minimize
	network.compile(optimizer=opt, loss=obj, metrics=['accuracy'])	# accuracy for testing the net after
	# training & evaluating
	NEPOCHS = 100
	history = network.fit(train_x, train_y, 
		nb_epoch=NEPOCHS,
		batch_size=1,
		verbose=1)
	loss, acc = network.evaluate(test_x, test_y)	# returns loss and accuracy as a tuple
	# print out result
	print('Final accuracy after {} iterations: {}'.format(NEPOCHS, acc))


def importData(filename, class_pos):
	###########################
	# step 1: data processing #
	###########################
	lines = open(filename)
	num = 0		# num lines in file
	classes = {}	# dictionary of all the different possible classifications
	# get num feats and num classes so that function is more generalize to all data files
	for line in lines:
		arr = line.strip('\n').split(' ')
		n_feats = len(arr) - 1
		num += 1	# number of lines in file4
		if arr[class_pos] not in classes:
			classes[arr[class_pos]] = len(classes)
	n_class = len(classes)
	# init x and y arrays
	x = np.zeros((num,n_feats)).astype(float)
	y = np.zeros((num,n_class)).astype(int)
	i = 0
	for line in open(filename):
		arr = line.strip('\n').split(',')
		# fill in first 4 values into corresponding line of x
		x[i][0:n_feats] = map(float,arr[0:n_feats])
		# fill in with correct classification
		y[i][classes[arr[class_pos]]] = 1
		i += 1
	return x, y

if __name__ == '__main__':
	main()
