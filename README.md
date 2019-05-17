# Ekşi Sözlük Title Classification
Classification using titles and their categories in eksisozluk.com

## 1-scrapingdata.py
This script scrapies eksisozluk.com and retrieve title and title categories, then insert them to the mongodb.
If the connection breaks, you can rerun this script later. It will not insert same records again, but can walk on same titles. You should wait for new records.

## 2-from_mongo_converting_csv.py
With this script you can make a csv file using records in mongodb you've inserted before using scrapingdata.py
Records will be arranged as one hot encoding in this csv file. Cleaned data is saved into the cleaned_data.csv

## 3-cleaningdata.py
Some special characters are removed from titles in this script.

## 4-knowing_data.py
You can see title distribution per category and relation between title length and number of titles (ex: how many titles are there which has length 34).

## DecisionTreeClassifier.py
In this script, DecisionTreeClassifier is implemented to classify titles using prepared data.

## LinearSVC.py
In this script, LinearSVC is implemented to classify titles using prepared data.

## BernoulliNB.py
In this script, BernoulliNB is implemented to classify titles using prepared data.

## LogisticRegression.py
In this script, LogisticRegression is implemented to classify titles using prepared data.

## input.py
You can write titles as input and see the prediction of the LinearSVC algorithm as a user.

## score.py
The functions in this script can be used to test the accuracy of the classifiers in other scripts. score_positive function tests the accuracy just considering the true positive and true negative results. score_exclude_true_negative function tests the accuracy considering results that is excluded true negatives.