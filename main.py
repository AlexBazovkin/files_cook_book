from pprint import pprint


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

# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2))
