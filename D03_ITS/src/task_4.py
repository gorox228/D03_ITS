"""
Пример кода с ошибкой № 4
"""


input_int = input("Введите целое число: ")
if input_int.isdigit():

    input_int = int(input_int)
    print(f'Твое число в степени два равно {input_int**2}')
else:
    print('Ну я же просил ввести целое число! Ну камон!')

input_str = input("А теперь напиши еще раз это число и добавь к нему букву: ")
input_str = input_str + " - это не число"
print(input_str)
