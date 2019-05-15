
filename=input("파일 이름을 입력하세요 : ")
f=open(filename)
content=f.read()
characters=len(content)
words=content.split()
lines=content.split('\n')
print("문자 : ",characters,",단어 : ",len(words),",행 : ",len(lines))