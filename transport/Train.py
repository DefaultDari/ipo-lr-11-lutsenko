from .Vehicle import Vehicle  # Импортируем класс Vehicle из текущего модуля

class Train(Vehicle):
    def __init__(self, capacity, number_of_cars, current_load=0):
        # Инициализируем класс Train, который наследует класс Vehicle
        super().__init__(capacity, current_load)  # Вызываем конструктор базового класса Vehicle
        self.number_of_cars = number_of_cars  # Устанавливаем количество вагонов

    def __str__(self):
        # Возвращаем строковое представление объекта Train
        return f"Поезд(ID: {self.vehicle_id}, Грузоподъемность: {self.capacity}, Текущая загрузка: {self.current_load}, Количество вагонов: {self.number_of_cars})"
