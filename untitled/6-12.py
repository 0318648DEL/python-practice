def printChars(ch1,ch2,numberPerLine=10):
    if ch1>="1" and ch2<="z":
        i=0
        for f in range(ord(ch1),ord(ch2)+1):
            print(chr(f),end="")
            i+=1
            if i%numberPerLine==0:
                print()


printChars("1","z")