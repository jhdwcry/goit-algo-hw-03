from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 7:
            
            if birthday.weekday() >= 5: 
                days_until_birthday += (7 - birthday.weekday())

            congratulation_date = today + timedelta(days=days_until_birthday)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "Ivan", "birthday": "2024.04.25"},
    {"name": "Mary", "birthday": "2024.04.30"},
    {"name": "Anna", "birthday": "2024.05.02"},
    {"name": "Petro", "birthday": "2024.05.05"},
    {"name": "Olena", "birthday": "2024.05.06"},
    {"name": "Julia", "birthday": "2024.05.07"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)