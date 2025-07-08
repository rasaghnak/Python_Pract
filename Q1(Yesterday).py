# #Description
# Write Python code that implements a function named yesterday. This function will get the date of the day before the incoming date, and finally return that date.

# Write the code for the yesterday function in solution.py, and we will run your code in main.py by importing it to check if it does the above correctly.

from datetime import datetime, timedelta

def yest_date(today)-> datetime:
  yesterday = today - timedelta(days=1)
  return yesterday 
