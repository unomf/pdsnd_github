import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'NewYork': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def user_inputs(input_str,input_type):
    while True:
        input_check = input(input_str).title()
        try:
            if input_check in ["Chicago", "NewYork", "Washington"] and input_type == 1:
                break
            elif input_check in ["January", "February", "March", "April", "May", "June", "All"] and input_type == 2:
                break
            elif input_check in ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "All"] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print("Invalid input: Please pick from the defined cities\n")
                    
                if input_type == 2:
                    print("Invalid input: Please choose a correct month or write All\n")
                    
                if input_type == 3:
                    print("Invalid input: Please choose a correct day or write All\n")
            
            
        except Exception as e:
            print("Oops something is not right: {}".format(e))
            
    return input_check

def get_filters():
    
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = user_inputs("Pick a city please: 'Chicago', 'NewYork', 'Washington':\n", 1)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = user_inputs("Choose a month from 'January to June' or write All:\n", 2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = user_inputs("Now pick a day from 'Saturday to Friday' or write All\n", 3)

    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

# find the most popular month
    print('The most popular month is:', df['month'].mode()[0])

    # TO DO: display the most common day of week


# find the most popular day of weekn
    print('The most popular weekday is:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    

# find the most popular hour

    print('The most popular start hour is:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station_used = df['Start Station'].mode()[0]
    print('The most used start station is:\n', most_start_station_used)

    # TO DO: display most commonly used end station
    most_end_station_used = df['End Station'].mode()[0]
    print('The most used end station is:\n', most_end_station_used)

    # TO DO: display most frequent combination of start station and end station trip
    start_end = df.groupby(['Start Station', 'End Station'])
    start_end_combined = start_end.size().sort_values(ascending = False).head(1)
    print('The most combined start-end station is:\n', start_end_combined) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total time of travel is:', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The mean time of travel is:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Here is the count of users types:\n', user_type)

    # TO DO: Display counts of gender
    if city != 'Washington':
        gender_count = df['Gender'].value_counts()
        print('Here is the count of gender:\n', gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth:
    
    # Common birth year:
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year is:\n', common_birth_year)
        
        # Most recent:
        most_recent_year = df['Birth Year'].max()
        print('The most recent year is:\n', most_recent_year)
        
        # Earliest year:
        earliest_year = df['Birth Year'].min()
        print('The earliest year is:\n', earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()