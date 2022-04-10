import time

class TrafficLight:
    __color = ('красный', 'желтый', 'зеленый')

    def running(self):

        seconds = time.time()
        local_time = time.ctime(seconds)                # узнаем дату и время
        a = local_time.split()                          # разбиваем что бы достать только время

        while "06:00:00" <= a[3] <= "23:00:00":         # между заданный временем будет работать
            print(f'горит {TrafficLight.__color[0]} сигнал')
            time.sleep(7)
            print(f'зажегся {TrafficLight.__color[1]} сигнал')
            time.sleep(2)
            print(f'горит {TrafficLight.__color[2]} сигнал')
            time.sleep(5)
            print(f'моргает {TrafficLight.__color[1]} сигнал')
            time.sleep(3)

            seconds = time.time()
            local_time = time.ctime(seconds)
            a = local_time.split()                      # проверяем какое время
            # print(a[3])                               # что бы подсмотреть который час

tr = TrafficLight()
tr.running()
