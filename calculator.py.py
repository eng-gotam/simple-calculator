# simple calculator
print("****SIMPLE CALCULATOR****")
print("***ENTER 1 TO START THE CALCULATION***")
print("***ENTER 2 TO EXIT FROM THE PROGRAM***")

enter_num = int(input("enter the number to start program:"))

while True:
    if enter_num == 1:

        num1 = int(input("Enter the number 1:"))
        num2 = int(input("Enter the number 2:"))
        operand = input("Enter the operand:")

        if operand == "+":
            print(f"The Sum of {num1} and {num1} is {num1+num2}")
        elif operand == "-":
            print(f"The Substraction of {num1} and {num1} is {num1-num2}")
        elif operand == "*":
            print(f"The Multiplication of {num1} and {num1} is {num1*num2}")
        elif operand == "/":
            print(f"The division of {num1} and {num1} is {num1/num2}")
        else:
            print("Invalid operand:")

        enter_num = int(input("Enter the number again:")) 
    elif enter_num == 2:
        print("THANKS! you are Existed ")
        break

    else:
        print("Your number is not valid:")
        break
    