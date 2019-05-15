class Fan:
    def __init__(self,speed=None,radius=None,color=None,on=None):
        SLOW = 1
        MEDIUM = 2
        FAST = 3
        if color is None:
            color="blue"

        if on is None:
            on=False

        if speed is None:
            speed=SLOW
        elif speed is "MEDIUM":
            speed=MEDIUM
        elif speed is "FAST":
            speed=FAST
        else:
            speed=SLOW

        if radius is None:
            radius=5

        self.__speed=speed
        self.__radius=radius
        self.__color=color
        self.__on=on
    def getSpeed(self):
        return self.__speed
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
    def getOn(self):
        return self.__on
    def setSpeed(self,speed):
        self.__speed=speed
    def setRadius(self,radius):
        self.__radius=radius
    def setColor(self,color):
        self.__color=color
    def setOn(self,on):
        self.__on=on
    def getFaninfo(self):
        print("속도 : {0}, 크기 : {1}, 색깔 : {2}, 켜짐 : {3}".format(self.__speed,self.__radius,self.__color,self.__on))


fan1=Fan("FAST",10,"yellow",True)
fan2=Fan("MEDIUM")
fan1.getFaninfo()
fan2.getFaninfo()