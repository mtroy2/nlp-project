# nlp-project
2016

To run this code <br />
Note: for all these files, if you want to change the train/test data, you must manually change it in the code - they accept no parameters <br />
Naive-Bayes
<ul>
  <li>Unigram </li>
  <ul> <li>python nb.py</li>
    <li>If you would like to change the train / test files, you must manually go into the files and change the paths of each file </li>
    </ul>
  <li>Bigram </li>
    <ul>
    	<li>python nb_bigrams.py </li>
    	<li>Same case as unigram for changing train/test files</li>
	</ul>
</ul>
Logistic Regression <br />

Note: unigram naive-bayes takes approximately 35 minutes to run on a reduced size dataset 
Bigrams may take much longer - we have never run it all the way to completion <br />
 <ul>       
 <li>Unigram </li>
   <ul>
   <li>python lr.py </li></ul>
 
 <li>Bigram</li> <ul>
 <li>python lr_bigrams.py </li>
 </ul>
Neural Network <br />
<ul>
  <li>Note: to change the number of epochs run, you need to open the network code (MLP.py) and change the value of NEPOCHS (line 47) </li>
  <li>Note: must have Keras and Python 2.7 installed </li>
  <ul>
  <li>module load keras</li>
  <li>python MLP.py</li>
  </ul>

</ul>
