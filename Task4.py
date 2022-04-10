class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_poliсe = is_police
        is_police == False


    def go(self):
        if self.is_poliсe == True:
            print("Включилась сирена: Виу, Виу, Виу")
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction} ")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed} км/ч")


class TownCar(Car):

    def info(self):
        print(f"Это городской автомобиль. Марка {self.name}, цвет {self.color}")

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        print(f"Текущая скорость автомобиля {self.speed} км/ч")

class SportCar(Car):

    def info(self):
        print(f"Это спортивный автомобиль. Марка {self.name}, цвет {self.color}")

class WorkCar(Car):
    def info(self):
        print(f"Это городской автомобиль. Марка {self.name}, цвет {self.color}")

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        print(f"Текущая скорость автомобиля {self.speed} км/ч")

class PoliceCar(Car):

    def info(self):
        print(f"Это полицейский автомобиль. Марка {self.name}, цвет {self.color}")

    def siren(self):
        print("Сирена включена")

    def close_siren(self):
        print("Сирена отключена")

car = Car(60, "серый", "ВАЗ-2121", False)
car.go()
car.turn('влево')
car.stop()
car.show_speed()

work_car = WorkCar(45, "белый", "ВАЗ-2107", False)
work_car.show_speed()

police_car = PoliceCar(80, "синий", "УАЗ", True)
police_car.go()
print(police_car.name)
police_car.info()

town_car = TownCar(65, "желтый", "Волга", False)
town_car.show_speed()
town_car.info()

