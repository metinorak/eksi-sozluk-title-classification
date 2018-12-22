import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

data = pd.read_csv('cleaned_data.csv')

categories = list(data.columns.values)
categories = categories[1:]


while(True):
    
    #print('Enter q to quit')
    test_title = input("Please enter a title: ")
    
    
    if(test_title == 'q'):
        break
    
    from sklearn.model_selection import train_test_split
    
    train, test = train_test_split(data, random_state=42, test_size=0, shuffle=True)
    
    
    train_title = train['title']
    test_title = pd.DataFrame(data = [test_title], columns = ['title'])['title']
    
    
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(strip_accents='unicode', analyzer='word', ngram_range=(1,3), norm='l2')
    vectorizer.fit(train_title)
    vectorizer.fit(test_title)
    
    
    
    
    x_train = vectorizer.transform(train_title)
    y_train = train.drop(labels = ['title'], axis=1)
    
    x_test = vectorizer.transform(test_title)
    y_test = test.drop(labels = ['title'], axis=1)
    
    
    
    SVC_pipeline = Pipeline([
                    ('clf', OneVsRestClassifier(LinearSVC(), n_jobs=1))])
                    
    results = []
    

    for category in categories:
		#print('... Processing {}'.format(category))
		# train the model using X_dtm & y
        SVC_pipeline.fit(x_train, train[category])
		# compute the testing accuracy
        prediction = SVC_pipeline.predict(x_test)
        if prediction == 1:
            results.append(category)
		#print('Test accuracy is {}'.format(accuracy_score(test[category], prediction)))
		
		
    print(results)

