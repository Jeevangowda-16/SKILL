n=int(input("SIZE:"))
for i in range(n):
 for j in range(n-i):
  print("*",end='')
 print()
     
n=int(input("SIZE:"))
for i in range(n+1):
  print("*"*i)

n=int(input("SIZE:"))
for i in range(n):
  print(" "*(n-i)+"*"*i)
