nor, tip= [float(x) for x in input("소계와 팁을 입력하세요. : ").split()]

total=nor+(nor*(tip/100))

print("팁은 ",tip,"이고 총액은 ",total,"입니다.")