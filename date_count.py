import datetime

def get_days_from_today(date):
    try:
        get_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.datetime.today()

        date_difference = (current_date - get_date)

        return date_difference 
    except ValueError:
        return "Invalid date format"
    

print(get_days_from_today("2024-04-20"))
