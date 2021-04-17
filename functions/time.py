import datetime
import pytz
import json

with open('time_zones.json', 'r') as f:                                                                                 # Opening time_zones.json as variable 'f'.
    time_zones = json.load(f)                                                                                           # Assigning the dictionary of time_zones.json to variable 'time_zones'.

# This is where the GUI (PyQt5) code will be.

today_date = datetime.date.today()                                                                                      # Assigning current date to variable 'today_date'.
today_year = today_date.year                                                                                            # Assigning current year to variable 'today_year'.
month = today_date.month                                                                                                # Assigning current month (number form) to variable 'month'.
today_day = today_date.day                                                                                              # Assigning current day to variable 'today_date'.
months = {                                                                                                              # A dictionary called 'months', assigning number values to their corresponding month names.
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
today_month = months[str(month)]                                                                                        # Assigning current date from 'months' dictionary to variable 'today_month'.

days_of_the_week = {                                                                                                    # A dictionary called 'days_of_the_week', assigning number values to their corresponding days of the week. 0 is Monday and 6 is Sunday.
    "0": "Monday",
    "1": "Tuesday",
    "2": "Wednesday",
    "3": "Thursday",
    "4": "Friday",
    "5": "Saturday",
    "6": "Sunday"
}
today_day_of_week = days_of_the_week[str(today_date.weekday())]                                                         # Assigning current day of the week from 'days_of_the_week' dictionary to variable 'today_day_of_week'.

print(f'Hello Rishil. It is {today_day_of_week}, {today_month} {today_day}, {today_year}.')

if month > 4 or today_month == 4 and today_day > 25:                                                                    # If my birthday has already passed this year...
    birthday_year = today_year + 1                                                                                      # birthday_year will be set for next year.
else:                                                                                                                   # If my birthday has not passed this year...
    birthday_year = today_year                                                                                          # birthday_year will be set for this year.

birthday = datetime.date(birthday_year, 4, 25)                                                                          # Set my birthday as April 25th, birthday_year as a variable called birthday.
days_until_birthday = birthday - today_date                                                                             # days_until_birthday is a timedelta showing current day to birthday.
untilBirthday = days_until_birthday.days                                                                                # untilBirthday is a variable showing number of days left from the current day to my birthday.

if month == 12 and today_day > 25:                                                                                      # If Christmas has already passed this year...
    christmas_year = today_year + 1                                                                                     # christmas_year will be set for next year.
else:                                                                                                                   # If Christmas has not passed this year...
    christmas_year = today_year                                                                                         # christmas_year will be set for this year.

christmas = datetime.date(christmas_year, 12, 25)                                                                       # Set Christmas as December 25th, christmas_year as a variable called christmas.
days_until_christmas = christmas - today_date                                                                           # days_until_christmas is a timedelta showing current day to Christmas.
untilChristmas = days_until_christmas.days                                                                              # untilChristmas is a variable showing number of days left from the current day to Christmas.
