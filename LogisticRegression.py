import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from score import *


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




#Logistic regression
LogReg_pipeline = Pipeline([
                ('clf', OneVsRestClassifier(LogisticRegression(solver='liblinear', ), n_jobs=1)),
            ])

for category in categories:  
    print('... Processing {}'.format(category))
    LogReg_pipeline.fit(x_train, train[category])
    prediction = LogReg_pipeline.predict(x_test)
    
    print('Test accuracy is {}'.format(accuracy_score(test[category], prediction)))

