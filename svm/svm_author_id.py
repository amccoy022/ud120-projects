#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import os
print os.getcwd() 

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.svm import SVC

### Use only 1% of the training set
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel='rbf', C=10000.0)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

import numpy as np
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, pred)
print accuracy

print("pred[10]: ",pred[10])
print("pred[26]: ",pred[26])
print("pred[50]: ",pred[50])

import collections
counter = collections.Counter(pred)
print counter[1], counter[0]

#########################################################


