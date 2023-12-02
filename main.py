import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["recipes"]

# Створення колекції (еквівалент таблиці в реляційних базах даних)
collection = db["dishes"]

# Додавання документів (еквівалент записів в таблиці)
data1 = {"name": "Swedish Meatballs", "cook_time": "1 hr", "main_ing": "1/3 pound ground pork"}
data2 = {"name": "Mom's Potato Latkes", "cook_time": "15 min", "main_ing": "3 cups shredded potato"}

# Вставка документів
inserted_data1 = collection.insert_one(data1)
inserted_data2 = collection.insert_one(data2)

# Оновлення документа
query = {"name": "Mom's Potato Latkes"}
new_data = {"$set": {"main_ing": "4 cups shredded potato"}}
collection.update_one(query, new_data)

# Видалення документа
delete_query = {"name": "Swedish Meatballs"}
collection.delete_one(delete_query)

#Пошук документа
search_query = {"name": "Mom's Potato Latkes"}
print("Знайдено рецепт:")
for document in collection.find(search_query):
    print(document)

# Зчитування документів після оновлення та видалення
print("Після оновлення та видалення:")
for document in collection.find():
    print(document)

# Закриття підключення
client.close()
