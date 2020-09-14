# Реализовать класс Stationery (канцелярская принадлежность). 
# Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” 
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. 
# Для каждого из классов метод должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''
    def draw(self):
        print('Basic class')

class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print('A pen is starting drawing') 

class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print('A pencil is starting drawing')         

class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print('A handle is starting drawing') 

stats = [] 
stats.append(Pen())
stats.append(Pencil())
stats.append(Handle())

for el in stats:
    print(f'I am a {el.title}.')
    print(f'{el.draw()}.' )
