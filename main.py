from transport import Client, Truck, Train, TransportCompany  # Импортируем необходимые классы из модуля transport

status = True  # Переменная для продолжения работы программы
clients, vehicles, companies = [], [], []  # Создаем пустые списки для клиентов, транспортных средств и компаний

def get_int_input(prompt):
    # Функция для получения целочисленного ввода от пользователя
    while True:
        try:
            return int(input(prompt))  # Пробуем преобразовать ввод в целое число
        except ValueError:
            print("Введите корректное числовое значение!")  # Сообщение об ошибке при неверном вводе

def get_str_input(prompt):
    # Функция для получения строкового ввода от пользователя
    while True:
        value = input(prompt)
        if value.isalpha():  # Проверяем, состоит ли строка только из букв
            return value
        else:
            print("Введите корректное текстовое значение!")  # Сообщение об ошибке при неверном вводе

def menu():
    # Функция для отображения основного меню
    print("1 - Создать клиента\n2 - Управлять транспортом\n3 - Управлять компаниями\n4 - Вывести информацию о всех клиентах\n5 - Вывести информацию о всех транспортах\n6 - Вывести информацию о всех компаниях\n7 - Выход из программы")

def vehicle_menu():
    # Функция для отображения меню управления транспортом
    print("1 - Создать грузовик\n2 - Создать поезд\n3 - Загрузить груз клиента в транспорт")

def company_menu():
    # Функция для отображения меню управления компаниями
    print("1 - Создать компанию\n2 - Добавить транспортное средство в компанию\n3 - Список всех транспортных средств компании\n4 - Добавить клиента в компанию\n5 - Распределить грузы клиентов по транспортным средствам")

