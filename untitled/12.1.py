class Triangle:
    def __init__(self,side1=None,side2=None,side3=None,color="black",fill=1):
        if side1 is None:
            side1=1.0

        if side2 is None:
            side2=1.0

        if side3 is None:
            side3=1.0

        self.__side1=side1
        self.__side2=side2
        self.__side3=side3
        self.__color=color
        self.__fill=fill

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        total=((((4*(self.__side1**2)*(self.__side2**2))-(self.__side1**2+self.__side2**2-self.__side3**2)**2))**0.5)*0.25
        return total

    def getParameter(self):
        return self.__side1+self.__side2+self.__side3

    def getTriangleInfo(self):
        print(self.__str__())
        print("색깔 : "+color+" 채움 여부 : ",bool(self.__fill))

    def __str__(self):
        return "Triangle: side1 = "+str(self.__side1)+", side2 = "+str(self.__side2)+", side3 = "+str(self.__side3)


side1,side2,side3=eval(input("삼각형의 세 변을 입력하세요(기본값 : 1) : "))
color=input("삼각형의 색깔을 입력하세요(기본값 : 검은색) : ")
fill=eval(input("삼각형 내부의 채움 여부를 1과 0으로 표현해주세요 : "))
tri=Triangle(side1,side2,side3,color,fill)
tri.getTriangleInfo()
print("둘레 : ",tri.getParameter())
print("넓이 : ",tri.getArea())