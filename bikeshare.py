import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for chicago, new york city, or washington?').lower()
    while city not in CITY_DATA:
        city = input('Please enter a VALID city name: chicago, new york city, or washington?').lower()
        # print('Please enter a VALID city name')
        continue


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Would you like to filter the data by  month (all, january, february, ... , june)?').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Would you like to filter the data by day of week (all, monday, tuesday, ..., friday)?').lower()


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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # to see 5 lines of raw data
    to_see = input('Would you like to see to see 5 lines of raw data? Enter yes or no:')
    strt = 0
    stp = 5
    while to_see == 'yes':
        print(df[st:sp].head())
        to_see = input('Would you like to see to see  another 5 lines of raw data? Enter yes or no:')
        strt += 5
        stp += 5
        continue
    
        
        
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week  and start hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour
    
    # filter by month to create the new dataframe
    if month != 'all':
        # use index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june'] 
        month = months.index(month) + 1
        
        # filtter by month to create the new dataframe
        df = df[df['month'] == month]
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common Month is: ', most_common_month)


    # TO DO: display the most common day of week
    most_common_doy = df['day_of_week'].mode()[0]
    print('The most common day of the week is: ', most_common_doy)


    # TO DO: display the most common start hour
    most_common_hour = df['start_hour'].mode()[0]
    print('The most common start hour is:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is:', df[['Start Station','End Station']].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('{} is the total time of travel'.factor(total_travel_time))
 

    # TO DO: display mean travel time
    print('Average total travel time is:', total_travel_time / len(df))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].count()
    print('Counts of user types:', count_user_types)
    
    
    if 'Gender' in df:
        # TO DO: Display counts of gender
        count_gender = df['Gender'].count()
        print('Counts of gender:', count_gender)
        
    if 'Birth Year' in df:
         # TO DO: Display earliest, most recent, and most common year of birth
         e_birth_year = df['Birth Year'].min()
         r_birth_year = df['Birth Year'].max()
         c_birth_year = df['Birth Year'].mode()[0]
         print('Ealiest, most recent and most common birth year are : {}, {}, and {} respectively'
               .format(e_birth_year, r_birth_year, c_birth_year))
               
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
