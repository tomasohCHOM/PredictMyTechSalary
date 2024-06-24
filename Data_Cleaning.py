#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning
# 
# 

# In[71]:


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


# upload data
df = pd.read_csv('datacopy.csv')


# ### Let's drop colums that we won't use, duplicates and NaN rows

# In[72]:


# drop colums "CodingActivities", "LearnCode", "LearnCodeOnline", "LearnCodeCoursesCert", "DevType" <- (this one
# will be too complicated to analise), "PurchaseInfluence", "BuyNewTool", "LanguageWantToWorkWith",
# "DatabaseHaveWorkedWith", "DatabaseWantToWorkWith", "PlatformHaveWorkedWith", "PlatformWantToWorkWith", 
# "WebframeHaveWorkedWith", "WebframeWantToWorkWith", "MiscTechHaveWorkedWith", "MiscTechWantToWorkWith",
# "ToolsTechHaveWorkedWith" <- (this one will be complicated to like split and analyse, but if we have 
# time, we can try), "ToolsTechWantToWorkWith", "NEWCollabToolsHaveWorkedWith", "NEWCollabToolsWantToWorkWith", 
# "OpSysProfessional use", "OpSysPersonal use", "VersionControlSystem", "VCInteraction", "VCHostingPersonal use",
# "VCHostingProfessional use", "OfficeStackAsyncHaveWorkedWith", "OfficeStackAsyncWantToWorkWith", 
# "OfficeStackSyncHaveWorkedWith", "OfficeStackSyncWantToWorkWith", "Blockchain", "NEWSOSites", "SOVisitFreq", 
# "SOAccount", "SOPartFreq", "SOComm", "TBranch", "ICorPM", "Knowledge_1", "Knowledge_2", "Knowledge_3",
# "Knowledge_4", "Knowledge_5", "Knowledge_6", "Knowledge_7", "Frequency_1", "Frequency_2", "Frequency_3", 
# "TimeSearching", "TimeAnswering", "Onboarding", "ProfessionalTech", "TrueFalse_1", TrueFalse_2", TrueFalse_3"
# "SurveyLength", "SurveyEase", "CompTotal", "CompFreq", "Currency"

df.drop(columns=["CodingActivities", "LearnCode", "LearnCodeOnline", "LearnCodeCoursesCert", "DevType",
                         "PurchaseInfluence", "BuyNewTool", "LanguageWantToWorkWith","DatabaseHaveWorkedWith", "DatabaseWantToWorkWith", "PlatformHaveWorkedWith", "PlatformWantToWorkWith", "WebframeHaveWorkedWith", "WebframeWantToWorkWith", "MiscTechHaveWorkedWith", "MiscTechWantToWorkWith",
                        "ToolsTechHaveWorkedWith","ToolsTechWantToWorkWith", "NEWCollabToolsHaveWorkedWith",
                        "NEWCollabToolsWantToWorkWith","OpSysProfessional use", "OpSysPersonal use",
                        "VersionControlSystem", "VCInteraction", "VCHostingPersonal use",
                        "VCHostingProfessional use", "OfficeStackAsyncHaveWorkedWith", "OfficeStackAsyncWantToWorkWith",
                        "OfficeStackSyncHaveWorkedWith", "OfficeStackSyncWantToWorkWith", "Blockchain", "NEWSOSites", "SOVisitFreq",
                        "SOAccount", "SOPartFreq", "SOComm", "TBranch", "ICorPM", "Knowledge_1", "Knowledge_2", "Knowledge_3",
                        "Knowledge_4", "Knowledge_5", "Knowledge_6", "Knowledge_7", "Frequency_1", "Frequency_2", "Frequency_3",
                        "TimeSearching", "TimeAnswering", "Onboarding", "ProfessionalTech", "TrueFalse_1", "TrueFalse_2", "TrueFalse_3",
                        "SurveyLength", "SurveyEase","CompTotal", "CompFreq","Currency"], inplace=True)



# In[73]:


#remove duplicates if we have any(we don't)
df = df.drop_duplicates()


# In[74]:


# removing colums that contain at least one NaN value
df = df.dropna()


