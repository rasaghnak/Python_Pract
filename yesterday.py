from datetime import datetime, timedelta

def yesterday(date) -> str:
    input_date = datetime.strptime(date, '%Y-%m-%d')
    yesterday_date = input_date - timedelta(days=1)
    return yesterday_date.strftime('%Y-%m-%d')


if __name__ == "__main__":
    args = input("Enter a date (YYYY-MM-DD): ")
    print("Yesterday's date is:", yesterday(args))