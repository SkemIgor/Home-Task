class Wolker:

    def __init__(self, name, surname, position, **_income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Wolker):

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        self._income = sum(self._income.values())
        return f'Доход: {self._income}'


position = Position("Скоморохов", "Игорь", "инженер-геодезист", оклад = 17000, премия = 50000 )
print(position.get_full_name())
print(position.get_total_income())