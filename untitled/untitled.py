#대충 그러하지 않을까란 생각을 하는 중이다
#아마도

class Person:
    Name="Default Name"
    def Print(self):
        print("My Name is {0}".format(self.Name))

class MyClass:
    def __init__(self,value):
        self.Value=value#인스턴스 변수 Value생성
        print("Class is created with Value = {0} ".format(self.Value))
    def __del__(self):
        print("Class is deleted")

class CounterManager:
    __insCount=0
    def __init__(self):
        CounterManager.__insCount+=1

    def printinstanceCount():
        print("Instance Count : ",CounterManager.__insCount)

class Person:
    def __init__(self,
