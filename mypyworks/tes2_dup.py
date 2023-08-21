class Rectangle:
    

    def area(self,length, width):
        return self.length * self.width

    def perimeter(self,length, width):
        return 2 * length + 2 * width
    
obj = Rectangle()
print(obj.perimeter(2,4))
print(obj.area(2,4))