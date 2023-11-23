import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["db"]

# Створення колекції (еквівалент таблиці в реляційних базах даних)
collection = db["collection"]

# Додавання документів (еквівалент записів в таблиці)
data1 = {"name": "Antony", "age": 17}
data2 = {"name": "Viktor", "age": 18}

# Вставка документів
inserted_data1 = collection.insert_one(data1)
inserted_data2 = collection.insert_one(data2)

# Зчитування документів
for document in collection.find():
    print(document)

# Оновлення документа
query = {"name": "Antony"}
new_data = {"$set": {"age": 18}}
collection.update_one(query, new_data)

# Видалення документа
delete_query = {"name": "Viktor"}
collection.delete_one(delete_query)

# Зчитування документів після оновлення та видалення
print("Після оновлення та видалення:")
for document in collection.find():
    print(document)

# Закриття підключення
client.close()
