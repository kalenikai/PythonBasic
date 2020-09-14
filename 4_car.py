# Реализуйте базовый класс Car. 
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).  
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
    def go(self):
        print('Car is moving')
    def stop(self):
        print('Car is stoped')
    def turn(self, direction):
        if direction == 'right':
            print('Car is turning to the right')
        elif direction == 'left':
            print('Car is turning to the left')
    def show_speed(self):
        print(f'The current speed is: {self.speed}') 

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        if self.speed >= 60:
           print(f'The current speed is: {self.speed}. Your town car is overspeed')

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        if self.speed >= 40:
           print(f'The current speed is: {self.speed}. Your work car is overspeed')  

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Car):
    is_police = True
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


cars = []
cars.append(TownCar(70, 'Black', 'Ford'))
cars.append(WorkCar(45, 'Black', 'Ford'))
cars.append(SportCar(200, 'Black', 'Mozeratti'))
cars.append(PoliceCar(120, 'White', 'BMW'))

for car in cars:
    print(car.go(), car.show_speed())
    if car.is_police:
        print ('It is police car')
    else:
        print ('It is not police car')
    print()    
