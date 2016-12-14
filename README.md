# nlp-project
2016

To run this code <br />
Note: for all these files, if you want to change the train/test data, you must manually change it in the code - they accept no parameters <br />
Naive-Bayes<br />
  Unigram <br />
    python nb.py <br />
    If you would like to change the train / test files, you must manually go into the files and change the paths of each file <br />
  Bigram <br />
    python nb_bigrams.py <br />
    Same case as unigram for changing train/test files <br />
Logistic Regression <br />
  Note: unigram naive-bayes takes approximately 35 minutes to run on a reduced size dataset <br />
        Bigrams may take much longer - we have never run it all the way to completion 
         <br />
  Unigram <br />
    python lr.py <br />
  Bigram <br />
    python lr_bigrams.py <br />
Neural Network <br />
  Note: to change the number of epochs run, you need to open the network code (MLP.py) and change the value of NEPOCHS (line 47)
  Note: must have Keras and Python 2.7 installed
	module load keras
	python MLP.py

