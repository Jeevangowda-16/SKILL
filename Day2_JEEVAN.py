rows=[]
transpose=[]
cols=[]
matrix=[]
def mat():
 global m
 n=int(input("enter the number of rows:"))
 m=int(input("enter the number of cols:"))
 print("Enter element row wise")
 for i in range(n):
    rows=list(map(int,input().split()))
    matrix.append(rows)
 for rows in matrix:
   print(rows)
def transp():
 transpose=[[rows[i]for rows in matrix]for i in range(m)]
 for rows in transpose:
     print(rows)
print(mat())
print(transp())



    
 
