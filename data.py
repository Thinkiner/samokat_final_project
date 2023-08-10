# Андрей Кирьянов, 7-я когорта — Финальный проект. Инженер по тестированию плюс

#   Заголовки
headers = {
    "Content-Type": "application/json"
}

# Ниже передача данных в теле запроса в формате JSON.
user_body = {
    "firstName": "Naruto",                        # Имя Наруто
    "lastName": "Uchiha",                         # Фамилия Учиха
    "address": "Konoha, 142 apt.",                # Адрес для доставки
    "metroStation": 5,                            # Станция метро
    "phone": "+7 800 355 35 35",                  # Номер телефона
    "rentTime": 5,                                # Количество дней аренды
    "deliveryDate": "2020-06-06",                 # Дата доставки
    "comment": "Saske, come back to Konoha",      # Комментарий для курьера
    "color": [
        "BLACK"                                   # Чёрного цвета
    ]
}