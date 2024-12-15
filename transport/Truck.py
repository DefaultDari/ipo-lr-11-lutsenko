from .Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity, color, current_load=0):
        super().__init__(capacity, current_load)
        self.color = color

    def __str__(self):
        return f"Грузовик(ID: {self.vehicle_id}, Грузоподъемность: {self.capacity}, Текущая загруженность: {self.current_load}, Цвет: {self.color})"
