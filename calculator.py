print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = int(input("Choose your operation: "))

if choice in [1, 2, 3, 4]:
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))
    
    if choice== 1:
        result = number1 + number2
        print("The result of the operation is:", result)
        
    elif choice == 2:
        result = number1 - number2
        print("The result of the operation is:", result)
        
    elif choice == 3:
        result = number1 * number2
        print("The result of the operation is:", result)
        
    elif choice ==4:
        if number2 ==0:
            print("Division by zero is not possible.")
            
        else:
            result = number1 // number2
            print("The result of the operation is:", result)
    
else:
    print("Invalid operation entered.") 