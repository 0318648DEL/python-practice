f=eval(input("화씨 -58도와 41도 사이의 온도를 입력하세요 : "))
while f<-58 and f>41:
    f = eval(input("화씨 -58도와 41도 사이의 온도를 입력하세요 : : "))

w=eval(input("풍속을 시간당 마일 단위로 입력하세요 : "))
while w<=2:
    w = eval(input("풍속을 시간당 마일 단위로 입력하세요 : "))

t=35.74+0.6215*f-35.75*(w**0.16)+0.4275*f*(w**0.16)
print("체감온도는 ",t)