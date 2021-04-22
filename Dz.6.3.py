class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

rab = Position('Mr_Crown', 'Smith', 'Manager', 15000, 1000)
print(rab.get_full_name())
print(rab.get_total_income())
print(rab.name, rab.surname, rab.position, rab._income)