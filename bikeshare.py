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
    city=input("choose a city name from this list: (chicago, new york city, washington)\n")
    while city.lower() not in ("chicago", "new york city", "washington"):
        city=input("please enter a valid city name from this list: (chicago, new york city, washington)\n")
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("choose a month to filter data with from january to june, if no filter required type all\n")
    while month.lower() not in ("january", "february", "march", "april", "may", "june","all"):
        month=input("please enter a valid choice from this list: (january, february, march, april, may, june, all)\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("choose a day to filter data with from monday to sunday, if no filter required type all\n")
    while day.lower() not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"):
       day=input("please enter a valid choice from this list: (monday, tuesday, wednesday, thursday, friday, saturday, sunday, all)\n")

    print('-'*40)
    city= city.lower()
    month= month.lower()
    day= day.lower()
    return city, month, day


def load_data(city, month, day):
    
     df = pd.read_csv(CITY_DATA[city])
        
     df['Start Time'] =  pd.to_datetime(df['Start Time'])

     df['month'] = df['Start Time'].dt.month
        
     df['day'] = df['Start Time'].dt. day_name()
    
     df['hour'] = df['Start Time'].dt.hour
     
     if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

     if day != 'all':
        
         df = df[df['day'] == day.title()]
    
     """
     Loads data for the specified city and filters by month and day if applicable.

     Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
     Returns:
        df - Pandas DataFrame containing city data filtered by month and day
     """
     return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = round(time.time(),4)

    # TO DO: display the most common month
    month= df['month'].unique()
    if len(month)>1 :
    
     Fr_month= df['month'].mode()[0]-1
     months = ['january', 'february', 'march', 'april', 'may', 'june']
     Fr_month_name = months[Fr_month]
    
     print("most frequent month is {}.".format(Fr_month_name).title()) 
    

    # TO DO: display the most common day of week
    day= df['day'].unique()
    if len(day)>1 :
    
     Fr_day= df['day'].mode()[0]
    
     print("most frequent day is {}.".format(Fr_day))

    # TO DO: display the most common start hour
    Fr_hour= df['hour'].mode()[0]
    print("most frequent hour is {}.".format(Fr_hour))

    print("\nThis took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Fr_start_station= df['Start Station'].mode()[0]
    print("The most commonly used start station is {}.".format(Fr_start_station))

    # TO DO: display most commonly used end station
    Fr_end_station= df['End Station'].mode()[0]
    print("The most commonly used end station is {}.".format(Fr_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']= "from " + df['Start Station'] + " to " + df['End Station']
    Fr_combination= df['combination'].mode()[0]
    print("The most commonly used combination is {}.".format(Fr_combination))

    print("\nThis took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time= df['Trip Duration'].sum()
    print("the total travel time is {} in seconds and {} in minutes.".format(total_time,round(total_time/60,2)))

    # TO DO: display mean travel time
    mean_time= df['Trip Duration'].mean()
    print("the total mean time is {} in seconds and {} in minutes.".format(round(mean_time,2),round(mean_time/60,2)))

    print("\nThis took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    print("users types count is:\n{}.".format(user_types))
    print("\n")

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        user_gender= df['Gender'].value_counts()
        print("users Genders count is:\n{}.".format(user_gender))
    else: print("Gender Data not available")
    print("\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        early_BY= int(df['Birth Year'].min())
        recent_BY= int(df['Birth Year'].max())
        common_BY= int(df['Birth Year'].mode()[0])
        print("The earliest Birth year is: {} \nThe most recent Birth year is: {} \nThe most common Birth year is: {}".format(early_BY,recent_BY,common_BY))
    else: print("Birth Year Data not available")


    print("\nThis took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)

def input_raw(df):
    
    """displays 5 rows of raw input upon replying yes until the values end or user reply no"""
    i=0
    while i< len(df):
            raw_data = input("Do you need raw data? Enter yes or no\n")
            while (raw_data != "yes") and (raw_data != "no"):
                  raw_data = input("pleas insert yes or no\n")
                
            if raw_data.lower() != 'yes':
                  break
            else:
                print(df[i:i+5])
                i+=5      
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        input_raw(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while (restart != "yes") and (restart != "no"):
            restart = input("pleas insert yes or no\n")
        if restart.lower() != 'yes':
                  break


if __name__ == "__main__":
	main()
