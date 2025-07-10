# #Description
# Write Python code that implements a function named yesterday. This function will get the date of the day before the incoming date, and finally return that date.

# Write the code for the yesterday function in solution.py, and we will run your code in main.py by importing it to check if it does the above correctly.

from datetime import datetime, timedelta

def yest_date(today)-> datetime:
  yesterday = today - timedelta(days=1)
  return yesterday 

# Description
# The exams records of students are stored in the exam table
# Please use SQL statement to find the student_id corresponding to the student with the largest number of failed subjects.

# Table definition: exams

# columns_name	type	explaination
# id	int unsigned	primary key
# student_id	int	student's id
# date	date	date of exam
# is_pass	int	grade status (0 means fail, others means pass)


SELECT student_id
FROM exams
WHERE is_pass = 0
GROUP BY student_id
HAVING COUNT(*) = (
        SELECT COUNT(*)
        FROM exams
        WHERE is_pass = 0
        GROUP BY student_id
        ORDER BY COUNT(*) DESC
        LIMIT 1
);
