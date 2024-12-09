import random
from datetime import datetime, timedelta
import csv
import calendar

# Define mentor assignments for each weekday (1=Monday, 7=Sunday)
mentors_by_weekday = {
    1: [10905, 10902, 10901, 11204],  # Monday
    2: [10803, 10902, 11301, 11304],  # Tuesday
    3: [10804, 10905, 11301, 11304],  # Wednesday
    4: [10804, 11104, 11203, 11103],  # Thursday
    5: [10904, 10803, 10902, 10901, 11303],  # Friday
    6: [10804, 10905, 11004, 11104],  # Saturday
    7: [11103, 10803, 11201, 11303, 11302],  # Sunday
}

# Generating 200 random reservation entries with student_id between s_2023001 and s_2023316
reservation = []
for i in range(200):
    # Generate random student_id between s_2023001 and s_2023316
    student_id = f"s_{str(random.randint(2021,2023))}{str(random.randint(1, 167)).zfill(3)}"
    
    # Generate random timestamp for different years
    if student_id.startswith('s_2021'):
        year = 2021
    elif student_id.startswith('s_2022'):
        year = 2022
    else:
        year = 2023
    
    month = random.randint(1, 12)
    
    # Get the number of days in the month
    _, last_day_of_month = calendar.monthrange(year, month)
    
    # Generate a valid random day in that month
    day = random.randint(1, last_day_of_month)
    
    # Generate a base_date with a valid day of the month
    base_date = datetime(year, month, day)
    
    # Generate random time within the day
    random_time = base_date + timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    
    # Generate a reservation_id (3 digits)
    reservation_id = str(i + 1).zfill(3)
    
    # Get the weekday of the random_time (1=Monday, 7=Sunday)
    weekday = random_time.weekday() + 1  # weekday() returns 0=Monday, 6=Sunday, so +1 to match 1-7
    
    # Select a mentor from the corresponding weekday's list
    mentor_id = random.choice(mentors_by_weekday[weekday])
    
    # Format the time to include weekday, e.g., "Monday, 2024-12-01 12:30:45"
    time = random_time.strftime("%Y-%m-%d %H:%M:%S")  # %A for full weekday name
    
    # Append the reservation data as a list of fields
    reservation.append([reservation_id, time, student_id, mentor_id])

# Writing to CSV
with open('reservation_1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["reservation_id", "timestamp", "student_id", "mentor_id"])  # Write header
    writer.writerows(reservation)  # Write reservation data

print("Data has been written to 'reservation_1.csv'")
