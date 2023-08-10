# Андрей Кирьянов, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

def post_new_order(body):                               # Функция создания заказа

    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json=body,
                         headers=data.headers)           # тело запроса из файла data.py

response = post_new_order(data.user_body)       # получаем ответ на запрос создания заказа

track_number = response.json()       # Получаем значение ответа в виде словаря
track_id = track_number['track']     # Сохраняем цифровое значение "track_id" в переменную


    # Здесь функция для проверки, что по треку заказа можно получить данные о заказе
def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER,
                        params={"t": track_id})
# В переменную track_response сохраняется результат запроса на проверку заказа по номеру трека
track_response = get_order_by_track()


# Тест 1: Проверяется, что по треку заказа можно получить данные о заказе.
def test_find_order_by_track_number_get_success_response():

    new_track_response = track_response     # Дублирую переменную track_response для "Теста 1"
# Проверяется, что код ответа равен 200
    assert new_track_response.status_code == 200

# Андрей Кирьянов, 7-я когорта — Финальный проект. Инженер по тестированию плюс