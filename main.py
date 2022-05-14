# -*- coding: utf-8 -*-

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
    # в функцию передаем список файлов, которые нужно объединить
    # универсальное решение, под n-oe количество файлов.
    # открываем каждый файл, считаем количество строк,
    # создаем пары (название файла, количество строк), сортируем по количеству строк.
    # В порядке сортировки открываем файлы  и считываем текст, записываем в новый файл
    work_zone = []
    for i in lst_files:
        with open(i, mode='r', encoding='utf-8') as f:
            work_zone.append((i, len(f.readlines())))
        work_zone.sort(key=lambda x: x[1])
    f = open('result.txt', 'w', encoding='utf-8')
    for name, lenght in work_zone:
        with open(name, mode='r', encoding='utf-8') as work_file:
            print(name + '\n' + str(lenght), file=f)
            for line in work_file:
                print(line.rstrip(), file=f)
    f.close()

# cook_book = read_reciept('rec2')
# add_files(['1.txt', '2.txt', '3.txt']
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# rec_reciept(cook_book, 'rec2')
