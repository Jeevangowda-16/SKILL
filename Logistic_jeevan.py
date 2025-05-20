print("IMPORT AND EXPORT")
print("Storage is empty")
goods = [] 
class shop:
 def Dealer():
  global goods
  n = int(input("Enter how many goods entering Gowdon: "))
  for i in range(n):
    element = input(f"Enter element {i+1}: ")
    goods.append(element)
  print("Stored Goods:", goods)
 def Customer():
   print("GOWDON ITEMS:",goods)
   print("\nEnter customer needs:")
   m = int(input("Enter how many goods customer needs: "))  
   Need = []   
   for i in range(m):
    element = input(f"Enter element {i+1}: ")
    if element in goods:
      goods.remove(element)  
    else:
      print(f"Error: {element} is not available in storage.")
    Need.append(element)
   print("\nCustomer Needs:", Need)
   print(Need,"items are delivered.")
   print("Updated Storage:", goods) 
if __name__=="__main__":
 while True:
  print('1.DEALER')
  print('2.BUYER')
  print('3.EXIT')
  choice=int(input("Are you BUYER or DEALER."))
  if choice==1:
    shop.Dealer()
  elif choice==2:
    shop.Customer()
  elif choice==3:
    break
