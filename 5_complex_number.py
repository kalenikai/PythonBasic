# Реализовать проект «Операции с комплексными числами». 
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
#  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imgn):
        self.real = real
        self.imgn = imgn
    
    def __str__(self):
        return str(self.real) + ' + j' + str(self.imgn)
    
    def __add__(self, cmplx_number):
        return ComplexNumber(self.real + cmplx_number.real, self.imgn + cmplx_number.imgn)
    # 
    def __mul__(self, cmplx_number):
        return ComplexNumber(self.real * cmplx_number.real - self.imgn * cmplx_number.imgn,\
                             self.real * cmplx_number.imgn + cmplx_number.real * self.imgn)
    
    def __sub__(self, cmplx_number):
        return ComplexNumber(self.real - cmplx_number.real, self.imgn - cmplx_number.imgn)






cn1 = ComplexNumber(1, 3)
cn2 = ComplexNumber(5, -2)
print(cn1 + cn2)
print(cn1 * cn2)
print(cn1 - cn2)

