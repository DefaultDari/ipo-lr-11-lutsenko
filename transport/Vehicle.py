import random  # Импортируем модуль random для генерации случайных значений
from .Client import Client  # Импортируем класс Client из текущего модуля

class Vehicle:
    def __init__(self, capacity, current_load=0):
        self.vehicle_id = str(random.randint(1000, 100000))  # Генерируем случайный ID для транспортного средства
        try:
            capacity = int(capacity)  # Проверяем, что грузоподъемность задана числом
        except ValueError:
            raise ValueError("Грузоподъемность указывается числом")  # Вызываем ошибку, если значение неверное
        try:
            current_load = int(current_load)  # Проверяем, что текущая загрузка задана числом
        except ValueError:
            raise ValueError("Текущая загрузка указывается числом")  # Вызываем ошибку, если значение неверное
        self.capacity = capacity  # Устанавливаем грузоподъемность
        self.clients_list = []  # Создаем пустой список клиентов
        self.current_load = current_load  # Устанавливаем текущую загрузку

    def load_cargo(self, client):
        try:
            new_weight = self.current_load + client.cargo_weight  # Вычисляем новый вес при добавлении груза клиента
        except AttributeError:
            raise AttributeError("Вы должны передать клиента в параметр функции!")  # Вызываем ошибку, если передан не клиент
        if new_weight > self.capacity:
            print("Грузоподъемность превышена! Действие отменено!")  # Сообщение, если превышена грузоподъемность
        else:
            self.current_load = new_weight  # Обновляем текущую загрузку
            self.clients_list.append(client)  # Добавляем клиента в список клиентов

    def __str__(self):
        return f"ID транспорта: {self.vehicle_id}\nГрузоподъемность транспорта: {self.capacity}\nЗагружено: {self.current_load}"  # Возвращаем строковое представление объекта
