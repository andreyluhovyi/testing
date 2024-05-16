#Звісно, ось переклад:

#Цикл for - Контрольний оператор для ітерації по послідовності. (For loop)

#Спискове включення - Компактний спосіб обробки та створення списків. (List comprehension)

#Розпакування - Присвоєння декількох змінних зі збірки в одній інструкції. (Unpack)

#Кортеж - Незмінний упорядкований набір. (Tuple)

#Абсолютний шлях - Повний шлях до файлу або каталогу. (Absolute path)

#Додавання - Додати елемент в кінець списку. (Append)

#Умовний оператор - Код, який виконується, якщо умова є істинною. (Conditional statement)

#Нормалізувати - Стандартизувати дані до однорідного формату. (Normalize)



import os
home_items = os.listdir('C:/Users/lygov')
print(home_items)




# For loop over a list 
names = ['John', 'Mary', 'Bob']
for name in names:
  print(name)

# List comprehension to capture even numbers
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Unpacking dictionary
person = {'name': 'John', 'age': 30}
for key, value in person.items():
  print(key, value)


# Append to a list
numbersTwo = [1, 2, 3]
numbersTwo.append(4)
print(numbersTwo)

# Conditional statement
nums = [1, 2, 3, 4] 
if len(nums) > 2:
  print("List has more than 2 items")


# Separate items into different lists
nums = [1, 2, 3, 4, 5, 6]
evens = []
odds = []

for n in nums:
  if n % 2 == 0:
    evens.append(n)
  else:
    odds.append(n)

print("Even numbers:", evens)
print("Odd numbers:", odds)



#JSON модуль JSON module- Модуль для роботи з даними у форматі JSON в Python

#Завантажити Load - Зчитати дані у форматі JSON у об'єкт Python

#Вивантажити Dump - Серіалізувати об'єкт Python до JSON

#Рядок String - Послідовність символів у Python

#Серіалізувати Serialize - Конвертувати об'єкт Python у формат, схожий на JSON

#Десеріалізувати Deserialize - Конвертувати JSON у об'єкт Python

#Читати Read - Отримати вміст файлу як рядок

#Записати Write - Зберегти дані у файл


import json


# Dictionary to JSON string
data = {'name':'John', 'age':30}
json_data = json.dumps(data)

# JSON string to Python Dictionary
json_str = '{"name":"John", "age":30}'
data = json.loads(json_str)

# Python list to JSON array
data = [1, 2, 3] 
json_data = json.dumps(data)

# JSON array to Python list
json_str = '[1, 2, 3]'
data = json.loads(json_str)

import json

# Write Python dict to JSON files
data = {'name':'John'}
with open('data.json','w') as f:
  json.dump(data, f)
  
# Read JSON file to Python dict  
with open('data.json') as f:
  data = json.load(f)

# verify files exist
import os
file_exists = os.path.exists('data.json')
print("Verifying if data.json file exists:", file_exists)