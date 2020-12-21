list_files = ["Файл 1", "Файл 2"]
result_file = "Файл №3"
lenght = 0
date = " "
for element in list_files:
  with open(element, encoding = "utf - 8") as f:
    date = f.readlines()
    lenght_date = len(date)
    text = element
    text_1 = lenght_date
    text_1 = str()
    if lenght < lenght_date:
      lenght = lenght_date
      date_1 = date
      text_finally = text
      text_finally_1 = text_1
    else:
      date_for_write = " ".join(date)
      date_for_write_1 = " ".join(date_1)
      with open(result_file,  "w", encoding = "utf - 8" ) as document:
        document.write(text)
        document.write(text_1)
        document.write(date_for_write)
        document.write(text_finally)
        document.write(text_finally_1)
        document.write(date_for_write_1)