#Calculator
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def exponential(n1,n2):
    return n1**n2


while True:
    user_choice=int(input("Select operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponential\n"))
    if user_choice in (1,2,3,4,5):
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        
        if(user_choice==1):
            print(num1," +",num2,"= ",add(num1,num2))
            
        if(user_choice==2):
            print(num1," -",num2,"= ",subtract(num1,num2))

        if(user_choice==3):
            print(num1," *",num2,"= ",multiplication(num1,num2))

        if(user_choice==4):
            print(num1," /",num2,"= ",division(num1,num2))

        if(user_choice==5):
            print(num1," ^",num2,"= ",exponential(num1,num2))


        next_operation=input("Do you want to continue:Y/N ")
        if(next_operation=='N'):
            break
    else:
        print("Invalid Input")
