cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
  dict_by_dishes= {}
  for dish in dishes:
    if dish in cook_book:
      for per in cook_book[dish]:
        per_1 = per.pop('ingredient_name')
        per['quantity'] *= person_count
        dict_by_dishes[per_1] = per
  return dict_by_dishes

result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#print(result)

dict_txt = {}
dict_sum = {}
with open ('1.txt', 'r', encoding='utf8') as f:
    name = '1.txt'
    sum_str = 0
    str_ = []
    for line in f:
      str_.append(line)
      dict_txt[name] = str_
      dict_sum.setdefault(name, sum_str)

with open('2.txt', 'r', encoding='utf8') as f:
  name = '2.txt'
  sum_str = 0
  str_ = []
  for line in f:
    str_.append(line)
    dict_txt[name] = str_
    dict_sum.setdefault(name, sum_str)

  with open('3.txt', 'r', encoding='utf8') as f:
    name = '3.txt'
    sum_str = 0
    str_ = []
    for line in f:
      str_.append(line)
      dict_txt[name] = str_
      dict_sum.setdefault(name, sum_str)

import operator
sorted_dict = dict(sorted(dict_sum.items(), key=operator.itemgetter(1)))

import pickle
with open('Text.txt', 'wb') as f:
  for key in sorted_dict.keys():
      for i in dict_txt[key]:
        text = i.strip()
        pickle.dump(text, f)
        print(text)



