from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd, numpy as np, re, time
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

train = [
('do something about it please, even tho you ban simple himself in 5 min this shit can still be up for 2 hours without even being noticed lmao', 'neg'),
('I love this sandwich.', 'pos'),
('I feel very good about these beers.', 'pos'),
('this is my best work.', 'pos'),
("what an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('he is my sworn enemy!', 'neg'),
('my boss is horrible.', 'neg')
]

test = [
('the beer was good.', 'pos'),
('I do not enjoy my job', 'neg'),
("I ain't feeling dandy today.", 'neg'),
("I feel amazing!", 'pos'),
('Gary is a friend of mine.', 'pos'),
("I can't believe I'm doing this.", 'neg')
]

cl = NaiveBayesClassifier(train)
