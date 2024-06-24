#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# Load CSV data
df = pd.read_csv("data/datacopy.csv")


# Let's drop colums that we won't use, duplicates and NaN rows
df.drop(
    columns=[
        "CodingActivities",
        "LearnCode",
        "LearnCodeOnline",
        "LearnCodeCoursesCert",
        "DevType",
        "PurchaseInfluence",
        "BuyNewTool",
        "LanguageWantToWorkWith",
        "DatabaseHaveWorkedWith",
        "DatabaseWantToWorkWith",
        "PlatformHaveWorkedWith",
        "PlatformWantToWorkWith",
        "WebframeHaveWorkedWith",
        "WebframeWantToWorkWith",
        "MiscTechHaveWorkedWith",
        "MiscTechWantToWorkWith",
        "ToolsTechHaveWorkedWith",
        "ToolsTechWantToWorkWith",
        "NEWCollabToolsHaveWorkedWith",
        "NEWCollabToolsWantToWorkWith",
        "OpSysProfessional use",
        "OpSysPersonal use",
        "VersionControlSystem",
        "VCInteraction",
        "VCHostingPersonal use",
        "VCHostingProfessional use",
        "OfficeStackAsyncHaveWorkedWith",
        "OfficeStackAsyncWantToWorkWith",
        "OfficeStackSyncHaveWorkedWith",
        "OfficeStackSyncWantToWorkWith",
        "Blockchain",
        "NEWSOSites",
        "SOVisitFreq",
        "SOAccount",
        "SOPartFreq",
        "SOComm",
        "TBranch",
        "ICorPM",
        "Knowledge_1",
        "Knowledge_2",
        "Knowledge_3",
        "Knowledge_4",
        "Knowledge_5",
        "Knowledge_6",
        "Knowledge_7",
        "Frequency_1",
        "Frequency_2",
        "Frequency_3",
        "TimeSearching",
        "TimeAnswering",
        "Onboarding",
        "ProfessionalTech",
        "TrueFalse_1",
        "TrueFalse_2",
        "TrueFalse_3",
        "SurveyLength",
        "SurveyEase",
        "CompTotal",
        "CompFreq",
        "Currency",
    ],
    inplace=True,
)


# remove duplicates if we have any(we don't)
df = df.drop_duplicates()

# removing colums that contain at least one NaN value
df = df.dropna()


# Replacing string values in the columns with numericals ones + desplaying unique values + convert values to int

df.loc[:, "MainBranch"] = pd.factorize(df["MainBranch"])[0] + 1
df["MainBranch"] = df["MainBranch"].astype(int)


df.loc[:, "Employment"] = pd.factorize(df["Employment"])[0] + 1
df["Employment"] = df["Employment"].astype(int)


df.loc[:, "RemoteWork"] = pd.factorize(df["RemoteWork"])[0] + 1
df["RemoteWork"] = df["RemoteWork"].astype(int)

df.loc[:, "EdLevel"] = pd.factorize(df["EdLevel"])[0] + 1
df["EdLevel"] = df["EdLevel"].astype(int)

# let's group all year of code into 5 groups: less than 5 year, from 5 to 10, from 11 to 20, from 21 to 40
# and more than 40


def process_age(age):
    if age == "Less than 1 year":
        return 1
    elif age == "More than 50 years":
        return 5
    age = int(age)
    if age < 5:
        return 1
    elif age >= 5 and age <= 10:
        return 2
    elif age > 10 and age <= 20:
        return 3
    elif age > 20 and age <= 40:
        return 4
    else:
        return 5


# Apply the function to the column and create a new column
df.loc[:, "YearsCode"] = df["YearsCode"].apply(process_age)

df.loc[:, "Country"] = pd.factorize(df["Country"])[0] + 1
df["Country"] = df["Country"].astype(int)


df.loc[:, "OrgSize"] = pd.factorize(df["OrgSize"])[0] + 1
df["OrgSize"] = df["OrgSize"].astype(int)


df.loc[:, "Age"] = pd.factorize(df["Age"])[0] + 1
df["Age"] = df["Age"].astype(int)


df.loc[:, "Gender"] = pd.factorize(df["Gender"])[0] + 1
df["Gender"] = df["Gender"].astype(int)


df.loc[:, "Trans"] = pd.factorize(df["Trans"])[0] + 1
df["Trans"] = df["Trans"].astype(int)

df.loc[:, "Sexuality"] = pd.factorize(df["Sexuality"])[0] + 1
df["Sexuality"] = df["Sexuality"].astype(int)


# Only get the 20 most occurring ethnicities (there are thousands of values for this column)
filtered_ethnicities = df["Ethnicity"].value_counts()[:20].index.tolist()
df = df[df["Ethnicity"].isin(filtered_ethnicities)]
df.loc[:, "Ethnicity"] = pd.factorize(df["Ethnicity"])[0] + 1
df["Ethnicity"] = df["Ethnicity"].astype(int)

df.loc[:, "Accessibility"] = pd.factorize(df["Accessibility"])[0] + 1
df["Accessibility"] = df["Accessibility"].astype(int)

df.loc[:, "MentalHealth"] = pd.factorize(df["MentalHealth"])[0] + 1
df["MentalHealth"] = df["MentalHealth"].astype(int)


# let's group all year of work experiece into 5 groups: less than 5 year, from 5 to 10, from 11 to 20, from 21 to 40
# and more than 40
def process_work_age(age):
    age = int(age)
    age = int(age)
    if age < 5:
        return 0
    elif age >= 5 and age <= 10:
        return 1
    elif age > 10 and age <= 20:
        return 2
    elif age > 20 and age <= 40:
        return 3
    else:
        return 4


# Apply the function to the column and create a new column
df.loc[:, "WorkExp"] = df["WorkExp"].apply(process_work_age)

df["ConvertedCompYearly"] = df["ConvertedCompYearly"].astype(int)


# Make historgram to understand the distibution
for i in df.select_dtypes(include="number").columns:
    sns.histplot(data=df, x=i)
    plt.show()


# Boxplot to identify Outliers
for i in df.select_dtypes(include="number").columns:
    sns.boxplot(data=df, x=i)
    plt.show()


# Let's work with "ConvertedCompYearly" as it has the most outliers
# Capping outliers
df[["ConvertedCompYearly"]].describe()

sns.boxplot(x=df["ConvertedCompYearly"])
plt.show()


q1 = df["ConvertedCompYearly"].quantile(0.25)
q3 = df["ConvertedCompYearly"].quantile(0.75)
iqr = q3 - q1

up_lim = q3 + (1.5 * iqr)
low_lim = q1 - (1.5 * iqr)

# capping this data

df.loc[(df["ConvertedCompYearly"] > up_lim), "ConvertedCompYearly"] = up_lim
df.loc[(df["ConvertedCompYearly"] < low_lim), "ConvertedCompYearly"] = low_lim

df[["ConvertedCompYearly"]].describe()

sns.boxplot(x=df["ConvertedCompYearly"])
plt.show()


# Now let's drop unuseful columns again
df = df.drop(columns=["LanguageHaveWorkedWith", "YearsCodePro"])

# import cleaned data into new file "CleanedData"
df1 = df
df1.to_csv("data/cleaned.csv")

# Let's scatter plot to understand the relationship

for i in [
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
    "MentalHealth",
    "WorkExp",
    "ConvertedCompYearly",
]:
    sns.scatterplot(data=df, x=i, y="ConvertedCompYearly")
    plt.show()


# Let's see the correlation with heat map
s = df.select_dtypes(include="number").corr()
plt.figure(figsize=(15, 15))
sns.heatmap(s, annot=True)
