# Project 1
# Tradidional calaculator 

print("\t \t Calaculator\n")
op= input("select operator\n + for addition\n - for subtraction\n * for multiplication\n / for division\nYou choose :  ")
no1= int(input("Enter first number\n"))
no2= int(input("Enter second number\n"))

if op == "+":
    print("The sum of two numbers is: ",end="")
    print(no1+no2)
elif op == "-":
    print("The subtraction of two numbers is: ",end="")
    print(no1-no2)
elif op == "*":
    print("The multiplication of two numbers is: ",end="")
    print(no1*no2)
elif op == "/":
    print("The division of two numbers is: ",end="")
    print(no1/no2)
else:
    print("Choose the correct operator as menctioned above")
