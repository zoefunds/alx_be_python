from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates the future date, and prints it.
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
        return future_date
    except ValueError:
        print("Invalid input. Please enter an integer value for days.")
        return None

if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)