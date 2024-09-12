import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = df.groupby(['race']).count().iloc[:,0]

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == "Male"]['age'].agg('mean'), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100 * len(df[df['education']=='Bachelors'])/len(df), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round(100* len(higher_education[higher_education['salary']=='>50K']) / len(higher_education), 1)
    lower_education_rich = round(100* len(lower_education[lower_education['salary']=='>50K']) / len(lower_education), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == df['hours-per-week'].min()])

    rich_percentage = round(100 * len(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')]) / num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_count = df[(df['salary'] == '>50K') & (df['native-country'] != "?")].groupby(['native-country']).count().iloc[:,0].to_frame("count")
    country_count = df[df['native-country'] != "?"].groupby(['native-country']).count().iloc[:,0].to_frame("count")

    highest_earning_country = (rich_count/country_count).idxmax().iloc[0]
    highest_earning_country_percentage = round((rich_count/country_count).max().iloc[0] * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby('occupation').count().iloc[:,0].idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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


# df = pd.read_csv("adult.data.csv")
# races = df.groupby(['race']).count().iloc[:,0]
# average_age_men = None
# print(df.head(10))
# print(df.dtypes)
# print(100 * len(df[df['education']=='Bachelors'])/len(df))
# # print(df.groupby(['sex']).count().iloc[:,0])
# # print(df[df['sex'] == "Male"]['age'].agg('mean'))
# print(df[df['education'].isin(['Bachelors','Masters','Doctorate'])])
# print(df[~df['education'].isin(['Bachelors','Masters','Doctorate'])])

# higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
# lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

# # percentage with salary >50K
# higher_education_rich = 100* len(higher_education[higher_education['salary']=='>50K']) / len(df)
# lower_education_rich = 100* len(lower_education[lower_education['salary']=='>50K']) / len(df)
# print(higher_education_rich, lower_education_rich)
# print(len(df))
# print(df[df['hours-per-week'] == df['hours-per-week'].min()])
# num_min_workers = len(df[df['hours-per-week'] == df['hours-per-week'].min()])

# rich_percentage = 100 * len(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')]) / num_min_workers
# print(rich_percentage)

# print(df.dtypes)
# rich_count = df[(df['salary'] == '>50K') & (df['native-country'] != "?")].groupby(['native-country']).count().iloc[:,0].to_frame("count")
# country_count = df[df['native-country'] != "?"].groupby(['native-country']).count().iloc[:,0].to_frame("count")
# print(rich_count, country_count)
# print((rich_count/country_count).idxmax().iloc[0])
# print((rich_count/country_count).max().iloc[0] * 100)


# print(pd.melt(df[df['salary'] == '>50K'], value_vars=['native-country']))

# print(df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby('occupation').count().iloc[:,0].idxmax())

