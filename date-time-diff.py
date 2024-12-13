from datetime import datetime

def get_valid_date_time_input(prompt):
    while True:
        date_time_input = input(prompt)
        try: 
            # Attempt to parse the input into a datetime object
            datetime.strptime(date_time_input, "%m/%d/%Y %H:%M")
            return date_time_input
        except ValueError:
            print("Invalid input! Check formatting.")

while True:
    # Input format: MMDDYYYY HHMM MMDDYYYY HHMM
    start_date_time = get_valid_date_time_input("Enter the start date and 24 HR time (in the format MM/DD/YYY HH:MM): ")
    end_date_time = get_valid_date_time_input("Enter the end date and 24 HR time (in the format MM/DD/YYY HH:MM): ")

    # Parse input strings into datetime objects
    start_datetime = datetime.strptime(start_date_time, "%m/%d/%Y %H:%M")
    end_datetime = datetime.strptime(end_date_time, "%m/%d/%Y %H:%M")

    # Calculate the time difference
    time_difference = end_datetime - start_datetime

    # Calculate total hours rounded down to the nearest hour
    total_hours = (time_difference.total_seconds() / 3600)

    # Extract days and remaining seconds
    days = time_difference.days
    total_hours_rounded = round(total_hours, 3)

    print(f"\n***************************")
    print(f"Total Time Difference:")
    print(f"Days: {days}")
    print(f"Hours: {total_hours_rounded}")
    print(f"***************************")

    # Ask the user if they want to run the program again
    try:
        input("\nPress Enter to run again. CTRL+C to quit.")
    except KeyboardInterrupt:
        print("Program terminated.")
        break  # Exit the program if the user presses CTRL+C