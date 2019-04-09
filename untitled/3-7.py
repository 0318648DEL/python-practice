import time

n=int(time.time()*10000)%26
print(chr(ord('A')+n))