class Road:

    def __init__(self, _length, _width, _thickness, _price):
        self._length = _length
        self._width = _width
        self._thickness = _thickness
        self._price = _price
    def asphalt_mass(self):
        weight = self._length * self._width * 25 * self._thickness/1000
        return f'Для покрытия {self._width} метров дороги, шириной {self._length} метров и толщиной слоя в {self._thickness} см., понадобится ' \
               f'{weight} тонн асфальтобетона. Обойдется это {weight * self._price} рублей'

road = Road(25, 5000, 3, 4350)
print(road.asphalt_mass())