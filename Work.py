with open("Поваренная книга", encoding = "utf-8") as file_work:
  cook_dict = { }
  for line in file_work:
    dish_name = line.strip()
    counter = int(file_work.readline())
    list_of_ingridient = []
    list_of_ingr_1 = [ ]
    for i in range(counter):
      list_of_ingr_1 = file_work.readline().strip().split("|")
      temp_dict = {"ingredient_name": list_of_ingr_1[0], "quantity": list_of_ingr_1[1], "measure": list_of_ingr_1[2]}
      list_of_ingridient.append(temp_dict)
    cook_dict[dish_name] = list_of_ingridient
    file_work.readline()
  print(cook_dict)

def get_shop_list_by_dishes(dishes, person_count):
  dict_of_ingr = {}
  for k, v in cook_dict.items():
    if k == dishes:
      for element in v:
        dict_of_ingr[element["ingredient_name"]] = element
        del element["ingredient_name"]
        element["quantity"]=int(element["quantity"])
        element["quantity"]*=person_count
      return dict_of_ingr
print(get_shop_list_by_dishes("Фахитос", 2))

