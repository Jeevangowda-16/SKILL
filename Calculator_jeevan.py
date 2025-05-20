
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
n1=int(input("Enter the number 1:"))
n2=int(input("Enter the number 2:"))
while True:
 print('1','Add')
 print('2','subtract')
 print('3','muliply')
 print('4','division')
 print('5','End')
 n=int(input("Enter the choice"))
 if n==1:
     print(add(n1,n2))
 elif n==2:
     print(sub(n1,n2))
 elif n==3:
     print(mul(n1,n2))
 elif n==4:
     print(div(n1,n2))
 else:
     print("Invalid choice.")