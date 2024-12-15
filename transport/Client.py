class Client:
    def __init__(self, name, cargo_weight, is_vip=False):
        if name:
            self.name = name
        else:
            raise ValueError("Должно быть указано имя.")
        try:
            cargo_weight = int(cargo_weight)
            self.cargo_weight = cargo_weight
        except ValueError:
            raise ValueError("Вес груза должен быть числом.")
        if not (is_vip == True or is_vip == False):
            raise ValueError("VIP статус должен быть bool типом.")
        self.is_vip = bool(is_vip)

    def __str__(self):
        return f"Клиент(Name: {self.name}, Вес груза: {self.cargo_weight}, Вип-статус: {self.is_vip})"
