#4- В текстовом файле удалить все слова, которые содержат
#  хотя бы одну цифру.
#В файле содержится, например:
#Мама сшила м0не штаны и7з бере9зовой кор45ы 893.
#  -> Мама сшила штаны.
#https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
#Это на случай возникновения непонятных символов в файле.

stringFile = 'Text_file.txt'
with open('Text_file.txt', 'r', encoding='utf-8') as f:
    text = f.readline()
    print(text)

items = list(filter(lambda word: not any(c.isdigit() for c in word), text.split()))
items_str = " ".join(items)
print(items_str)