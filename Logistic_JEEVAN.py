print("IMPORT AND EXPORT")
print("Storage is empty")
goods = {} 
class shop:
 def Dealer():
  global goods
  global n
  n = int(input("Enter how many goods entering Gowdon: "))
  for i in range(n):
    key = input("Item: ")
    value =int(input("Quantity: \n"))
    goods[key] = value
  print("\nStored Goods")
  print(" ITEM:QUANTITY")
  for key,value in goods.items():
   print(f" {key}:{value}")
 def Customer():
   print("\nStored Goods")
   print(" ITEM:QUANTITY")
   for key,value in goods.items():
      print(f"{key}:{value}")
   print("\nEnter customer needs:")
   m = int(input("Enter how many goods customer needs: "))  
   Need = {}   
   for i in range(m):
    key = input(f"Enter Item {i+1}: ")
    value=int(input(f"Quantity {i+1}:"))
    if key in goods:
      if goods[key]>=value:
         Need[key]=value
         goods[key]-=Need[key]
    else:
      print(f"Error: {key} is not available in storage.")
   print("\nCustomer Needs:", Need)
   print(Need,"items are delivered.")
   print("\nUpdated Goods")
   print(" ITEM:QUANTITY")
   for key,value in goods.items():
    print(f"{key}:{value}")
if __name__=="__main__":
 while True:
  print('1.DEALER')
  print('2.BUYER')
  print('3.EXIT')
  choice=int(input("Are you BUYER or DEALER:"))
  if choice==1:
    shop.Dealer()
  elif choice==2:
    shop.Customer()
  elif choice==3:
    break
