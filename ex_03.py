"""
Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних
у форматі ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік.
Перетворене значення функція повертає під час виклику.
"""

from datetime import datetime


def get_str_date(date):
    date_list = date[:10].split('-')
    date_in = datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]))
    
    return date_in.strftime('%A %d %B %Y')


print(get_str_date('2021-05-27 17:08:34.149Z'))
   