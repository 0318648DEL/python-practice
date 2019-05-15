
def decimalToBinary(value):
    if value==0:
        return ""
    return decimalToBinary(value//2)+str(value%2)

inp=eval(input("10진수를 입력해주세요 : "))
print("{0}의 2진수는 {1}입니다".format(inp,decimalToBinary(inp)))