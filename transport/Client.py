class Client:
    def __init__(self, name, cargo_weight, is_vip=False):
        if name:  # Проверяем, что имя клиента указано
            self.name = name  # Устанавливаем имя клиента
        else:
            raise ValueError("Должно быть указано имя.")  # Вызываем ошибку, если имя не указано
        try:
            cargo_weight = int(cargo_weight)  # Проверяем, что вес груза указан числом
            self.cargo_weight = cargo_weight  # Устанавливаем вес груза клиента
        except ValueError:
            raise ValueError("Вес груза должен быть числом.")  # Вызываем ошибку, если вес не является числом
        if not (is_vip == True or is_vip == False):  # Проверяем, что VIP-статус является булевым типом
            raise ValueError("VIP статус должен быть bool типом.")  # Вызываем ошибку, если VIP-статус не булевый
        self.is_vip = bool(is_vip)  # Устанавливаем VIP-статус клиента

    def __str__(self):
        # Возвращаем строковое представление объекта Client
        return f"Клиент(Name: {self.name}, Вес груза: {self.cargo_weight}, Вип-статус: {self.is_vip})"
