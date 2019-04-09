import math

def dist(x1,y1,x2,y2):
    d=6371.01 * math.acos((math.sin(x1) * math.sin(x2)) + (math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))
    return d

def area(x1,y1,x2,y2,x3,y3):
    x1=math.radians(x1)
    x2=math.radians(x2)
    x3=math.radians(x3)
    y1=math.radians(y1)
    y2=math.radians(y2)
    y3=math.radians(y3)
    s1=dist(x1,y1,x2,y2)
    s2=dist(x2,y2,x3,y3)
    s3=dist(x1,y1,x3,y3)
    s = (s1 + s2 + s3) / 2
    r = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
    return r

gs1,gx1=eval(input("도시1의 위도와 경도를 입력하세요 : "))
gs2,gx2=eval(input("도시2의 위도와 경도를 입력하세요 : "))
gs3,gx3=eval(input("도시3의 위도와 경도를 입력하세요 : "))
gs4,gx4=eval(input("도시4의 위도와 경도를 입력하세요 : "))


tri1=area(gs1,gx1,gs2,gx2,gs4,gx4)
tri2=area(gs2,gx2,gs3,gx3,gs4,gx4)

print("추정넓이는 ",tri1+tri2)