import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    formatted_phone = re.sub(r'\D', '', phone_number)

    if formatted_phone.startswith('380'):
        formatted_phone = '+' + formatted_phone
        if '380' not in formatted_phone:
            formatted_phone = '+380' + formatted_phone
        elif formatted_phone.startswith('0'):
            formatted_phone = '+38' + formatted_phone
    else:
        formatted_phone = '+38' + formatted_phone

    return formatted_phone
      

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#дякую тепер я головна хейтерка цього завдання