from .Client import Client  # Импортируем класс Client из текущего модуля
from .Vehicle import Vehicle  # Импортируем класс Vehicle из текущего модуля

class TransportCompany:
    def __init__(self, name):
        self.name = name  # Название компании
        self.vehicles = []  # Список транспортных средств компании
        self.clients = []  # Список клиентов компании

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):  # Проверка, является ли переданный объект экземпляром класса Vehicle
            raise TypeError("Транспортное средство должно быть экземпляром класса Vehicle")  # Исключение в случае ошибки типа
        self.vehicles.append(vehicle)  # Добавление транспортного средства в список

    def list_vehicles(self):
        return self.vehicles  # Возвращает список транспортных средств компании

    def add_client(self, client):
        if not isinstance(client, Client):  # Проверка, является ли переданный объект экземпляром класса Client
            raise TypeError("Клиент должен быть экземпляром класса Client")  # Исключение в случае ошибки типа
        self.clients.append(client)  # Добавление клиента в список

    def list_clients(self):
        return self.clients  # Возвращает список клиентов компании

    def optimize_cargo_distribution(self):
        priority = [c for c in self.clients if c.is_vip]  # Список VIP-клиентов
        not_priority = [c for c in self.clients if not c.is_vip]  # Список не VIP-клиентов
        success = []  # Список клиентов, для которых груз был успешно распределен
        
        for client_list in (priority, not_priority):  # Проходим по спискам VIP и не VIP клиентов
            for client in client_list:
                for vehicle in self.vehicles:
                    if vehicle.capacity - vehicle.current_load >= client.cargo_weight:  # Проверка, можно ли загрузить груз клиента в транспортное средство
                        vehicle.current_load += client.cargo_weight  # Обновление текущей загрузки транспортного средства
                        vehicle.clients_list.append(client)  # Добавление клиента в список клиентов транспортного средства
                        success.append(client)  # Добавление клиента в список успешно распределенных грузов
                        break  # Переход к следующему клиенту
        
        print("Груз распределен для клиентов компании:")  # Сообщение об успешном распределении груза
        for client in success:
            print(f"{client.name}")  # Вывод имени клиента, для которого груз был успешно распределен
        print()  # Печатает пустую строку
