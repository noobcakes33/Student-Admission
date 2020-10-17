import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

# read dataset csv file
dataset = pd.read_csv("College Dataset.csv")

# specifing features and labels
feature_cols = ["Math_exam", "Essay_exam"]
X = dataset[feature_cols] # Features
y = dataset["Admission"] # Target variable

# splitting the dataset we generated into train and test sets with ratio of 0.75 to 0.25
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

# instantiate the model
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)

# predict test set
y_pred=logreg.predict(X_test)

# confusion matrix
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

# Accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100, "%")
