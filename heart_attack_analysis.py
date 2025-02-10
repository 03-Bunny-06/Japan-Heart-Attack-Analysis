import numpy as np
import pandas as pd

df = pd.read_csv("japan_heart_attack_dataset.csv")

#Removing unwanted columns

removing_columns = df.drop(labels=['Extra_Column_1', 'Extra_Column_2', 'Extra_Column_3', 'Extra_Column_4', 'Extra_Column_5', 'Extra_Column_6', 'Extra_Column_7', 'Extra_Column_8', 'Extra_Column_9', 'Extra_Column_10', 'Extra_Column_11', 'Extra_Column_12', 'Extra_Column_13', 'Extra_Column_14', 'Extra_Column_15'], axis=1, inplace=True)

#Handling empty data by relacing it with zeros

making_duplicate_free = df.fillna(0, inplace=True)

#Number of males that got attacked with heart attack are 15067/30000 50.6% and females are around 14933/30000 49.4%

male_data = df[df['Gender'] == 'Male']

female_data = df[df['Gender'] == 'Female']

# print(male_data)

# print(female_data)

#With Addictions or Health Issues

smoking_history_male = male_data[male_data['Smoking_History'] == 'Yes']

diabetes_history_male = male_data[male_data['Diabetes_History'] == 'Yes']

both_male = male_data[(male_data['Diabetes_History'] == 'Yes') & (male_data['Smoking_History'] == 'Yes')]

#Males that got heart attack with only 4542 are smokers

#Males that got heart attack with only 3025 are diabetic

#Males that got heart attack with 904 are both diabetic and smokers

smoking_history_female = female_data[female_data['Smoking_History'] == 'Yes']

diabetes_history_female = female_data[female_data['Diabetes_History'] == 'Yes']

both_female = female_data[(female_data['Diabetes_History'] == 'Yes') & (female_data['Smoking_History'] == 'Yes')]

#print(both_female)

#Females that got heart attack with only 4455 are smokers

#Females that got heart attack with only 3072 are diabetic

#Females that got heart attack with 941 are both diabetic and smokers

urban_data_male = df[(df['Region'] == 'Urban') & (df['Gender'] == 'Male') & (df['Smoking_History'] == 'Yes')]

rural_data_male = df[(df['Region'] == 'Rural') & (df['Gender'] == 'Male') & (df['Smoking_History'] == 'Yes')]

# print(rural_data_male.count())

# Data for where Urban data and Gender is male and where there is smoking history is 3187.

# Data for where Urban data and Gender is male and where there is smoking history is 1355.

# There are more urban male smokers than rural male smokers.

urban_data_female = df[(df['Region'] == 'Urban') & (df['Gender'] == 'Female') & (df['Smoking_History'] == 'Yes')]

rural_data_female = df[(df['Region'] == 'Rural') & (df['Gender'] == 'Female') & (df['Smoking_History'] == 'Yes')]

# print(rural_data_female.count())

# Data for where Urban data and Gender is female and where there is smoking history is 3109.

# Data for where Rural data and Gender is female and where there is smoking history is 1346.

# There are more urban female smokers than rural female smokers.

alcohal_consumer_male_high = df[(df['Gender'] == 'Male') & (df['Alcohol_Consumption'] == 'High')] #2905

alcohal_consumer_male_mod = df[(df['Gender'] == 'Male') & (df['Alcohol_Consumption'] == 'Moderate')] #6138

alcohal_consumer_male_low = df[(df['Gender'] == 'Male') & (df['Alcohol_Consumption'] == 'Low')] #4555

# print(alcohal_consumer_male_mod)

# Modeate alcohal consumers are more prone to heart attacks than High Alcohal Consumers. Hierarchy is Moderate > Low > High (Male)

alcohal_consumer_female_high = df[(df['Gender'] == 'Female') & (df['Alcohol_Consumption'] == 'High')] #2923

alcohal_consumer_female_mod = df[(df['Gender'] == 'Female') & (df['Alcohol_Consumption'] == 'Moderate')] #5921

alcohal_consumer_female_low = df[(df['Gender'] == 'Female') & (df['Alcohol_Consumption'] == 'Low')] #4543

# print(alcohal_consumer_female_low)

# Modeate alcohal consumers are more prone to heart attacks than High Alcohal Consumers. Hierarchy is Moderate > Low > High (Female)

# Minimum, Maximum, and Average Age of Smoking Males

min_age_male = np.min(smoking_history_male['Age'])

max_age_male = np.max(smoking_history_male['Age'])

avg_age_male = np.mean(smoking_history_male['Age'])

# print(avg_age_male.round(2))

# Minimum, Maximum, and Average Age of Smoking Females

min_age_female = np.min(smoking_history_female['Age'])

max_age_female = np.max(smoking_history_female['Age'])

avg_age_female = np.mean(smoking_history_female['Age'])

# print(avg_age_female.round(2))