class Rectangle:
    def __init__(self,width=1,height=2):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return 2*(self.width+self.height)
    def infoPrint(self):
        print("폭 : {0}, 높이 : {1}, 둘레 : {2}, 넓이 : {3}".format(self.width,self.height,self.getPerimeter(),self.getArea()))

r1=Rectangle(4,10)
r2=Rectangle(3.5,25.7)

r1.infoPrint()
r2.infoPrint()