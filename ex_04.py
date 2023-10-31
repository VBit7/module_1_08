"""
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами,
що випали випадковим чином і в певному діапазоні під час чергового тиражу.
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Напишіть функцію, яка випадково підбиратиме набір чисел для лотерейного квитка. Серед цих чисел не має бути дублікатів.

Формат функції get_numbers_ticket(min, max, quantity), де параметри:

min - мінімальне значення діапазону, не може бути менше 1
max - максимальне значення діапазону, не може бути більше 1000
quantity - кількість чисел у наборі (має бути min < quantity < max)
Функція повинна повернути перелік випадкових чисел за зростанням.
Якщо порушено умови обмежень на параметри функції, тоді повернути пустий список.
"""

from random import randrange


def get_numbers_ticket(min, max, quantity):

#Variant 1
    # result = []
    # count = 0

    # if min < 1 or max > 1000:
    #     return result

    # while count < quantity:
    #     num = randrange(min, max)
    #     if num not in result:
    #         result.append(num)
    #         count += 1

    # result = sorted(result)

    # return result

# Variant 2
    # if min < 1 or max > 1000:
    #     return []

    # result = set()
    # while len(result) < quantity:
    #     num = randrange(min, max)
    #     result.add(num)

    # return sorted(list(result))

# Variant 3 (passed auto-check)
    from random import sample

    if min < 1 or max > 1000 or min >= max or quantity <= min or quantity >= max:
        return []

    random_numbers = sample(range(min, max), quantity)
    
    random_numbers.sort()
    
    return random_numbers


print(get_numbers_ticket(1, 49, 6))
