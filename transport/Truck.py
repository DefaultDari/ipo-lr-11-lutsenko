from .Vehicle import Vehicle  # Импортируем класс Vehicle из текущего модуля

class Truck(Vehicle):
    def __init__(self, capacity, color, current_load=0):
        # Инициализируем класс Truck, который наследует класс Vehicle
        super().__init__(capacity, current_load)  # Вызываем конструктор базового класса Vehicle
        self.color = color  # Устанавливаем цвет грузовика

    def __str__(self):
        # Возвращаем строковое представление объекта Truck
        return f"Грузовик(ID: {self.vehicle_id}, Грузоподъемность: {self.capacity}, Текущая загруженность: {self.current_load}, Цвет: {self.color})"
