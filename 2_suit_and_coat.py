# Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), 
# для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. 
# Проверить на практике полученные на этом уроке знания: 
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

@abstractmethod
class Closing(ABC):
    def material_consump(self):
        pass
    def __add__(self, closing):
        return self.material_consump + closing.material_consump
    def __rmul__(self, multypl):
        return self.material_consump * multypl


class Coat(Closing):
    def __init__(self, size):
        self.size = size
    @property
    def material_consump(self):
        return round(self.size / 6.5 + 0.5, 2)
    def __add__(self, closing):
        return super().__add__(closing)
    def __rmul__(self, multypl):
        return super().__rmul__(multypl)

class Suit(Closing):
    def __init__(self, height):
        self.height = height
    @property
    def material_consump(self):
        return round(self.height * 2 + 0.5, 2)
    def __add__(self, closing):
        return super().__add__(closing)
    def __rmul__(self, multypl):
        return super().__rmul__(multypl)

coat = Coat(56)
print(f'Material for the coat {coat.material_consump}')

suit = Suit(184)
print(f'Material for the suit {suit.material_consump}')

summ = 2*coat  + 2*suit
print(f'Sum of 2 coats and 2 suits {summ}')

fabric = [Coat(56), Coat(58), Coat(60), Suit(184), Suit(194), Suit(176)] 
amount = 0
for cl in fabric:
    amount += cl.material_consump
print(f'Toal material for fabric {amount}')
