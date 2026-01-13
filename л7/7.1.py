class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"

    def get_info(self):
        return f"Менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет обслуживание ({self.specialization})"

    def get_info(self):
        return f"Техник: {self.name}, ID: {self.id}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        self.department = department
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return "\n".join([emp.get_info() for emp in self.team])


# Создание объектов
emp = Employee("Иван Петров", "E001")
mgr = Manager("Мария Смирнова", "M001", "IT")
tech = Technician("Алексей Козлов", "T001", "Сети")
tm = TechManager("Дмитрий Соколов", "TM001", "DevOps", "Инфраструктура")

# Вывод информации
print(emp.get_info())
print(mgr.get_info())
print(tech.get_info())
print(tm.get_info())

# Демонстрация методов
print(mgr.manage_project())
print(tech.perform_maintenance())

# Формирование команды
tm.add_employee(emp)
tm.add_employee(tech)
print(tm.get_team_info())

# class Employee:
#     def __init__(self, name, emp_id):
#         self.name = name
#         self.id = emp_id

#     def get_info(self):
#         return f"{self.name} (ID: {self.id})"


# class Manager(Employee):
#     def __init__(self, name, emp_id, department, **kwargs):
#         super().__init__(name, emp_id, **kwargs)
#         self.department = department

#     def manage_project(self, project):
#         return f"{self.name} управляет {project}"

#     def get_info(self):
#         return f"Менеджер {self.name} (ID: {self.id}), Отдел: {self.department}"


# class Technician(Employee):
#     def __init__(self, name, emp_id, specialization, **kwargs):
#         super().__init__(name, emp_id, **kwargs)
#         self.specialization = specialization

#     def perform_maintenance(self):
#         return f"{self.name} выполняет работу по {self.specialization}"

#     def get_info(self):
#         return f"Техник {self.name} (ID: {self.id}), Специализация: {self.specialization}"


# class TechManager(Manager, Technician):
#     def __init__(self, name, emp_id, department, specialization):
#         super().__init__(name=name, emp_id=emp_id, department=department, specialization=specialization)
#         self.team = []

#     def add_employee(self, employee):
#         self.team.append(employee)
#         return f"{employee.name} добавлен в команду"

#     def get_team_info(self):
#         return "\n".join([m.get_info() for m in self.team]) if self.team else "Команда пуста"

#     def get_info(self):
#         return f"Тех. Менеджер {self.name} (ID: {self.id}), Отдел: {self.department}, Специализация: {self.specialization}"


# if __name__ == "__main__":
#     emp = Employee("Ivan", "E001")
#     manager = Manager("Sasha", "M001", "IT")
#     tech = Technician("Lev", "T001", "сетям")

#     tech_manager = TechManager("Sergey", "TM001", "Техподдержка", "серверам")
#     tech_manager.add_employee(emp)
#     tech_manager.add_employee(tech)

#     print(tech_manager.get_info())
#     print(tech_manager.manage_project("апгрейд серверов"))
#     print(tech_manager.perform_maintenance())
#     print("Команда:", tech_manager.get_team_info(), sep="\n")