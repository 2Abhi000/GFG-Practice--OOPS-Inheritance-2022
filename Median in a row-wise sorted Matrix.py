#Median in a row-wise sorted Matrix
row=int(input("Row: "))
col=int(input("Col: "))
a=[[int(input("Value: ")) for i in range(row)]for j in range(col)]
#bruteforce approach
def median_mat(mat):
    if len(mat)==0:
        print(0)
    else:
        a=[]
        for i in range(len(mat)):
            for j in range(len(mat)):
                a.append(mat[i][j])
        a.sort()
        s=0
        end=len(a)
        mid=(s+end)//2
        print(a[int(mid)])
ans=median_mat(a)
