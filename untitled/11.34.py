def getRightmostLowestPoint(points):
    xr=points[0][0]
    yl=points[0][1]
    index=None
    for i in range(0,len(points)):
        if yl>points[i][1]:
            yl=points[i][1]
            index=i

        elif yl==points[i][1] and xr<points[i][0]:
            xr=points[i][0]
            index=i
    return points[index]

lst=input("점 6개를 입력하세요 :")
lst=lst.split()
lst=[eval(i) for i in lst]
lst=[[lst[i],lst[i+1]] for i in range(0,len(lst),2)]

point_right_down=getRightmostLowestPoint(lst)

print("최우측 하단의 점 {0:.1f}.{1}".format(point_right_down[0],point_right_down[1]))