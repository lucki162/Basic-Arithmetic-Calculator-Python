while True:
  a = int(input("Enter the first number : "))
  b = int(input("Enter the second number : "))
  print(f"The result of {a} + {b} is {a+b}")
  print(f"The result of {a} - {b} is {a-b}")
  print(f"The result of {a} / {b} is {a/b}")
  print(f"The result of {a} * {b} is {a*b}")
  
  confirmated = input("Is this program finished? (Y/N)")
  if confirmated == "Y":
    print("Thank You for using this program")
    break
  elif confirmated == "y":
    print("Thank You for using this program")
    break
  elif confirmated == "yes":
    print("Thank You for using this program")
    break
  elif confirmated == "Yes":
    print("Thank You for using this program")
    break
  elif confirmated == "N":
    print("Please use the program again")
  elif confirmated == "n":
    print("Please use the program again")
  elif confirmated == "No":
    print("Please use the program again")
  elif confirmated == "no":
    print("Please use the program again")
    
  else :
    print("Invalid input")
    break