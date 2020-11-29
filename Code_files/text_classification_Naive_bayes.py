# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TsBih-oTiIBfThtmyWK4UcfW86WOQv7f

Scikit learn is pre installed in Google colab,........but just to verify we'll use '!' to run commands like console commands in Anaconda
"""

!pip install sklearn 
!pip install scikit-learn

"""Needed to upload our bbc.csv file with all the data :"""

from google.colab import files 


uploaded = files.upload()

"""importing the classes needed from scikit learn"""

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

"""Import NLTK for data filtering ops.....
NLTK is also preinstalled in Colab, but we'll need to download the different wordlists saperately, then we use pandas to create a dataframe of the csv file and ....
"""

import pandas as pd 
import io 
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
#we load the dataset we've uploaded 
df = pd.read_csv(io.BytesIO(uploaded['new_bbc.csv'])) 
# print top part
df.head # --> df is now a pandas dataframe!!

"""Creating a function for cleaning the text in news column"""

from nltk import word_tokenize
from nltk.corpus import stopwords
import string

def text_cleaning(a):
  remove_punctuation = [char for char in a if char not in string.punctuation]
  #print(remove_punctuation)
  remove_punctuation = ''.join(remove_punctuation)
  #print(remove_punctuation)
  return [word for word in remove_punctuation.split() if word.lower() not in stopwords.words('english')]
print(df['news'].apply(text_cleaning))

"""Example:...."""

text_cleaning("who let, the dogs out.")

"""Now we need to vectorize every word, i.e. assign unique numerical value to each word"""

from sklearn.feature_extraction.text import CountVectorizer
vector_transform = CountVectorizer(analyzer=text_cleaning).fit(df['news'])
vector_transform.vocabulary_

"""Vector transform applied to the 'news' column"""

title_transformed = vector_transform.transform(df['news'])
print(title_transformed)

"""Now, we'll perform TF- IDF transform on the vectorized data!"""

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transform = TfidfTransformer().fit(title_transformed)
print(tfidf_transform)

news_tfidf = tfidf_transform.transform(title_transformed)
print(news_tfidf)

"""Split the tf-idf transformed data along with the classes in 'types' into 70:30 ratio for training n testing!!"""

X_train, X_test, y_train, y_test = train_test_split(news_tfidf, df['type'], test_size=0.3,random_state=109) # 70% training and 30% test
print(X_train,"\nshape:",X_train.shape,"\n",X_test,"\nshape:",X_test.shape,"\n",y_train, y_test)

"""Creating a model and predicting the classes for the test data"""

from sklearn.naive_bayes import MultinomialNB

# fit the training features and classes in the model and train
model = MultinomialNB().fit(X_train,y_train)

predicted = model.predict(X_test)#predict the classes for the 30% test data
print(predicted)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,predicted)# function for confusion matrix

"""Plotting the confusion matrix"""

import matplotlib.pyplot as plt
import seaborn as sns

cm = confusion_matrix(y_test, predicted)#create a confusion matrix
print(cm)
#Creating a heatmap:
sns.heatmap(cm, square=True, annot=True, cmap='RdBu', cbar=False,
xticklabels=['business', 'entertainment', 'politics','sports','tech'],# supply label names x axis 
yticklabels=['business', 'entertainment', 'politics','sports','tech'])# supply label names y axis 
plt.xlabel('true label')
plt.ylabel('predicted label')

"""Determining accuracy by comparing the test classes with the predicted classes"""

print("Accuracy:",metrics.accuracy_score(y_test, predicted))