# ### Replacing string values in the columns with numericals ones + desplaying unique values + convert values to int
# 

# In[75]:


#let's display all unique values in MainBranch column
print('MainBranch: ', df['MainBranch'].unique())


# In[76]:


df.loc[:,'MainBranch'] = pd.factorize(df['MainBranch'])[0] + 1
df['MainBranch'] = df['MainBranch'].astype(int)


# In[77]:


#let's display all unique values in MainBranch column
print('MainBranch: ', df['MainBranch'].unique())


# In[78]:


#let's display all unique values in MainBranch column
print('Employment: ', df['Employment'].unique())


# In[79]:


df.loc[:,'Employment'] = pd.factorize(df['Employment'])[0] + 1
df['Employment'] = df['Employment'].astype(int)


# In[80]:


#let's display all unique values in MainBranch column
print('Employment: ', df['Employment'].unique())


# In[81]:


#let's display all unique values in 'RemoteWork' column
print('RemoteWork: ', df['RemoteWork'].unique())


# In[82]:


df.loc[:,'RemoteWork'] = pd.factorize(df['RemoteWork'])[0] + 1


# In[83]:


#let's display all unique values in 'RemoteWork' column
print('RemoteWork: ', df['RemoteWork'].unique())
df['RemoteWork'] = df['RemoteWork'].astype(int)


# In[84]:


#let's display all unique values in 'EdLevel' column
print('EdLevel: ', df['EdLevel'].unique())


# In[85]:


df.loc[:,'EdLevel'] = pd.factorize(df['EdLevel'])[0] + 1
df['EdLevel'] = df['EdLevel'].astype(int)


# In[86]:


#let's display all unique values in 'EdLevel' column
print('EdLevel: ', df['EdLevel'].unique())


# In[87]:


#let's display all unique values in 'YearsCode' column
print('YearsCode: ', df['YearsCode'].unique())


# In[88]:


# let's group all year of code into 5 groups: less than 5 year, from 5 to 10, from 11 to 20, from 21 to 40 
# and more than 40

def process_age(age):
    if age == 'Less than 1 year':
        return 1
    elif age == 'More than 50 years':
        return (5)
    age = int(age)
    if age <5:
        return(1)
    elif (age >= 5 and age <=10):
        return(2)
    elif (age>10 and age <=20):
        return (3)
    elif (age>20 and age <=40):
        return (4)
    else:
        return(5)

# Apply the function to the column and create a new column
df.loc[:,'YearsCode'] = df['YearsCode'].apply(process_age)


# In[89]:


print('YearsCode: ', df['YearsCode'].unique())


# In[90]:


#let's display all unique values in 'Country' column
print('Country: ', df['Country'].unique())


# In[91]:


df.loc[:,'Country'] = pd.factorize(df['Country'])[0] + 1


# In[92]:


#let's display all unique values in 'Country' column
print('Country: ', df['Country'].unique())
df['Country'] = df['Country'].astype(int)


# In[93]:


#let's display all unique values in 'OrgSize' column
print('OrgSize: ', df['OrgSize'].unique())


# In[94]:


df.loc[:,'OrgSize'] = pd.factorize(df['OrgSize'])[0] + 1


# In[95]:


#let's display all unique values in 'OrgSize' column
print('OrgSize: ', df['OrgSize'].unique())
df['OrgSize'] = df['OrgSize'].astype(int)


# In[96]:


#let's display all unique values in 'Age' column
print('Age: ', df['Age'].unique())


# In[97]:


df.loc[:,'Age'] = pd.factorize(df['Age'])[0] + 1


# In[98]:


#let's display all unique values in 'Age' column
print('Age: ', df['Age'].unique())
df['Age'] = df['Age'].astype(int)


# In[99]:


#let's display all unique values in 'Gender' column
print('Gender: ', df['Gender'].unique())


# In[100]:


df.loc[:,'Gender'] = pd.factorize(df['Gender'])[0] + 1


# In[101]:


#let's display all unique values in 'Gender' column
print('Gender: ', df['Gender'].unique())
df['Gender'] = df['Gender'].astype(int)


