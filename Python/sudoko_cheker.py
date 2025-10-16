def sudochecker(r):
    #check rows
    for i in range(9):
        a=[int(x) for x in r[i]]
        a.sort()
        for x in a:
            if x != a.index(x)+1:
                print(21)
                return False
    #check coloumns
    for i in range(9):
        a=[]
        for j in range(9):
            a.append(int(r[j][i]))
        a.sort()
        print(a,"oasdbf")
        for x in a:
            if x != a.index(x)+1:
                print(234)
                return False
    #check boxes
    row,col=0,0
    for i in range(3):
        for j in range(3):
            a=[]
            for x in range(3*i,3*i+3):
                for y in range(3*j,3*j+3):
                    a.append(int(r[x][y]))
            a.sort()
            for x in a:
                if x != a.index(x)+1:
                    print(1312)
                    return False
     return True           

if __name__=="__main__":
    r=[]
    for i in range(9):
        z=input().split()
        r.append(z)
    print(sudochecker(r))

    
