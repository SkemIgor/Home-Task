class Stationery:
    title = "Название"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print("Запуск отрисовки. Ручка чернилами наносит тонкие линии")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print("Запуск отрисовки. Карандаш грифелем наносит тонкие линии которые можно стереть ластиком")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print("Запуск отрисовки. Маркер наносит толстые линии краской")

stationery = Stationery()
stationery.draw()

pen = Pen()
print(pen.title)
pen.draw()

pencil = Pencil()
print(pencil.title)
pencil.draw()

handle = Handle()
print(handle.title)
handle.draw()