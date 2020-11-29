---- Naive Bayes Implementation for Text Classification----
**************************************************************************************************
@ authors :
Akash Apturkar
Amruth Anand
Shubham Pandya
Nidhi Kulkarni
-----------------------
Steps for installing :-
-----------------------

Our Project is run Google Colab where this dependency is pre-installed on other platforms.

The following modules need to be installed using pip in the command prompt before running the main code:

pip install sklearn

pip install nltk

pip install Tensorflow

--then in python terminal run:
>>> import nltk
>>> nltk.download()
--then select all and download

----------------------------------------------
----Data Source----
----------------------------------------------
https://www.kaggle.com/shivamkushwaha/bbc-full-text-document-classification

----------
EXECUTION:
----------
1.'testing_iris_scikitlearn_sepal.py' - the file refers to scikit learn implementation of naive bayes on iris data set (calculating accuracy for sepal length and sepal width).
2.'testing_iris_scikitlearn_petal.py' - the file refers to scikit learn implementation of naive bayes on iris data set (calculating accuracy for petal length and petal width).
3.'testing_iris_tesorflow_sepal.py' - the file refers to tensorflow implementation of naive bayes on iris data set.
4. Run the file Data_cleaning.py to convert out given data in to the csv format.
5. On Goodgle Colab- upload new_bbc.csv to the colaboratory(code included in text_classification_Naive_bayes.py), on jupyter notebook make sure new_bbc.csv in the same directroy.
6.'text_classification_Naive_bayes.py' and run the file to obtain the results.