# In[102]:


#let's display all unique values in 'Trans' column
print('Trans: ', df['Trans'].unique())


# In[103]:


df.loc[:,'Trans'] = pd.factorize(df['Trans'])[0] + 1


# In[104]:


#let's display all unique values in 'Trans' column
print('Trans: ', df['Trans'].unique())
df['Trans'] = df['Trans'].astype(int)


# In[105]:


#let's display all unique values in 'Sexuality' column
print('Sexuality: ', df['Sexuality'].unique())


# In[106]:


df.loc[:,'Sexuality'] = pd.factorize(df['Sexuality'])[0] + 1
df['Sexuality'] = df['Sexuality'].astype(int)


# In[107]:


filtered_ethnicities = df['Ethnicity'].value_counts()[:20].index.tolist()
print(filtered_ethnicities)

df = df[df['Ethnicity'].isin(filtered_ethnicities)]
df.loc[:,'Ethnicity'] = pd.factorize(df['Ethnicity'])[0] + 1


# In[108]:


#let's display all unique values in 'Ethnicity' column
print('Ethnicity: ', df['Ethnicity'].unique())
df['Ethnicity'] = df['Ethnicity'].astype(int)


# In[109]:


#df.loc[:,'Ethnicity'] = pd.factorize(df['Ethnicity'])[0] + 1


# In[110]:


#let's display all unique values in 'Accessibility' column
print('Accessibility: ', df['Accessibility'].unique())


# In[111]:


df.loc[:,'Accessibility'] = pd.factorize(df['Accessibility'])[0] + 1
df['Accessibility'] = df['Accessibility'].astype(int)


# In[ ]:





# In[112]:


#let's display all unique values in 'MentalHealth' column
print('MentalHealth: ', df['MentalHealth'].unique())


# In[113]:


df.loc[:,'MentalHealth'] = pd.factorize(df['MentalHealth'])[0] + 1
df['MentalHealth'] = df['MentalHealth'].astype(int)


# In[114]:


#let's display all unique values in 'WorkExp' column
print('WorkExp: ', df['WorkExp'].unique())


# In[115]:


# let's group all year of work experiece into 5 groups: less than 5 year, from 5 to 10, from 11 to 20, from 21 to 40 
# and more than 40

def process_age(age):
    age = int(age)
    age = int(age)
    if age <5:
        return(0)
    elif (age >= 5 and age <=10):
        return(1)
    elif (age>10 and age <=20):
        return (2)
    elif (age>20 and age <=40):
        return (3)
    else:
        return(4)

# Apply the function to the column and create a new column
df.loc[:,'WorkExp'] = df['WorkExp'].apply(process_age)


# In[116]:


df['ConvertedCompYearly'] = df['ConvertedCompYearly'].astype(int)


# In[117]:


df.dtypes


# In[118]:


df


# In[119]:


# make historgram to understand the distibution

for i in df.select_dtypes(include = "number").columns:
    sns.histplot( data = df, x = i)
    plt.show()


# In[120]:


# boxplot to identify Outliers

for i in df.select_dtypes(include = "number").columns:
    sns.boxplot( data = df, x = i)
    plt.show()


#  

# ## Let's work with "ConvertedCompYearly" as it has the most outliers

# ## Capping outliers

# In[121]:


df[['ConvertedCompYearly']].describe()


# In[122]:


import sklearn
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x = df['ConvertedCompYearly'])
plt.show()


# In[123]:


q1 = df['ConvertedCompYearly'].quantile(0.25)
q3 = df['ConvertedCompYearly'].quantile(0.75)
iqr = q3 - q1

up_lim = q3 + (1.5 * iqr)
low_lim = q1 - (1.5*iqr)

#capping this data

df.loc[(df['ConvertedCompYearly'] > up_lim), 'ConvertedCompYearly'] = up_lim
df.loc[(df['ConvertedCompYearly'] < low_lim), 'ConvertedCompYearly'] = low_lim


# In[124]:


df[['ConvertedCompYearly']].describe()


# In[125]:


import sklearn
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x = df['ConvertedCompYearly'])
plt.show()


