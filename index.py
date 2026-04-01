from functools import reduce
# Тут что то объяснять же надо, да? Эх...


def update_profile(user_id, **others):
    return {'id': user_id, 'updated_fields':others}
# Функция принимает на вход айди пользователя - user_id, а также другие именованные аргументы(**args)
# Возвращает цельный объект из айди и именованных аргументов


def get_domains(emails):
    return map(lambda x: x[x.find('@') + 1:],emails)
# Функция принимает на вход массив из почт и обрабатывает его через метод map: 
# (используется lambda для компактности) выражение x[x.find('@') означает срез, начиная с индекса, где впервые начинается символ @(метод find())


def filter_target_audience(users):
    adult = filter(lambda x: x.get('age') >= 18, users)
    return filter(lambda x: x.get('is_premium') == True, adult)
# Функция принимает на вход массив пользователей. Применятся два последовательных фильтра: сначала не взрослых людей, потом тех, у кого есть премиум. 
# Используется метод get() для нахождения определенного ключа


def build_response(status, *errors, **data):
    return {"status": status, 'errors': errors, 'data': data}
# Функция принимает на вход статус, позиционный аргумент в виде ошибок(*args) и именованные аргументы в виде даты(**args). Работает идентично как и первая функция


def calculate_total_spent(transactions):
    price_array = map(lambda x: x.get('amount'), transactions)
    return reduce(lambda x, y: x + y, price_array)
# Функция принимает на вход массив из транзакций. Происходит выборка чисел при помощи get() из объектов для дальнейшей работы
# Применяется reduce для сложения этих чисел.
