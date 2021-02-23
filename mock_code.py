import csv
import pandas as pd
import numpy as np

pd.set_option('display.width', None)

df = pd.read_csv('../DataAnalyser_Demograph/adult.data.csv')

# print(df)

# Question 1
# #extract race dataframe
race = df['race'].values

race_list = np.unique(race).tolist()

race_occ = {}

for word in enumerate(race_list):

    race_num = 0

    for a in race:

        if(a==word[1]):
          race_num += 1

    race_occ[word[1]] = race_num

# val = list(race_occ.values())

ans = race_occ.values()

print(ans.tolist())

# # convert the set to the list
# unique_list = (list(list_set))
#
# # print how many elements are in the list
# race_num = len(unique_list)
#
# print(race_num.tolist())

# #Question 2
# #extract race dataframe
# df1 = (df[['age', 'sex']])
#
# df2 = df1.loc[df1['sex'] == 'Male', 'age']
#
# average_age_men = np.around(df2.mean(), decimals=1)
#
# print(average_age_men)

# #Question 3
# #extract education(the one w/Bachelors) from dataframe
# bach_only = df[df['education'] == 'Bachelors']
#
# num_bach = len(bach_only)

def percentage(part, whole):
    Percentage = 100 * float(part) / float(whole)
    Answer = round(Percentage, 1)
    return Answer

# print(percentage(num_bach, len(df)))

# #Question 3
# #extract education(the one w/Bachelors) from dataframe
# array = df.iloc[:, 3].values
#
# edu_salary = (df[['education', 'salary']]).values
#
# highED_high = 0
# highED_low = 0
# highED_size = 0
#
# lowED_high = 0
# lowED_low = 0
# lowED_size = 0
#
# for a, b in edu_salary:
#    if (a == 'Bachelors') or (a == 'Masters') or (a == 'Doctorate'):
#        highED_size += 1
#
#        if b == '>50K':
#           highED_high += 1
#    else:
#        lowED_size += 1
#
#        if b == '>50K':
#           lowED_high += 1
#
# # Calculate percentage of higher ed that earns more than 50K
# higher_education_rich = percentage(highED_high, highED_size)
#
# print("Highly educated people who earn more than 50K:", higher_education_rich)
#
# # Calculate percentage of lower ed that earns more than 50K
# lower_education_rich = percentage(lowED_high, lowED_size)
#
# print("Lowly educated people who earn more than 50K:", lower_education_rich)

#Question 4
# Min num of hours per week

# c = (df[['hours-per-week', 'salary']]).values
#
# min_value = min(c, key=lambda x: x[0])
#
# print(min_value[0])

# total_min = 0
#
# num_min = 0
#
# for a in c:
#    if a[0] == min_value[0]:
#        total_min +=1
#
#        if a[1] == '>50K':
#            num_min +=1

# print(total_min)
#
# print(percentage(num_min, total_min))

# #Question 5
# country has the highest percentage of people that earn >50K?

# country = (df[['native-country']]).values
#
# count_list = np.unique(country).tolist()
#
# # print(count_list)
# count_sal = (df[['native-country', 'salary']]).values
#
# country_p = {}
#
# for word in enumerate(count_list):
#
#     country_num = 0
#     country_rich = 0
#
#     for a, b in count_sal:
#
#         if(a== word[1]):
#
#             if(b == '>50K'):
#                 country_rich += 1
#             else:
#                 country_num += 1
#
#     total = country_rich + country_num
#
#     cp = percentage(country_rich, total)
#
#     country_p[word[1]] = cp
#
# max_country = max(country_p, key=country_p.get)
#
# print(max_country)

# print(country_p[max_country])

# #Question 6
# # Most popular occupation in India that earns >50K
# india = df[df['native-country'] == 'India']
#
# india2 = india[india['salary'] == '>50K']
#
# india3 = india2[['occupation', 'salary']].values
#
# occp_list = np.unique(india2[['occupation']]).tolist()
#
# occupation = {}
#
# for word in enumerate(occp_list):
#
#     occur = 0
#
#     for a, b in india3:
#
#         if(a== word[1]):
#             occur += 1
#
#     occupation[word[1]] = occur
#
# top_IN_occupation = max(occupation, key=occupation.get)
#
# print(top_IN_occupation)