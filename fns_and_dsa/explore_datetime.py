from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    formatted_current = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current}")

    def calculate_future_date():
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            future_date = current_datetime + timedelta(days=days)
            formatted_future = future_date.strftime("%Y-%m-%d")
            print(f"Future date: {formatted_future}")
        except ValueError:
            print("Please enter a valid number.")

    calculate_future_date()

# Call the function
display_current_datetime()
