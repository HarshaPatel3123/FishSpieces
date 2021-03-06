# import required libraries
import numpy as np
import pandas as pd

#create a dataframe using pandas and retrieve data from csv file
df = pd.read_csv('Fishcsv.csv', engine='python')
df

# separate dependent and independent values

y = df.iloc[:, :1]
x = df.iloc[:,1:]

x.head()

y

# Train test split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state = 0)

#implementing random forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(x_train,y_train)

# prediction
y_pred = classifier.predict(x_test)

# accuracy check
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
score

# create pickle file

import pickle
pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

import numpy as np

classifier.predict([[340,23,26,31,12,4]])
