# -*- coding: utf-8 -*-
import os


def read_reciept(name):
    # Создаем словарь из файла
    with open(name, mode='r', encoding='utf-8') as f:
        result = {}
        name = f.readline().strip()
        for line in f:
            quatity = int(line.strip())
            lines = []
            for item in range(quatity):
                data = f.readline().strip().split(' | ')
                lines.append({'ingredient_name': data[0],
                              'quantity': int(data[1]),
                              'measure': data[2]})
            result[name] = lines
            f.readline()
            name = f.readline().strip()
    return result


def rec_reciept(book, name='reciept.txt'):
    # создаем файл из словаря
    f = open(name, mode='w', encoding='utf-8')
    for dish, recipe in book.items():
        f.write(dish + '\n')
        f.write(str(len(recipe)) + '\n')
        for ingridients in recipe:
            f.write(' | '.join(map(str, ingridients.values())) + '\n')
        f.write('\n')
    f.close()


def get_shop_list_by_dishes(dishes, person_count):
    # Создаем список покупок на ужин
    result = {}
    for i in dishes:
        if i in cook_book:
            for reciept in cook_book[i]:
                if reciept['ingredient_name'] in result:
                    result[reciept['ingredient_name']]['quantity'] += reciept['quantity'] * person_count
                else:
                    result[reciept['ingredient_name']] = {'measure': reciept['measure'],
                                                          'quantity': reciept['quantity'] * person_count}
    return result


def add_files(lst_files):
    # Задание 3
    work_zone = []
    for i in lst_files:
        with open(os.path.join(text_direct, i), mode='r', encoding='utf-8') as f:
            work_zone.append((i, len(f.readlines())))
    work_zone.sort(key=lambda x: x[1])
    f = open('result.txt', 'w', encoding='utf-8')
    for name, lenght in work_zone:
        with open(os.path.join(text_direct, name), mode='r', encoding='utf-8') as work_file:
            print(name + '\n' + str(lenght), file=f)
            for line in work_file:
                print(line.rstrip(), file=f)
    f.close()


reciept_direct = os.path.join(os.getcwd(), 'reciepts')  # Адрес папки для рецептов
text_direct = os.path.join(os.getcwd(), 'texts')  # Адрес папки для текстов
lst_files = os.listdir(text_direct)  # Список файлов для склейки в 1
# add_files(lst_files)  # Вызов функции для склейки файлов

# cook_book = read_reciept(os.path.join(reciept_direct, 'rec2')) # создание словаря из текста в файле
# print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)) # сколько продуктов купить
# rec_reciept(cook_book, 'rec2') # на всякий пожарный, создание файла из словаря
