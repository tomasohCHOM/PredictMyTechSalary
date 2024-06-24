#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import seaborn as sns
import pickle as pkl

sns.set_theme()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv("data/cleaned.csv")

# Define Input and Output

# Input data
X = df[
    [
        "MainBranch",
        "Employment",
        "RemoteWork",
        "EdLevel",
        "YearsCode",
        "OrgSize",
        "Country",
        "Age",
        "Gender",
        "Trans",
        "Sexuality",
        "Ethnicity",
        "Accessibility",
        "WorkExp",
    ]
]

# Output data
y = df["ConvertedCompYearly"]

X = np.asarray(X).astype("float32")
y = np.asarray(y).astype("float32")


# Split data into training and test sets, 70% and 30%.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR

# Chosing a model we will use
knn = KNeighborsRegressor().fit(X_train, y_train)
ada = AdaBoostRegressor().fit(X_train, y_train)
svm = SVR().fit(X_train, y_train)
ridge = Ridge().fit(X_train, y_train)
lasso = Lasso().fit(X_train, y_train)
rf = RandomForestRegressor().fit(X_train, y_train)
gbm = GradientBoostingRegressor().fit(X_train, y_train)

models = [ridge, lasso, knn, ada, svm, rf, gbm]


def ML(Y, models):
    y_pred = models.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred) * 100

    return mse, rmse, r2


for i in models:
    print("\n", i, "\n\nDifferent models success rate :", ML("salary_in_usd", i))


# Hyperparameter Tuning of Gradient Boosting
from sklearn.ensemble import GradientBoostingRegressor

gbr_best = GradientBoostingRegressor()

search_grid = {
    "n_estimators": [500],
    "learning_rate": [0.001, 0.01, 1],
    "max_depth": [1, 2, 4],
    "subsample": [0.5, 0.75, 1],
    "random_state": [1],
}

search = GridSearchCV(
    estimator=gbr_best,
    param_grid=search_grid,
    scoring="neg_mean_squared_error",
    cv=2,
    n_jobs=1,
)

search.fit(X_train, y_train)
print(search.best_params_)


gbm_best = GradientBoostingRegressor(
    learning_rate=1, max_depth=1, n_estimators=3000, random_state=1, subsample=1
).fit(X_train, y_train)

y_pred = gbm_best.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred) * 100


print("\n GradientBoostingRegressor \n\nDifferent models success rate :", r2)


# Saving Model
file = open("model/model.pkl", "wb")
pkl.dump(gbm_best, file)
model = pkl.load(open("model/model.pkl", "rb"))
