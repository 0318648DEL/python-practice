x,y=eval(input("점 x,y를 입력 : "))

if 0<=x<=200 and 0<=y<=100:
    y1=-0.5*x+100
    if y<=y1:
        print("점은 삼각형 내부에 있습니다.")
    else:
        print("점은 삼각형 외부에 있습니다.")

else:
    print("점은 삼각형 외부에 있습니다.")