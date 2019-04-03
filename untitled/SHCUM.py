import math

x1,y1=eval(input("첫번째 위도와 경도 : "))
x2,y2=eval(input("두번째 위도와 경도 : "))

x1=math.radians(x1)
y1=math.radians(y1)
x2=math.radians(x2)
y2=math.radians(y2)

d=6371.01*math.acos((math.sin(x1)*math.sin(x2))+(math.cos(x1)*math.cos(x2)*math.cos(y1-y2)))

print("두 점 사이의 거리는 ",d,"입니다.")