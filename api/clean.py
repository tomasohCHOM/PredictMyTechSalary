import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# Load CSV data
df = pd.read_csv("data/datacopy.csv")


COLUMNS = [
    "MainBranch",
    "Employment",
    "RemoteWork",
    "EdLevel",
    "YearsCode",
    "Country",
    "OrgSize",
    "Age",
    "Gender",
    "Trans",
    "Sexuality",
    "Ethnicity",
    "Accessibility",
    "WorkExp",
]

UNUSED_COLUMNS = [
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
]


# Let's drop colums that we won't use, duplicates and NaN rows
df.drop(
    columns=UNUSED_COLUMNS,
    inplace=True,
)


# remove duplicates if we have any(we don't)
df = df.drop_duplicates()

# removing colums that contain at least one NaN value
df = df.dropna()


def factorize_columns(column_name: str):
    codes, uniques = pd.factorize(df[column_name])
    # Add 1 to the codes to start from 1 instead of 0
    df.loc[:, column_name] = codes + 1
    df[column_name] = df[column_name].astype(int)

    # Map string values to their corresponding factorizations
    mapping_dict = {uniques[i]: int(codes[i]) + 1 for i in range(len(uniques))}
    factorization_mappings[column_name] = mapping_dict


# Groups all YearsCode values into 5 groups:
# less than 5 year, from 5 to 10, from 11 to 20,
# from 21 to 40 and more than 40
def process_age(age):
    if age == "Less than 1 year":
        factorization_mappings["YearsCode"][age] = 0
        return 1
    elif age == "More than 50 years":
        factorization_mappings["YearsCode"][age] = 0
        return 5

    age = int(age)
    if age < 5:
        factorization = 1
    elif age >= 5 and age <= 10:
        factorization = 2
    elif age > 10 and age <= 15:
        factorization = 3
    elif age > 15 and age <= 20:
        factorization = 4
    else:
        factorization = 5

    if age not in factorization_mappings["YearsCode"]:
        factorization_mappings["YearsCode"][age] = factorization
    return factorization


# Groups all WorkExp values into 5 groups:
# less than 5 year, from 5 to 10, from 11 to 20,
# from 21 to 40 and more than 40
def process_work_age(age):
    age = int(age)
    if age < 5:
        factorization = 0
    elif age >= 5 and age <= 10:
        factorization = 1
    elif age > 10 and age <= 15:
        factorization = 2
    elif age > 15 and age <= 20:
        factorization = 3
    else:
        factorization = 4

    if age not in factorization_mappings["WorkExp"]:
        factorization_mappings["WorkExp"][age] = factorization
    return factorization


# Replacing string values in the columns with numericals ones + desplaying unique values + convert values to int
factorization_mappings = {}

for column_name in COLUMNS:
    if column_name == "YearsCode":
        factorization_mappings["YearsCode"] = {}
        # Apply the function to the column and create a new column
        df.loc[:, column_name] = df[column_name].apply(process_age)
    elif column_name == "Ethnicity":
        # Only get the 20 most occurring ethnicities (there are thousands of values for this column)
        filtered_ethnicities = df[column_name].value_counts()[:20].index.tolist()
        df = df[df[column_name].isin(filtered_ethnicities)]
        factorize_columns(column_name=column_name)
    elif column_name == "WorkExp":
        factorization_mappings["WorkExp"] = {}
        # Apply the function to the column and create a new column
        df.loc[:, column_name] = df[column_name].apply(process_work_age)
    else:
        factorize_columns(column_name=column_name)

df["ConvertedCompYearly"] = df["ConvertedCompYearly"].astype(int)

# Dump the mappings in json format to mappings.json
with open("mappings/mappings.json", "w") as fp:
    json.dump(factorization_mappings, fp, indent=2)

# Make historgram to understand the distibution
# for i in df.select_dtypes(include="number").columns:
#     sns.histplot(data=df, x=i)
#     plt.show()


# # # # Boxplot to identify Outliers
# for i in df.select_dtypes(include="number").columns:
#     sns.boxplot(data=df, x=i)
#     plt.show()


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


# Drop unuseful columns again
df = df.drop(columns=["LanguageHaveWorkedWith", "YearsCodePro", "MentalHealth"])

# import cleaned data into new file "CleanedData"
df1 = df
df1.to_csv("data/cleaned.csv")

# Scatter plot to understand the relationship
# for i in COLUMNS + ["ConvertedCompYearly"]:
#     sns.scatterplot(data=df, x=i, y="ConvertedCompYearly")
#     plt.show()


# Let's see the correlation with heat map
s = df.select_dtypes(include="number").corr()
plt.figure(figsize=(15, 15))
sns.heatmap(s, annot=True)
