import os, time

orders = []

fileExists = True
try:
  f = open("pizza.orders", "r")
  orders = eval(f.read())
  f.close()
except:
  print()
  print("Welcome to:")
  fileExists = False

heading = [["Customer", "Total Q", "Marinara Q", "Mrna Size" ,"Margherita Q", "Mgta Size", "Salami Q", "Slm Size", "Toppings Q", "Total $"]]

pizzas = ["Marinara", "Margherita", "Salami"]
pizzaPerMenuValue = 10

toppings = ["Extra Mozarella", "Extra Salami", "Extra Prosciutto"]
toppingsPerMenuValue = 5
toppingsQT = 0

pizzaType1 = ""
quantityType1 = 0
sizeType1 = ""

pizzaType2 = ""
quantityType2 = 0
sizeType2 = ""

pizzaType3 = ""
quantityType3 = 0
sizeType3 = ""

pizzaMarinaraValue = 0
pizzaMargheritaValue = 0
pizzaSalamiValue = 0


pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
toppingValue = 0
quantity = 0

#headerTable = ["Customer", "Total Q", "Marinara Q", "Mrna Size" ,"Margherita Q", "Mgta Size", "Salami Q", "Slm Size", "Toppings Q", "Total $"]

def prettyPrint():
  print()
  #for items in headerTable:  
   # print(f"{items:^14}", end="")
  #print()
  for rows in heading:
    for items in rows:
      print(f"{items:^15}", end="")
    print()
  for rows in orders:
    for items in rows:
      print(f"{items:^15}", end="")
    print()