# ### The following 2 functions will make new columns with the names of all languages and write 1, if person knows this language and 0 otherwise

# In[126]:


# function that return 1 person knows each language in the list and 0 otherwise
def process_list(lst):
    languages = ['C#', 'C', 'HTML/CSS', 'Python' ,'Dart' ,'Bash/Shell' ,'JavaScript' ,'Java',
 'Haskell', 'Assembly', 'Go', 'Groovy', 'Crystal' ,'PHP' ,'Delphi' ,'C++',
 'Clojure' ,'Kotlin', 'APL', 'Rust' ,'TypeScript', 'COBOL' ,'PowerShell' ,'Scala',
 'Elixir', 'F#' ,'LISP' ,'Ruby', 'Julia' ,'MATLAB', 'Objective-C' ,'Erlang',
 'Swift', 'Fortran', 'OCaml' ,'R' ,'SQL', 'Perl' ,'Lua' ,'VBA']
    result = ""
    lst = lst.split(';')
    for lang in languages:
        if lang in lst:
            result += "1,"
        else:
            result += "0,"
    return result[:-1]  # Remove the trailing comma


# Apply the function to the column and create a new column
df.loc[:,'new_column'] = df['LanguageHaveWorkedWith'].apply(process_list)


# In[127]:


## add new colums with languges names


# Specifying the column names
column_names = ['C#', 'C', 'HTML/CSS', 'Python', 'Dart', 'Bash/Shell', 'JavaScript', 'Java',
                'Haskell', 'Assembly', 'Go', 'Groovy', 'Crystal', 'PHP', 'Delphi', 'C++',
                'Clojure', 'Kotlin', 'APL', 'Rust', 'TypeScript', 'COBOL', 'PowerShell',
                'Scala', 'Elixir', 'F#', 'LISP', 'Ruby', 'Julia', 'MATLAB', 'Objective-C',
                'Erlang', 'Swift', 'Fortran', 'OCaml', 'R', 'SQL', 'Perl', 'Lua', 'VBA']


# Splitting the 'new_column' and assigning to the new DataFrame
df[column_names] = df['new_column'].str.split(',', expand=True)

df[column_names] = df[column_names].astype(int)


# In[128]:


df


# In[129]:


print(df.head(0))


# ### Now let's drop unuseful columns again

# In[130]:


df = df.drop(columns=['LanguageHaveWorkedWith', 'new_column', 'YearsCodePro'])


# In[131]:


df


# # Importing cleaned data into new file "CleanedData"

# In[132]:


# import cleaned data into new file "CleanedData"
df1 = df
df1.to_csv('CleanedData.csv')


#  

# # Let's scatter plot to understand the relationship

# In[133]:


for i in ['MainBranch','Employment','RemoteWork','EdLevel','YearsCode','OrgSize','Country','Age','Gender','Trans','Sexuality','Ethnicity','Accessibility','MentalHealth','WorkExp','C#','C','HTML/CSS','Python','Dart','Bash/Shell','JavaScript','Java','Haskell','Assembly','Go','Groovy','Crystal','PHP','Delphi','C++','Clojure','Kotlin','APL','Rust','TypeScript','COBOL','PowerShell','Scala','Elixir','F#','LISP','Ruby','Julia','MATLAB','Objective-C','Erlang','Swift','Fortran','OCaml','R','SQL','Perl','Lua','VBA']:
    sns.scatterplot(data = df, x = i, y = 'ConvertedCompYearly')
    plt.show()


# # Let's see the correlation with heat map

# In[134]:


s = df.select_dtypes(include = "number").corr()
plt.figure(figsize = (20,20))
sns.heatmap(s)


# In[135]:


# let's do heatmap without languages

df_2 = df[['MainBranch','Employment','RemoteWork','EdLevel','YearsCode','OrgSize','Country','Age','Gender','Trans','Sexuality','Ethnicity','Accessibility','MentalHealth','WorkExp', 'ConvertedCompYearly']]
s = df_2.select_dtypes(include = "number").corr()
plt.figure(figsize = (15,15))
sns.heatmap(s, annot = True)

