
def Slump(*strs):
    result=[]
    count=strs.__len__()
    brake=0

    for x in range(count):
        brake=0
        if len(strs[x])>2:
            for y in range(len(strs[x])):
                if y==0:
                    if not strs[x][y]=='D' and not strs[x][y]=='E':
                        result.append("NO")
                        brake=1
                        break
                elif y==len(strs[x])-1:
                    if not strs[x][y]=='G' or not strs[x][y-1]=='F':
                        result.append("NO")
                        brake=1
                        break
                else:
                    if strs[x][y-1]=='D'or strs[x][y-1]=='E':
                        if not strs[x][y]=='F':
                            result.append("NO")
                            brake=1
                            break
                    elif strs[x][y-1]=='F':
                        if not strs[x][y] == 'D' and not strs[x][y] == 'E' and not strs[x][y] == 'F':
                            result.append("NO")
                            brake = 1
                            break
            if not brake:
                result.append("YES")

        else:
            result.append("NO")

    return result


print(Slump("DFG","EFG","DFFFFFG","DFDFDFDFG","DFEFFFFFG"))