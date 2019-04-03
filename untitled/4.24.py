import random
number=random.randint(0,51)
if number//13==0:
    pattern="Clover"
elif number//13==1:
    pattern="Diamond"
elif number//13==2:
    pattern="Heart"
else:
    pattern="Spade"

if number%13==0:
    n='A'
elif number%13==10:
    n='J'
elif number%13==11:
    n='Q'
elif number%13==12:
    n='K'
else:
    n=str(number%13+1)

print("당신이 뽑은 카드는 {0} {1}".format(pattern,n))