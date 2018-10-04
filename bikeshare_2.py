import time
import pandas as pd
import numpy as np
import os
CITY_DATA = { 'chicago': 'F:/data/sam/chicago.csv',
              'new york city': 'F:/data/sam/new_york_city.csv',
              'washington': 'F:/data/sam/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities=['Chicago','New York City','Washington']
    while True:
        city=input("City:")
        if city.title() in cities:
            city = city.lower()
            break# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
        month=input("month:")# get user input for month (all, january, february, ... , june)
        if month.lower() == 'january':
            month=month.lower()
            break
        elif month.lower() == 'february':
            month=month.lower()
            break
        elif month.lower() == 'march':
            month=month.lower()
            break
        elif month.lower() == 'april':
            month=month.lower()
            break
        elif month.lower() == 'may':
            month=month.lower()
            break
        elif month.lower() == 'june':
            month=month.lower()
            break
        elif month.lower() =='all':
            month=month.lower()
            break
        else:
            print('that is no valid input . Please mind your spelling')


    while True:
        day=input("day:")# get user input for day of week (all, monday, tuesday, ... sunday)
        if day.lower() == 'sunday':
            day=day.lower()
            break
        elif day.lower() == 'monday':
            day=day.lower()
            break
        elif day.lower() == 'tuesday':
            day=day.lower()
            break
        elif day.lower() == 'wednesday':
            day=day.lower()
            break
        elif day.lower() == 'thursday':
            day=day.lower()
            break
        elif day.lower() == 'friday':
            day=day.lower()
            break
        elif day.lower() == 'saturday':
            day=day.lower()
            break
        elif day.lower() == 'all':
            day=day.lower()
        else:
            print("print valid data")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]




    return df
def load_data1(city, month, day):
    df1= pd.read_csv(CITY_DATA[city])
    return df1

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]


    print('most Popular month:',popular_month)
    print('most popular day:', popular_day)
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    strt = df['Start Station'].mode()[0]
    print('start station',strt)


    # display most commonly used end station
    endst = df['End Station'].mode()[0]
    print('END STATION:',endst)


    # display most frequent combination of start station and end station trip
    df['combine']=df['Start Station']+'  to  '+df['End Station']
    print(df['combine'].mode()[0])




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print("total:",float(total))


    # display mean travel time
    menavr = df['Trip Duration'].mean()
    print("mean:",float(menavr))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("count of differnt user:",user_types.to_frame())
    user_types = df['User Type'].value_counts()


    # Display counts of gender

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("counts of gender:",gender.to_frame())
    else:
        print("washington does not have gender info")


    # Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        early = df['Birth Year'].min()
        print("early birth:",int(early))
        recent = df['Birth Year'].max()
        print("recent birth:",int(recent))
        common_birth = df['Birth Year'].mode()
        print("common year:",int(common_birth))
    else:
        print("washington does not have gender info")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    s=df.sample(n=7)
    print(s)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df1 = load_data1(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df1)


        restrt = input('\n Would you like to view individual data ? enter yes or no\n')
        if restrt.lower() == 'yes':
            display_data(df1)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
