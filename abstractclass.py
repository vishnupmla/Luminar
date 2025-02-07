from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,n):
        self.shapename = n

    def show(self):
        print('shape = ',self.shapename)

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,shape):
        super().__init__(shape)
        self.len = int(input('Enter the Length: '))
        self.bre = int(input('Enter the Breadth: '))

    def area(self):
        print('Area = ',self.len*self.bre)

    def perimeter(self):
        print('Perimeter = ',(2*(self.len+self.bre)))

a = Rectangle('Circle')
a.show()
a.area()
a.perimeter()