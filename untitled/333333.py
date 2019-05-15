att=0
def division(N):
    global att
    att+=1
    return ((N*att)+att)+division(N)

s=eval(input(" "))
print(division(s))