while status:
    menu()  # Отображаем основное меню
    choice = get_int_input("Введите номер: ")  # Получаем выбор пользователя

    if choice == 1:
        # Создание нового клиента
        name = get_str_input("Введите имя нового клиента: ")  # Получаем имя клиента
        while True:
            try:
                cargo = int(input("Введите вес груза нового клиента (кг): "))  # Получаем вес груза
                if cargo < 0:
                    print("Вес груза должен быть положительным. Попробуйте снова.")
                else:
                    break
            except ValueError:
                print("Некорректный ввод. Введите числовое значение.")
        is_vip = get_int_input("Укажите, является ли новый клиент VIP? (1 - да / 2 - нет) ") == 1  # Получаем статус VIP
        clients.append(Client(name, cargo, is_vip))  # Добавляем клиента в список клиентов
        print("Новый клиент был успешно создан!")  # Сообщение об успешном создании клиента

    elif choice == 2:
        # Управление транспортом
        vehicle_menu()  # Отображаем меню управления транспортом
        choice = get_int_input("Введите номер: ")  # Получаем выбор пользователя

        if choice == 1:
            # Создание грузовика
            capacity = get_int_input("Введите грузоподъемность грузовика(кг): ")  # Получаем грузоподъемность
            color = get_str_input("Введите цвет грузовика: ")  # Получаем цвет
            vehicles.append(Truck(capacity, color))  # Добавляем грузовик в список транспортных средств
            print("Грузовик создан!")  # Сообщение об успешном создании грузовика
        elif choice == 2:
            # Создание поезда
            capacity = get_int_input("Введите грузоподъемность поезда(кг): ")  # Получаем грузоподъемность
            number_of_cars = get_int_input("Введите количество вагонов: ")  # Получаем количество вагонов
            vehicles.append(Train(capacity, number_of_cars))  # Добавляем поезд в список транспортных средств
            print("Поезд создан!")  # Сообщение об успешном создании поезда
        elif choice == 3:
            # Загрузка груза клиента в транспорт
            while True:
                try:
                    target_vehicle = get_int_input("Введите номер транспорта: ")  # Получаем номер транспорта
                    if target_vehicle <= 0 or target_vehicle > len(vehicles):
                        print("Некорректный номер транспорта. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            while True:
                try:
                    target_client = get_int_input("Введите номер клиента: ")  # Получаем номер клиента
                    if target_client <= 0 or target_client > len(clients):
                        print("Некорректный номер клиента. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            vehicles[target_vehicle - 1].load_cargo(clients[target_client - 1])  # Загружаем груз клиента в транспорт
            print("Груз успешно загружен!")  # Сообщение об успешной загрузке груза

    elif choice == 3:
        # Управление компаниями
        company_menu()  # Отображаем меню управления компаниями
        choice = get_int_input("Введите номер: ")  # Получаем выбор пользователя

        if choice == 1:
            # Создание компании
            name = get_str_input("Введите название компании: ")  # Получаем название компании
            companies.append(TransportCompany(name))  # Добавляем компанию в список компаний
            print("Компания успешно создана!")  # Сообщение об успешном создании компании
        elif choice == 2:
            # Добавление транспортного средства в компанию
            while True:
                try:
                    target_vehicle = get_int_input("Введите номер транспорта: ")  # Получаем номер транспорта
                    if target_vehicle <= 0 or target_vehicle > len(vehicles):
                        print("Некорректный номер транспорта. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            while True:
                try:
                    target_company = get_int_input("Введите номер компании: ")  # Получаем номер компании
                    if target_company <= 0 or target_company > len(companies):
                        print("Некорректный номер компании. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            companies[target_company - 1].add_vehicle(vehicles[target_vehicle - 1])  # Добавляем транспорт в компанию
            print("Транспорт успешно добавлен!")  # Сообщение об успешном добавлении транспорта
        elif choice == 3:
            # Список всех транспортных средств компании
            while True:
                try:
                    target_company = get_int_input("Введите номер компании: ")  # Получаем номер компании
                    if target_company <= 0 or target_company > len(companies):
                        print("Некорректный номер компании. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            print(f"Список транспорта компании {target_company}:")  # Выводим сообщение о транспорте компании
            for idx, vehicle in enumerate(companies[target_company - 1].list_vehicles(), start=1):
                print(f"{idx}. {vehicle}")  # Выводим каждый транспорт компании
        elif choice == 4:
            # Добавление клиента в компанию
            while True:
                try:
                    target_company = get_int_input("Введите номер компании: ")  # Получаем номер компании
                    if target_company <= 0 or target_company > len(companies):
                        print("Некорректный номер компании. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            while True:
                try:
                    target_client = get_int_input("Введите номер клиента: ")  # Получаем номер клиента
                    if target_client <= 0 or target_client > len(clients):
                        print("Некорректный номер клиента. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            companies[target_company - 1].add_client(clients[target_client - 1])  # Добавляем клиента в компанию
            print("Клиент успешно добавлен!")  # Сообщение об успешном добавлении клиента
        elif choice == 5:
            # Распределение грузов клиентов по транспортным средствам
            while True:
                try:
                    target_company = get_int_input("Введите номер компании: ")  # Получаем номер компании
                    if target_company <= 0 or target_company > len(companies):
                        print("Некорректный номер компании. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод. Введите числовое значение.")
            companies[target_company - 1].optimize_cargo_distribution()  # Оптимизируем распределение груза
            print("Грузы успешно распределены!")  # Сообщение об успешном распределении грузов

    elif choice == 4:
        # Вывод информации о всех клиентах
        for idx, client in enumerate(clients, start=1):
            print(f"{idx}. Имя: {client.name}. Вес груза(кг): {client.cargo_weight}. VIP-статус: {'Да' if client.is_vip else 'Нет'}")  # Вывод информации о каждом клиенте

    elif choice == 5:
        # Вывод информации о всех транспортах
        for idx, vehicle in enumerate(vehicles, start=1):
            print(f"{idx}. {vehicle}")  # Вывод информации о каждом транспорте

    elif choice == 6:
        # Вывод информации о всех компаниях
        for idx, company in enumerate(companies, start=1):
            print(f"{idx}. Название компании: {company.name}")  # Вывод названия компании
            print("| Список транспортных средств: ")
            for vehicle in company.list_vehicles():
                print(f"| {vehicle}")  # Вывод информации о каждом транспорте компании
            print("| Список клиентов компании: ")
            for client in company.list_clients():
                print(f"| Имя клиента: {client.name}. Вес груза(кг): {client.cargo_weight}. VIP-статус: {'Да' if client.is_vip else 'Нет'}")  # Вывод информации о каждом клиенте компании

    elif choice == 7:
        # Выход из программы
        status = False  # Завершаем работу программы
        print("Выход.")  # Сообщение о выходе
