class Shape:
    def area(self):
        print("the area is:")
class rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("the area of rectangle is:",self.l*self.b)
l=int(input("enter the value of length:"))
b=int(input("enter the value of breadth:"))
class square(Shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print("the area of square is:",self.s*self.s)

        
r=rectangle(l,b)
r.area()
a=square(5)
a.area()
             