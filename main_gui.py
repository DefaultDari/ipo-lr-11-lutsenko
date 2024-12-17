import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class App:
    def __init__(self, root):
        self.root = root  # Ссылка на основное окно приложения
        self.root.title("Распределение грузов")  # Заголовок окна
        
        # Списки для хранения данных о клиентах, транспорте и компаниях
        self.clients = []
        self.vehicles = []
        self.companies = []

        # Создание меню
        self.menu = tk.Menu(root)  # Главное меню
        self.root.config(menu=self.menu)  # Настройка меню в окне

        # Подменю "Файл"
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Экспорт результата", command=self.export_results)  # Экспорт данных
        self.menu.add_cascade(label="Файл", menu=self.file_menu)  # Добавление подменю в главное меню

        # Добавление пункта "О программе" в меню
        self.menu.add_command(label="О программе", command=self.show_about)

        # Рабочая область
        self.main_frame = tk.Frame(root)  # Основной фрейм
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Упаковка фрейма на весь экран

        # Панель управления (слева)
        self.control_panel = tk.Frame(self.main_frame)
        self.control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)  # Расположение панели

        # Панель с таблицами данных (справа)
        self.data_panel = tk.Frame(self.main_frame)
        self.data_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Кнопки управления
        self.add_client_button = tk.Button(self.control_panel, text="Добавить клиента", command=self.add_client)
        self.add_client_button.pack(pady=5)

        self.add_vehicle_button = tk.Button(self.control_panel, text="Добавить транспорт", command=self.add_vehicle)
        self.add_vehicle_button.pack(pady=5)

        self.add_company_button = tk.Button(self.control_panel, text="Добавить компанию", command=self.add_company)
        self.add_company_button.pack(pady=5)

        self.manage_companies_button = tk.Button(self.control_panel, text="Управление компаниями", command=self.manage_companies)
        self.manage_companies_button.pack(pady=5)

        self.allocate_button = tk.Button(self.control_panel, text="Распределить грузы", command=self.allocate_cargo)
        self.allocate_button.pack(pady=5)

        # Таблица данных о клиентах
        self.client_table = ttk.Treeview(self.data_panel, columns=("name", "weight", "vip"), show="headings")
        self.client_table.heading("name", text="Имя клиента")
        self.client_table.heading("weight", text="Вес груза")
        self.client_table.heading("vip", text="VIP статус")
        self.client_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Таблица данных о транспорте
        self.vehicle_table = ttk.Treeview(self.data_panel, columns=("id", "type", "capacity", "load"), show="headings")
        self.vehicle_table.heading("id", text="ID транспорта")
        self.vehicle_table.heading("type", text="Тип транспорта")
        self.vehicle_table.heading("capacity", text="Грузоподъемность")
        self.vehicle_table.heading("load", text="Текущая загрузка")
        self.vehicle_table.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Статусная строка
        self.status_bar = tk.Label(root, text="Готово", bd=1, relief=tk.SUNKEN, anchor=tk.W)  # Строка состояния
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)  # Размещение статусной строки внизу

    # Функция для добавления компании
    def add_company(self):
        AddCompanyWindow(self)  # Открытие окна добавления компании
    
    # Обновление статусной строки
    def update_status(self, message):
        self.status_bar.config(text=message)  # Изменение текста в статусной строке

    # Открытие окна добавления клиента
    def add_client(self):
        AddClientWindow(self)

    # Открытие окна добавления транспортного средства
    def add_vehicle(self):
        AddVehicleWindow(self)

    # Открытие окна управления компаниями
    def manage_companies(self):
        ManageCompaniesWindow(self)

    # Распределение грузов
    def allocate_cargo(self):
        if not self.clients or not self.vehicles or not self.companies:
            self.update_status("Недостаточно данных для распределения.")
            return
        for company in self.companies:  # Для каждой компании
            company["vehicles"].sort(key=lambda v: v["capacity"])  # Сортировка транспорта по грузоподъемности
            for client in self.clients:  # Для каждого клиента
                for vehicle in company["vehicles"]:  # Для каждого транспортного средства
                    if vehicle["capacity"] - vehicle["load"] >= client["weight"]:  # Если груз можно загрузить
                        vehicle["load"] += client["weight"]  # Добавляем груз на транспорт
                        break
        self.update_status("Распределение завершено.")

    # Экспорт результатов распределения
    def export_results(self):
        if not self.clients or not self.vehicles or not self.companies:
            messagebox.showwarning("Ошибка", "Нет данных для экспорта.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])  # Окно выбора пути для сохранения файла
        if file_path:
            with open(file_path, 'w') as f:  # Открытие файла для записи
                f.write("Результаты распределения грузов\n")
                for company in self.companies:  # Для каждой компании
                    f.write(f"Компания: {company['name']}\n")
                    for vehicle in company["vehicles"]:  # Для каждого транспортного средства
                        f.write(f"  Транспорт {vehicle['type']} (Грузоподъемность: {vehicle['capacity']}, Загрузка: {vehicle['load']})\n")
                f.write("\n")
            self.update_status("Результаты сохранены.")  # Обновление статусной строки

    # Окно "О программе"
    def show_about(self):
        messagebox.showinfo("О программе", "Лабораторная Работа №12 \nРазработчик: Луценко Д.К.\nГруппа: 81ТП ")

# Класс для окна добавления клиента
class AddClientWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Toplevel()  # Создание нового окна
        self.window.title("Добавить клиента")  # Заголовок окна

        # Элементы управления в окне добавления клиента
        tk.Label(self.window, text="Имя клиента").pack(pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Вес груза (кг)").pack(pady=5)
        self.weight_entry = tk.Entry(self.window)
        self.weight_entry.pack(pady=5)

        self.vip_var = tk.BooleanVar()
        tk.Checkbutton(self.window, text="VIP статус", variable=self.vip_var).pack(pady=5)

        tk.Button(self.window, text="Сохранить", command=self.save_client).pack(pady=5)  # Кнопка сохранения клиента
        tk.Button(self.window, text="Отмена", command=self.window.destroy).pack(pady=5)  # Кнопка отмены

    # Функция сохранения клиента
    def save_client(self):
        name = self.name_entry.get()  # Получаем имя клиента
        weight = self.weight_entry.get()  # Получаем вес груза

        # Проверка корректности имени клиента
        if not name.isalpha() or len(name) < 2:
            messagebox.showerror("Ошибка", "Имя клиента должно содержать только буквы и быть длиннее 2 символов.")
            self.name_entry.delete(0, tk.END)
            return

        # Проверка корректности веса груза
        try:
            weight = float(weight)
            if weight <= 0 or weight > 10000:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Вес груза должен быть положительным числом не более 10000.")
            self.weight_entry.delete(0, tk.END)
            return
        
        # Добавление клиента в список и обновление таблицы
        self.app.clients.append({"name": name, "weight": weight, "vip": self.vip_var.get()})
        self.app.client_table.insert("", tk.END, values=(name, weight, "Да" if self.vip_var.get() else "Нет"))
        self.app.update_status("Клиент добавлен.")  # Обновление статусной строки
        self.window.destroy()  # Закрытие окна

# Остальные окна (AddVehicleWindow, AddCompanyWindow, ManageCompaniesWindow) имеют аналогичную структуру.


class AddVehicleWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Toplevel()
        self.window.title("Добавить транспорт")

        tk.Label(self.window, text="Тип транспорта").pack(pady=5)
        self.type_combo = ttk.Combobox(self.window, values=["Грузовик", "Поезд"], state="readonly")
        self.type_combo.pack(pady=5)
        
        tk.Label(self.window, text="Грузоподъемность (кг)").pack(pady=5)
        self.capacity_entry = tk.Entry(self.window)
        self.capacity_entry.pack(pady=5)

        tk.Label(self.window, text="Цвет грузовика").pack(pady=5)
        self.color_entry = tk.Entry(self.window)
        self.color_entry.pack(pady=5)

        tk.Button(self.window, text="Сохранить", command=self.save_vehicle).pack(pady=5)
        tk.Button(self.window, text="Отмена", command=self.window.destroy).pack(pady=5)

    def save_vehicle(self):
        vehicle_type = self.type_combo.get()
        capacity = self.capacity_entry.get()
        color = self.color_entry.get()

        if not vehicle_type:
            messagebox.showerror("Ошибка", "Выберите тип транспорта.")
            return

        if not color:
            messagebox.showerror("Ошибка", "Укажите цвет грузовика.")
            return

        try:
            capacity = float(capacity)
            if capacity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Грузоподъемность должна быть положительным числом.")
            self.capacity_entry.delete(0, tk.END)
            return

        # Добавляем транспорт с цветом в список
        self.app.vehicles.append({"type": vehicle_type, "capacity": capacity, "load": 0, "color": color})
        self.app.vehicle_table.insert("", tk.END, values=(len(self.app.vehicles), vehicle_type, capacity, 0, color))
        self.app.update_status("Транспорт добавлен.")
        self.window.destroy()

class AddCompanyWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Toplevel()
        self.window.title("Добавить компанию")

        tk.Label(self.window, text="Название компании").pack(pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Button(self.window, text="Сохранить", command=self.save_company).pack(pady=5)
        tk.Button(self.window, text="Отмена", command=self.window.destroy).pack(pady=5)

    def save_company(self):
        name = self.name_entry.get()
        if not name or len(name) < 2:
            messagebox.showerror("Ошибка", "Название компании должно быть длиннее 2 символов.")
            self.name_entry.delete(0, tk.END)
            return
        self.app.companies.append({"name": name, "vehicles": [], "clients": []})
        self.app.update_status("Компания добавлена.")
        self.window.destroy()

class ManageCompaniesWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Toplevel()
        self.window.title("Управление компаниями")

        self.company_listbox = tk.Listbox(self.window, height=10)
        self.company_listbox.pack(pady=5, fill=tk.X)
        self.update_company_list()

        self.add_vehicle_button = tk.Button(self.window, text="Добавить транспорт в компанию", command=self.add_vehicle_to_company)
        self.add_vehicle_button.pack(pady=5)

        self.add_client_button = tk.Button(self.window, text="Добавить клиента в компанию", command=self.add_client_to_company)
        self.add_client_button.pack(pady=5)

        self.list_vehicles_button = tk.Button(self.window, text="Список транспортных средств компании", command=self.list_company_vehicles)
        self.list_vehicles_button.pack(pady=5)

        self.list_clients_button = tk.Button(self.window, text="Список клиентов компании", command=self.list_company_clients)
        self.list_clients_button.pack(pady=5)

        self.allocate_cargo_button = tk.Button(self.window, text="Распределить грузы", command=self.allocate_company_cargo)
        self.allocate_cargo_button.pack(pady=5)

    def update_company_list(self):
        self.company_listbox.delete(0, tk.END)
        for idx, company in enumerate(self.app.companies, start=1):
            self.company_listbox.insert(tk.END, f"{idx}. {company['name']}")

    def get_selected_company(self):
        try:
            selection = self.company_listbox.curselection()
            if not selection:
                raise IndexError
            return self.app.companies[selection[0]]
        except IndexError:
            messagebox.showerror("Ошибка", "Выберите компанию из списка.")
            return None

    def add_vehicle_to_company(self):
        company = self.get_selected_company()
        if not company:
            return

        vehicle_index = tk.simpledialog.askinteger(
            "Добавление транспорта",
            "Введите ID транспорта:",
            minvalue=1,
            maxvalue=len(self.app.vehicles)
        )
        if vehicle_index is None or not (1 <= vehicle_index <= len(self.app.vehicles)):
            messagebox.showerror("Ошибка", "Некорректный ID транспорта.")
            return

        vehicle = self.app.vehicles[vehicle_index - 1]
        company["vehicles"].append(vehicle)
        self.app.update_status(f"Транспорт {vehicle['type']} добавлен в компанию {company['name']}.")

    def add_client_to_company(self):
        company = self.get_selected_company()
        if not company:
            return

        client_index = tk.simpledialog.askinteger(
            "Добавление клиента",
            "Введите номер клиента:",
            minvalue=1,
            maxvalue=len(self.app.clients)
        )
        if client_index is None or not (1 <= client_index <= len(self.app.clients)):
            messagebox.showerror("Ошибка", "Некорректный номер клиента.")
            return

        client = self.app.clients[client_index - 1]
        company["clients"].append(client)
        self.app.update_status(f"Клиент {client['name']} добавлен в компанию {company['name']}.")

    def list_company_vehicles(self):
        company = self.get_selected_company()
        if not company:
            return

        vehicles = company["vehicles"]
        if not vehicles:
            messagebox.showinfo("Транспортные средства", f"У компании {company['name']} нет транспорта.")
            return

        # Формируем строку с информацией о транспорте компании, включая цвет
        vehicle_info = "\n".join(
            f"Транспорт {v['type']}, Грузоподъемность: {v['capacity']}, Загрузка: {v['load']}, Цвет: {v['color']}"
            for v in vehicles
        )
        messagebox.showinfo("Транспортные средства", vehicle_info)

    def list_company_clients(self):
        company = self.get_selected_company()
        if not company:
            return

        clients = company["clients"]
        if not clients:
            messagebox.showinfo("Клиенты компании", f"У компании {company['name']} нет клиентов.")
            return

        client_info = "\n".join(
            f"Клиент {c['name']}, Вес груза: {c['weight']} кг, VIP статус: {'Да' if c['vip'] else 'Нет'}"
            for c in clients
        )
        messagebox.showinfo("Клиенты компании", client_info)

    def allocate_company_cargo(self):
        company = self.get_selected_company()
        if not company:
            return

        for client in company["clients"]:
            allocated = False
            for vehicle in company["vehicles"]:
                if vehicle["capacity"] - vehicle["load"] >= client["weight"]:
                    vehicle["load"] += client["weight"]
                    allocated = True
                    break
            if not allocated:
                messagebox.showwarning("Предупреждение", f"Не удалось распределить груз клиента {client['name']}.")

        self.app.update_status("Распределение грузов завершено.")
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