while True:
  print()
  print("Pizzeria Napoletana Da Tiberius")
  print("---------------")
  print()
  
  print("Our menu is shown below:")
  for items in pizzas:
    print(f"Small {items:<11} ---> ${pizzaPerMenuValue} | Big {items:<11} ---> ${pizzaPerMenuValue + 10}")
    pizzaPerMenuValue += 2
  pizzaPerMenuValue -=6
  print("---------------------------------------------------------------")
  for items in toppings:
    print(f"Small {items:<16} ---> ${toppingsPerMenuValue}")
    toppingsPerMenuValue += 1
  toppingsPerMenuValue -= 3
  
  print()
  print("1. Add Pizza(s)")
  print("2. View Orders")
  
  choice = input("> ")
  if choice == "2":
    if orders != []:
      prettyPrint()
    else:
      print("Empty List. Please place an order!")
  elif choice == "1":
    name = input("What's your name\n> ")
    print(f"Got it. What's your order {name}?")
    print()
    
    while True:
      pizza = input("What pizza do you want?\n> ")
      if pizza.lower() == "marinara":
        pizzaType1 = "Marinara"
        pizzaMarinaraValue += 10
        print(f"Test: {pizzaMarinaraValue}")
        while True:
          try:
            quantityPer = input("How many?\n> ")
            quantityPer = int(quantityPer)
            quantity += quantityPer
            quantityType1 += quantityPer
            break
          except ValueError:
            print("We only work with integers. Please select accordingly!")
        size = input("Small or Big?\nDisclaimer: Big = 10 extra bucks\n> ")
        if size.lower() == "big":
          sizeType1 = size
          pizzaMarinaraValue += 10
          print(f"Test::: Pizza Marinara value = {pizzaMarinaraValue}")
          pizzaMarinaraValue *= int(quantityPer)
          print(f"Test: {pizzaMarinaraValue}")
          print(f"{pizza.title()} made big. Modified! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        elif size.lower() == "small":
          sizeType1 = size
          pizzaMarinaraValue += 0
          pizzaMarinaraValue *= int(quantityPer)
          print(f"Test: {pizzaMarinaraValue}")
          print(f"{pizza.title()} small. You got it! ") 
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue 
        print() 
        print("Added")
        print(f"TEST::: Pizza Mrna = {pizzaMarinaraValue} | Pizza Mrg = {pizzaMargheritaValue} | Pizza Slm = {pizzaSalamiValue} |Total Pizza Value = {pizzaValue} | Pizza Q = {quantity}")
        print()
        time.sleep(3)
        os.system("cls") 

      elif pizza.lower() == "margherita":
        pizzaType2 = "Margherita"
        pizzaMargheritaValue += 12
        print(f"Test: {pizzaMargheritaValue}")
        while True:
          try:
            quantityPer = input("How many?\n> ")
            quantityPer = int(quantityPer)
            quantity += quantityPer
            quantityType2 += quantityPer
            break
          except ValueError:
            print("We only work with integers. Please select accordingly!")
        size = input("Small or Big?\nDisclaimer: Big = 10 extra bucks\n> ")
        if size.lower() == "big":
          sizeType2 = size
          pizzaMargheritaValue += 10
          print(f"Test::: Pizza Margherita value = {pizzaMargheritaValue}")
          pizzaMargheritaValue *= int(quantityPer)
          print(f"Test: {pizzaMargheritaValue}")
          print(f"{pizza.title()} made big. Modified! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        elif size.lower() == "small":
          sizeType2 = size
          pizzaMargheritaValue += 0
          pizzaMargheritaValue *= int(quantityPer)
          print(f"Test: {pizzaMargheritaValue}")
          print(f"{pizza.title()} small. You got it! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        print()
        print("Added")
        print(f"TEST::: Pizza Mrna = {pizzaMarinaraValue} | Pizza Mrg = {pizzaMargheritaValue} | Pizza Slm = {pizzaSalamiValue} |Total Pizza Value = {pizzaValue} | Pizza Q = {quantity}")
        print()
        time.sleep(3)
        os.system("cls") 

      elif pizza.lower() == "salami":
        pizzaType3 = "Salami"
        pizzaSalamiValue += 14
        print(f"Test: {pizzaSalamiValue}")
        while True:
          try:
            quantityPer = input("How many?\n> ")
            quantityPer = int(quantityPer)
            quantity += quantityPer
            quantityType3 += quantityPer
            break
          except ValueError:
            print("We only work with integers. Please select accordingly!")
        size = input("Small or Big?\nDisclaimer: Big = 10 extra bucks\n> ")
        if size.lower() == "big":
          sizeType3 = size
          pizzaSalamiValue += 10
          print(f"Test::: Pizza Marinara value = {pizzaMarinaraValue}")
          pizzaSalamiValue *= int(quantityPer)
          print(f"Test: {pizzaSalamiValue}")
          print(f"{pizza.title()} made big. Modified! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        elif size.lower() == "small":
          sizeType3 = size
          pizzaValue += 10
          pizzaSalamiValue *= int(quantityPer)
          print(f"Test: {pizzaSalamiValue}")
          print(f"{pizza.title()} small. You got it! ")
          pizzaValue = pizzaMarinaraValue + pizzaMargheritaValue + pizzaSalamiValue
        print()
        print("Added")
        print(f"TEST::: Pizza Mrna = {pizzaMarinaraValue} | Pizza Mrg = {pizzaMargheritaValue} | Pizza Slm = {pizzaSalamiValue} |Total Pizza Value = {pizzaValue} | Pizza Q = {quantity}")
        print()   
        time.sleep(3)
        os.system("cls") 

      elif choice not in pizzas:
        print("We don't have. Please check out our menu and choose accordingly")
        continue
      addAnother = input("Add another?\n1. Yes\n2. No\n> ")
      if addAnother == "1":
        continue
      else:
        print("You got it!")
        break
    time.sleep(3)
    os.system("cls")     
     

    while True:  
      toppingsAgain = input("Toppings\n0. No Fucking Topics - I'm a Neapolitan Pizza Afficionado\n1. Extra Mozarella\n2. Extra Salami\n3. Extra Prosciutto\n> ")
      if toppingsAgain == "0":
        print("Yup! You really are and we congratulate you for that! Salve, nostro amico!")
        break
      elif toppingsAgain.lower() == "1":
        toppingValue += 5
        toppingsQT += 1
        print("Added")
        print()
      elif toppingsAgain.lower() == "2":
        toppingValue += 6
        toppingsQT += 1
        print("Added")
        print()
      elif toppingsAgain.lower() == "3":
        toppingValue += 7
        toppingsQT += 1
        print("Added")
        print()
      else:
        print("We don't have that")
        print()
        continue
      addAnother = input("Add another?\n1. Yes\n2. No\n> ")
      if addAnother == "1":
        continue
      else:
        print("You got it!")
        break
    time.sleep(3)
    os.system("cls")

    #quantity = input("How many\n> ")
    #print("Noted")
    #print()
    total = pizzaValue + toppingValue
    print(f"Total = {total}$")
    orderPerCustomer = [name, quantity, quantityType1, sizeType1, quantityType2, sizeType2, quantityType3, sizeType3, toppingsQT, total]
    orders.append(orderPerCustomer)

    if fileExists:
      try:
        os.mkdir("bah")
      except:
        pass
      backup_file = "bah.txt"
      os.system(f"cp pizza.orders bah/{backup_file}")

    f = open("pizza.orders", "w")
    f.write(str(orders))
    f.close()

    print("--------------")
    print(f"TEST::::: Pizza Value = ${pizzaValue}| toppings Value = ${toppingValue} | Q = {quantity}")
    print("--------------")
    print("Today's Orders:")
    prettyPrint()
    print("--------------")
    
    pizzaMarinaraValue = 0
    pizzaMargheritaValue = 0
    pizzaSalamiValue = 0
    toppingValue = 0
    toppingsQT = 0
    quantity = 0
    quantityType1 = 0
    quantityType2 = 0
    quantityType3 = 0
    sizeType1 = ""
    sizeType2 = ""
    sizeType3 = ""


    oneMoreTime = input("Continue?\n1. Yes\n2. No\n> ")
    if oneMoreTime == "1":
      continue
    else:
      print("Done with the orders for today")
      break
  
  else:
    print("You can only place an order or see the current ones")
    continue
  
  

time.sleep(3)
os.system("cls")


