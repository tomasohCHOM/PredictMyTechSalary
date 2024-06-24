#!/usr/bin/env python
# coding: utf-8

# # Data Categories

# The data is seperated in these categories; 
#  
# `ResponseId | MainBranch | Employment | RemoteWork| EdLevel| YearsCode | OrgSize | Country | Age | Gender | Trans | Sexuality | Ethnicity | Accessibility | MentalHealth | WorkExp | ConvertedCompYearly | C# | C | HTML/CSS,
#   | Python | Dart | Bash/Shell | JavaScript | Java | Haskell | Assembly | Go | Groovy | Crystal | PHP | Delphi | C++ | Clojure | Kotlin | APL | Rust | TypeScript | COBOL | PowerShell | Scala | Elixir | F# | LISP | Ruby | Julia | MATLAB | Objective-C | Erlang | Swift | Fortran | OCaml | R | SQL | Perl | Lua | VBA`
#   
# Our Inputs for the model are;
# 
# `MainBranch | Employment | RemoteWork| EdLevel| YearsCode | OrgSize | Country | Age | Gender | Trans | Sexuality | Ethnicity | Accessibility | WorkExp`
#   
# Our Outputs for the model will be;
# 
# `ConvertedCompYearly`

# # Importing data and libraries

# In[64]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pkl

sns.set()

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score, train_test_split, KFold, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn import metrics
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.metrics import confusion_matrix, classification_report


# In[65]:


df = pd.read_csv("CleanedData.csv")
df


# In[66]:


df['ConvertedCompYearly']


# # Define Input and Output

# In[67]:


# Input data 
X = df[['MainBranch','Employment','RemoteWork','EdLevel','YearsCode','OrgSize','Country','Age','Gender','Trans','Sexuality','Ethnicity','Accessibility','WorkExp']]

# Output data 
y = df["ConvertedCompYearly"]

X = np.asarray(X).astype('float32')
y = np.asarray(y).astype('float32')



# Split data into training and test sets, 70% and 30%.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# # Modeling
# 

# In[68]:


from sklearn.linear_model import Ridge,Lasso,RidgeCV,LassoCV,ElasticNet,ElasticNetCV,LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn import neighbors
from sklearn.svm import SVR


# ## Chosing a model we will use

# In[69]:


knn=KNeighborsRegressor().fit(X_train,y_train)
ada=AdaBoostRegressor().fit(X_train,y_train)
svm=SVR().fit(X_train,y_train)
ridge=Ridge().fit(X_train,y_train)
lasso=Lasso().fit(X_train,y_train)
rf=RandomForestRegressor().fit(X_train,y_train)
gbm=GradientBoostingRegressor().fit(X_train,y_train)

models=[ridge,lasso,knn,ada,svm,rf,gbm]

def ML(Y,models):
    y_pred=models.predict(X_test)
    mse=mean_squared_error(y_test,y_pred)
    rmse=np.sqrt(mean_squared_error(y_test,y_pred))
    r2=r2_score(y_test,y_pred)*100
    
    return mse,rmse,r2

for i in models:
    print("\n",i,"\n\nDifferent models success rate :",ML("salary_in_usd",i))


# # Hyperparameter Tuning of Gradient Boosting

# In[70]:


from sklearn.ensemble import GradientBoostingRegressor


# In[71]:


gbr_best = GradientBoostingRegressor()


# In[72]:


search_grid={ 'n_estimators': [500], 'learning_rate':[0.001,0.01,1],
            'max_depth':[1,2,4], 'subsample':[0.5,0.75,1], 'random_state' : [1]}

search = GridSearchCV(estimator = gbr_best, param_grid = search_grid,
                     scoring = 'neg_mean_squared_error', cv = 2, n_jobs = 1)


# In[73]:


search.fit(X_train, y_train)
print(search.best_params_)


# In[74]:


gbm_best=GradientBoostingRegressor(learning_rate = 1, max_depth = 1, n_estimators = 3000, random_state = 1, subsample = 1).fit(X_train,y_train)

y_pred=gbm_best.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mean_squared_error(y_test,y_pred))
r2=r2_score(y_test,y_pred)*100


print("\n GradientBoostingRegressor \n\nDifferent models success rate :", r2)


# # Saving Model

# In[76]:


import pickle

file = open('Salary_prediction_model.pkl', 'wb')
pkl.dump(gbm_best, file)

# Load the saved model
model = pickle.load(open('Salary_prediction_model.pkl', 'rb'))

