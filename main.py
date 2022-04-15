import os
from pprint import pprint
dict = []  # К сожалению так и не понял как обойтись без глобальной переменной.
           # По моей задумке словарь должен быть вне функций и хранить данные о всех файлах.


def create_cook_book(filename):
    cook_book = {}
    with open(filename, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            qty = int(file.readline().strip())
            cook_book[dish_name] = []
            for ingredients in range(qty):
                ingredients = file.readline().strip().split(' | ')
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[dish_name].append(ingredients_dict)
            file.readline()
    return cook_book

# Test:
# print(create_cook_book('recipes.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if name in shop_list:
                shop_list[name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[name] = {'measure': ingredient['measure'],
                                   'quantity': ingredient['quantity'] * person_count
                                   }
    return shop_list

# Test:
# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2))



def create_dict_files(file_name): # Создает словарь с данными о файле (Название, путь, кол-во строк в файле).
    with open(file_name, encoding='utf8') as file:
        line_counter = 0
        for lines in file:
            if lines.strip():
                line_counter += 1
                file_dict = {
                    'file_name': file.name,
                    'file_path': os.path.realpath(file.name),
                    'lines_qty': line_counter
                            }
    return file_dict


def create_n_sort_files(info): # После каждого использования def create_dict_files(file_name) обновляет глобальные словарь.
    dict.append(info)
    return


# Тестовый пуск функции для записи данных в словарь и последующей работе с ними:
# create_n_sort_files(create_dict_files('1.txt'))
# create_n_sort_files(create_dict_files('2.txt'))
# create_n_sort_files(create_dict_files('3.txt'))


def write_into_file(data_dict): # Запись данных в отдельный файл. Передается словарь с данными о файлах.
    data_dict = sorted(dict, key=lambda x: x['lines_qty'])
    with open('4_wright.txt', 'a', encoding='utf8') as file:
        for information in data_dict:
            with open(information['file_path'], encoding='utf8') as file_to_copy:
                file.write(f"{information['file_name']}\n{information['lines_qty']}\n")
                for line in file_to_copy.readlines():
                    file.write(f'{line.strip()}\n')
