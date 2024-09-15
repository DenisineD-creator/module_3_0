# Глобальная переменная для подсчёта вызовов функции
calls = 0


# Функция для подсчёта вызовов
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # увеличивает счётчик вызовов
    return (len(string), string.upper(), string.lower())

    # Функция для проверки наличия строки в списке, без учета регистра

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower



