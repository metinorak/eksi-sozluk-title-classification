import re
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import seaborn as sns

def score(test, pre):
    test_pre = zip(test,pre)
    count_true_positive = 0
    count_false_positive = 0
    
    
    for x,y in test_pre:
        if (x == 0 and y == 1):
            count_false_positive += 1
        
        elif (x == 1 and y == 1): 
            count_true_positive += 1
            
    if (count_true_positive + count_false_positive) == 0:
        return 0
    return count_true_positive/ (count_true_positive + count_false_positive)


def score2(test, pre):
    test_pre = zip(test,pre)
    count_true_positive = 0
    count_false_positive = 0
    count_false_negative = 0
    
    
    for x,y in test_pre:
        if (x == 0 and y == 1):
            count_false_positive += 1
        
        elif (x == 1 and y == 1): 
            count_true_positive += 1
        elif (x == 1 and y == 0):
            count_false_negative += 1
            
    if (count_true_positive + count_false_positive + count_false_negative) == 0:
        return 0
    return count_true_positive/ (count_true_positive + count_false_positive + count_false_negative)

    
    
data = pd.read_csv('cleaned_data.csv')

categories = list(data.columns.values)
categories = categories[1:]



train, test = train_test_split(data, random_state=42, test_size=0.33, shuffle=True)


train_title = train['title']
test_title = test['title']



vectorizer = TfidfVectorizer(strip_accents='unicode', analyzer='word', ngram_range=(1,3), norm='l2')
vectorizer.fit(train_title)
vectorizer.fit(test_title)




x_train = vectorizer.transform(train_title)
y_train = train.drop(labels = ['title'], axis=1)

x_test = vectorizer.transform(test_title)
y_test = test.drop(labels = ['title'], axis=1)



from sklearn.naive_bayes import MultinomialNB
NB_pipeline = Pipeline([
                ('clf', OneVsRestClassifier(MultinomialNB(
                    alpha=1.0, fit_prior=True, class_prior=None))),
            ])
for category in categories:
    print('... Processing {}'.format(category))
    # train the model using X_dtm & y
    NB_pipeline.fit(x_train, train[category])
    # compute the testing accuracy
    prediction = NB_pipeline.predict(x_test)
    print('Test accuracy is {}'.format(acurracy_score(test[category], prediction)))