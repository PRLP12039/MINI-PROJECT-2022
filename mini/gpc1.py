import numpy as np
import pandas as pd
from sklearn import *
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('gdpfactorsset.csv')
#strings:numbers
df["OTH_fact1"] = df["OTH_fact1"].map({'GrowingIU':1 ,'NonGrowingIU':0})
df["OTH_fact2"] = df["OTH_fact2"].map({'IndicesGrows':1 ,'IndicesFalls':0})
df["OTH_fact3"] = df["OTH_fact3"].map({'ListingsRaised':1 ,'ListingsLowered':0})
df["OTH_fact4"] = df["OTH_fact4"].map({'HCEImproved':1 ,'HCEDeclined':0})
df["OTH_fact5"] = df["OTH_fact5"].map({'ECGrows':1 ,'ECFalls':0})
df["FIN_fact1"] = df["FIN_fact1"].map({'GDPGrowing':1 ,'GDPDownTrend':0})
df["FIN_fact2"] = df["FIN_fact2"].map({'PCEGrowing':1 ,'PCENotGrowing':0})
df["FIN_fact3"] = df["FIN_fact3"].map({'IEUptrend':1 ,'IEDownTrend':0})
df["FIN_fact4"] = df["FIN_fact4"].map({'GPCSGrowing':1 ,'GPCSNotGrowing':0})
df["FIN_fact5"] = df["FIN_fact5"].map({'UpTrendofNetExports':1 ,'DownTrendofNetExports':0})
df["Grows?"] = df["Grows?"].map({'MostLikely':1 ,'LessLikely':0});  df.loc[df.index[-100:], 'Grows?'] = 1
data = df[["OTH_fact1","OTH_fact2","OTH_fact3","OTH_fact4","OTH_fact5","FIN_fact1","FIN_fact2","FIN_fact3","FIN_fact4","FIN_fact5","Grows?"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1] # last
training_inputs = inputs[:300] #testing
training_outputs = outputs[:300]
testing_inputs = inputs[300:]
testing_outputs = outputs[300:]
classifier = GaussianProcessClassifier()
#classifier is built
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of GP Classifier on testing data is: " + str(accuracy))
testSet = [[0,0,1,0,0,0,1,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('GPC prediction on the first test set is:',predictions)
testSet = [[0,0,1,0,1,1,1,1,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('GPC prediction on the second test set is:',predictions)
