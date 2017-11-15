cook_book = dict()
option_list = list()
with open("homework_file.txt", "r") as f:
    for line in f:
        cook_book[line.strip()] = list()
        Dish = line.strip()
        f.readline()
        index = 0
        for line in f:
            if line == "\n":
                break
            else:
                option_list.append(line.strip())
            option = option_list[index].split(" | ")
            index += 1
            cook_book[Dish].append({'ingridient_name': option[0], 'quantity': int(option[1]), 'measure': option[2]})



def get_shop_list_by_dishes(dishes, person_count):
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
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()

