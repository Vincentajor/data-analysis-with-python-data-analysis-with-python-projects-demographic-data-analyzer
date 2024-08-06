import numpy as np
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv ("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df["sex"] == "Male","age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    mask = df["education"] == "Bachelors"
    percentage_bachelors = np.float64(100 * len(df[mask]) / df.shape [0]).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    snd_mask = df["education"].isin(["Bachelors","Masters","Doctorate"])
    higher_education = df[snd_mask]
    lower_education = df[~snd_mask]

    # percentage with salary >50K
    higher_education_rich = np.float64(100 * len (higher_education[higher_education["salary"] == ">50k"]) / higher_education.shape[0]).round(1)
    lower_education_rich = np.float64(100 * len (lower_education[lower_education["salary"] == ">50k"]) / lower_education.shape[0]).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-weeek"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = np.float64(100 * len (num_min_workers[num_min_workers["salary"] == ">50k"]) / num_min_workers.shape[0]).round(1)

    # What country has the highest percentage of people that earn >50K?
    max_rich_country_percentage = 0.00 
    highest_earning_country = None

    for country in df["native-country"].value_counts().index:
        current_country_people = df[df["native-country"] == country]
        current_country_rich = np.float64(100 * len (current_country_people[current_country_people["salary"] == ">50k"]) / current_county_people.shape[0]).round(1)
        if current_country_rich > max_rich_country_percentage:
            max_rich_country_percentage = current_country_rich
            highest_earning_country = country

    highest_earning_country_percentage = max_rich_country_percentage


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50k")]["occupation"].value_counts(sorted).index[0]

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
