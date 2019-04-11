from tkinter import *

filename=input("파일 이름 입력 : ")
f=open(filename)
content=f.read()
histogram=[0]*26
new=content.lower()
for c in new:
    if c.isalpha():
        histogram[ord(c)-ord('a')]+=1
for i in range(26):
    print(chr(ord('a')+i),"빈도수 : ",histogram[i])

f.close()