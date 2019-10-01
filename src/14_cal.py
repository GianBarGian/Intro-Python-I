"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

calendar = calendar.TextCalendar(calendar.MONDAY)
current_time = datetime.now()
year = int(current_time.strftime('%Y'))
month = int(current_time.strftime('%-m'))
if len(sys.argv) == 1:
    current = calendar.formatmonth(year, month)
    print(current)
elif len(sys.argv) == 2:
    try:
        if int(sys.argv[1]) < 0 or int(sys.argv[1]) > 13:
            print('The first argument should be an int from 1 to 12 for the month')
        else:
            month = int(sys.argv[1])
            current = calendar.formatmonth(year, month)
            print(current)
    except ValueError:
        print('It should be an int')
elif len(sys.argv) == 3:
    try:
        if int(sys.argv[2]) < 1000 or int(sys.argv[2]) > 9999:
            print('The second argument should be an int yyyy for the year')
        else:
            month = int(sys.argv[1])
            year = int(sys.argv[2])
            current = calendar.formatmonth(year, month)
            print(current)
    except ValueError:
        print('It should be an int')
else:
    print('This script takes 2 optional arguments\nAn int from 1 to 12 for the month\nAn int yyyy for the year\nIf no args are provided it default at hte current month')
