import time
import calendar  as ca
import pandas as pd 
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    city= input("Please type the name of your city: 1-  chicago 2- for New York 3- for washington ").lower()
    while city not in CITY_DATA.keys():
         print ("there is somthing wrong .. please type a valid city")
         city= input("Please type the name of your city: 1-  chicago 2- for New York 3- for washington ").lower()      


    # TO DO: get user input for month (all, january, february, ... , june)
    
    months= ['january','february', 'march', 'april', 'may', 'june', 'all'] #months list 
    while True: 
      month = input("type the month").lower()
      if month  in months:
           break
      else:
           print("There is somthing wrong .. please check")
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  
    while True:
       
        day = input("type the day").lower()
        if day  in  days:
            break
        else:
            print("There is somthing wrong .. please check")

   

     #Returning the city, month and day selections

    print('-'*10)
    return city, month, day

def load_data(city, month, day):


    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.hour

# for filtering 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f"Most popular month  from January to June is {popular_month}")

    # TO DO: display the most common day
    popular_day = df['day_of_week'].mode()[0]
    print(f"Most popular day is {popular_day}")

      # the most popular hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print(f"Most Popular start hour is  {popular_hour}")

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # the most common start station
    start_station = df['Start Station'].mode()[0]

    print(f"The most Popular start station: {start_station}")

    #Uses mode method to find the most common end station
    end_station = df['End Station'].mode()[0]

    print(f"The most Popular used end station: {end_station}")
    
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print(f"{combo}.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()

    print(f"The types of users : {user_type}")

    # TO DO: Display counts of gender
    
    gender = df['Gender'].value_counts()
    print(f"The types of gender  : {gender}")


    # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest = int(df['Birth Year'].min())
    most_recent = int(df['Birth Year'].max())
    common_year = int(df['Birth Year'].mode()[0])
    print(f" the earliest year of birth: {earliest} & the most recent year of birth: {most_recent} & The most common year of birth: {common_year}")


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
            print("Thank you !")
            break


if __name__ == "__main__":
	main()


