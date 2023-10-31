"""
У нас є іменований кортеж для зберігання котів у змінній Cat.
На першому місці у нас кличка котика nickname, потім його вік age та ім'я власника кота owner.

Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.

Якщо функція convert_list приймає у параметрі cats список іменованих кортежів

[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
То функція поверне наступний список словників:

[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
І в той же час, якщо функція convert_list приймає в параметрі cats список словників,
то результатом буде зворотна операція та функція поверне список іменованих кортежів.

Для визначення типу параметра cats використовуйте функцію isinstance.
"""

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    # Перевірка, чи вхідний параметр є списком іменованих кортежів
    if isinstance(cats[0], Cat):
        # Якщо вхідний список містить іменовані кортежі, перетворимо їх в словники
        return [{"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats]
    else:
        # Якщо вхідний список містить словники, перетворимо їх в іменовані кортежі
        return [Cat(cat["nickname"], cat["age"], cat["owner"]) for cat in cats]


# Приклад використання функції
cats_namedtuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_dict = [{"nickname": "Mick", "age": 5, "owner": "Sara"},
            {"nickname": "Barsik", "age": 7, "owner": "Olga"},
            {"nickname": "Simon", "age": 3, "owner": "Yura"}]

# Перетворення іменованих кортежів в словники
converted_to_dict = convert_list(cats_namedtuple)
print(converted_to_dict)

# Перетворення словників в іменовані кортежі
converted_to_namedtuple = convert_list(cats_dict)
print(converted_to_namedtuple)
