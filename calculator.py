while True:

        print("=================")
        print("  CALCULATOR")
        print("=================")


        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exponential")
        print("6 - Modulus")

        choice = int(input("Choose your operation: "))

        if choice in [1, 2, 3, 4, 5, 6]:
            number1 = float(input("Enter your first number: "))
            number2 = float(input("Enter your second number: "))
            
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
                    result = number1 / number2
                    print("The result of the operation is:", result)
                    
            elif choice == 5:
                try:
                 result = number1 ** number2
                 print("The result of the operation is:", result)

                except OverflowError:
                 print("The number is too large to calculate.")
                
            elif choice == 6:
                if number2 == 0:
                    print("Modulus by zero is not possible.")
                
                else:
                    result = number1 % number2
                    print("The result of the operation is:", result)
            
        else:
            print("Invalid operation entered.")
            
            
        again = input("Do you want to perform another calculation? (y/n): ")

        if again.lower() == "n":
            print("Thank you for using the CALCULATOR!")
            break
