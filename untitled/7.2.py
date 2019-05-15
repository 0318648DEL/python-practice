class Stock:
    def __init__(self,symbol,name,previousClosingPrice,currentPrice):
        self.__symbol=symbol
        self.__name=name
        self.__previousClosingPrice=previousClosingPrice
        self.__currentPrice=currentPrice

    def getSymbol(self):
        return self.__symbol
    def getName(self):
        return self.__name
    def getPrevious(self):
        return self.__previousClosingPrice
    def getCurrent(self):
        return self.__currentPrice
    def setPrevious(self,previousClosingPrice):
        self.__previousClosingPrice=previousClosingPrice
    def setCurrent(self,currentPrice):
        self.__currentPrice=currentPrice
    def getChangePercent(self):
        return ((self.__currentPrice-self.__previousClosingPrice)/self.__previousClosingPrice)*100

s=Stock("INTC","Intel Co",20500,20350)
print("Symbol : ",s.getSymbol())
print("Name : ",s.getName())
print("Previous Closing Price : ",s.getPrevious())
print("Current Price : ",s.getCurrent())
print("Change Percent : ",s.getChangePercent())
