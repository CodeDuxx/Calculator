def calculator():

    name = str(input("What is your name? :"))

    with open("userinputs.txt", "a") as f:
        
        f.write("User = ")
        
        f.write(name)
        
        f.write('\n')
            
    print("Hi ", name,"I am Cal your personal calculator")

    T = True

    while T == True : 

        userinput = input("So what do we want to do today \n[Type the things in the square brackets to choose the option]\n1. Addition [+]\n2. Subtraction [-]\n3. Multiplication [*]\n4. Division [/]\n5. Remainder Finder [%]\n6. Square [^2]\n7. Cube [^3]\n8. Power to Any Number [^x]\n:")
        
        if userinput == "+" : 
            
            num1 = int(input("Enter the first number: "))

            num2 = int(input("Enter the second number: "))

            ans = num1 + num2
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
                
                T = False
        
        elif userinput ==  "-" : 
            
            num1 = int(input("Enter the first number: "))

            num2 = int(input("Enter the second number: "))

            ans = num1 - num2
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
                T = False
        
        elif userinput == "*" : 

            num1 = int(input("Enter the first number: "))

            num2 = int(input("Enter the second number: "))

            ans = num1 * num2
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
                T = False 

        elif userinput == "/" : 

            num1 = int(input("Enter the first number: "))

            num2 = int(input("Enter the second number: "))

            ans = num1 / num2
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
                T = False   

        elif userinput == "%" :

            num1 = int(input("Enter the first number: ")) 

            num2 = int(input("Enter the second number: "))

            ans = num1 % num2
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
                T = False

        elif userinput == "^2" : 

            num1 = int(input("Enter the first number: "))

            ans = num1**2
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
                T = False
        
        elif userinput == "^3" : 

            num1 = int(input("Enter the first number: "))

            ans = num1**3
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
                T = False     

        elif userinput == "^x" : 

            num1 = int(input("Enter the first number: "))
            
            num2 = int(input("Enter the power: "))

            ans = num1**num2
            
            print("Your answer is ", ans)
            
            ans1 = input("Do you want to continue using me (Cal)\n[y/n]\n:")
            
            if ans1 == 'y' : 
                
                T = True 
            
            else : 
            
                T = False 

        else: 
        
            print("Error")
        
            break        