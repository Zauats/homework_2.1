def cook_book_programm():
    cook_book = dict()
    with open("homework_file.txt", "r") as f:
        for line in f:
            cook_book[line.strip()] = list()
            dish = line.strip()
            f.readline()
            for line in f:
                line = line.strip()
                if not line:
                    break
                product = line.strip().split(" | ")
                cook_book[dish].append({'ingridient_name': product[0], 'quantity': int(product[1]), 'measure': product[2]})
    return cook_book

print(cook_book_programm())







def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book_programm())
  print_shop_list(shop_list)

create_shop_list()
