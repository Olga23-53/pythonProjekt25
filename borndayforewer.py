"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def ask_question(question, correct_answer):
    answer = input(question)
    while answer != correct_answer:
        print("Не верно")
        answer = input(question)
    print("Верно")

ask_question('Ввведите день рождения А.С. Пушкина: ','1799')
ask_question('Введите день рождения Пушкин (Число июня): ', '6')
