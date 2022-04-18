class Cell:

    def __init__(self, cells):
        self.cells = int(cells)
        if self.cells < 0:
            print('Не бывает клеток с отрицательным количеством ячеек')
            exit()

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if self.cells - other.cells < 0:
            return f'Клетка не может быть с отрицательным количеством ячеек'
        else:
            return self.cells - other.cells

    def __mul__(self, other):
        return self.cells * other.cells

    def __floordiv__(self, other):
        try:
            return self.cells // other.cells
        except ZeroDivisionError:
            return f'Зачем делить на 0 клеток?'

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.cells // rows)]) \
               + '\n' + '*' * (self.cells % rows)



c1 = Cell(25)
c2 = Cell(0)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 // c2)
print(c1.make_order(10))