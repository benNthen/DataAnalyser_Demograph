import pandas as pd
import csv
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('../DataAnalyser_Demograph/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df['race'].values

    race_list = np.unique(race).tolist()

    race_occ = {}

    for word in enumerate(race_list):

        race_num = 0

        for a in race:

            if (a == word[1]):
                race_num += 1

        race_occ[word[1]] = race_num

    val = list(race_occ.values())

    v2 = sorted(val, reverse=True)

    race_count = v2

    # What is the average age of men?
    df1 = (df[['age', 'sex']])

    df2 = df1.loc[df1['sex'] == 'Male', 'age']
    average_age_men = np.around(df2.mean(), decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    bach_only = df[df['education'] == 'Bachelors']

    num_bach = len(bach_only)

    def percentage(part, whole):
        Percentage = 100 * float(part) / float(whole)
        Answer = round(Percentage, 1)
        return Answer

    percentage_bachelors = percentage(num_bach, len(df))

    edu_salary = (df[['education', 'salary']]).values # extracts education and salary columns

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    highED_high = 0
    highED_low = 0
    highED_size = 0

    # What percentage of people without advanced education make more than 50K?
    lowED_high = 0
    lowED_low = 0
    lowED_size = 0

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    for a, b in edu_salary:
        if (a == 'Bachelors') or (a == 'Masters') or (a == 'Doctorate'):
            highED_size += 1

            if b == '>50K':
                highED_high += 1
        else:
            lowED_size += 1

            if b == '>50K':
                lowED_high += 1

    higher_education = percentage(highED_low, highED_size)
    lower_education = percentage(lowED_low, lowED_size)

    # percentage with salary >50K
    higher_education_rich = percentage(highED_high, highED_size)
    lower_education_rich = percentage(lowED_high, lowED_size)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    w = (df[['hours-per-week', 'salary']]).values

    min_hours = min(w, key=lambda x: x[0])

    min_work_hours = min_hours[0]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    total_min = 0

    num_min = 0

    for i in w:
        if i[0] == min_hours[0]:
            total_min += 1

            if i[1] == '>50K':
                num_min += 1

    num_min_workers = total_min

    rich_percentage = percentage(num_min, num_min_workers)

    # What country has the highest percentage of people that earn >50K?
    country = (df[['native-country']]).values
    count_list = np.unique(country).tolist()
    count_sal = (df[['native-country', 'salary']]).values
    country_p = {}

    for word in enumerate(count_list):

        country_num = 0
        country_rich = 0

        for a, b in count_sal:

            if (a == word[1]):

                if (b == '>50K'):
                    country_rich += 1
                else:
                    country_num += 1

        total = country_rich + country_num

        cp = percentage(country_rich, total)

        country_p[word[1]] = cp

    max_country = max(country_p, key=country_p.get)

    highest_earning_country = max_country
    highest_earning_country_percentage = country_p[max_country]

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[df['native-country'] == 'India']

    india2 = india[india['salary'] == '>50K']

    india3 = india2[['occupation', 'salary']].values

    occp_list = np.unique(india2[['occupation']]).tolist()

    occupation = {}

    for word in enumerate(occp_list):

        occur = 0

        for a, b in india3:

            if (a == word[1]):
                occur += 1

        occupation[word[1]] = occur

    top_IN_occupation = max(occupation, key=occupation.get)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country_percentage)
        print(f"Highest percentage of rich people in country: {highest_earning_country}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
