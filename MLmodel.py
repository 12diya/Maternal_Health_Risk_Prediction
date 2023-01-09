import pandas as pd
import warnings
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
import math
import numpy as np
warnings.filterwarnings("ignore")
risk_data=pd.read_csv('Maternal Health Risk Data Set.csv')
X=risk_data.drop('RiskLevel',axis='columns')
Y=risk_data.RiskLevel
X=np.array(X)
Y=np.array(Y)
# scaler=StandardScaler()
# X_scaled=scaler.fit_transform(X)
# X_scaled[:3]
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,random_state=10)
kfold = model_selection.KFold(n_splits = 3, shuffle=True,
                       random_state = 10)
base_cls = DecisionTreeClassifier()
num_trees = 500
Model = BaggingClassifier(base_estimator = base_cls,
                          n_estimators = num_trees,
                          random_state = 10) 
results = model_selection.cross_val_score(Model, X_train, Y_train, cv = kfold)
Model.fit(X_train,Y_train)
pickle.dump(Model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

