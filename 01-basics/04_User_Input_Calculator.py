# Define Function
def two_number_calculator(first_num, second_num, operation_symbole):
    print("two_number_calculator started...")
    operation_symbole_list = ["+","-","*","/"]
    if(first_num != "" and second_num != ""):
        if(operation_symbole_list.__contains__(operation_symbole)):
            if(operation_symbole=="+"):
                return f"Addition: {first_num + second_num}"
            elif(operation_symbole=="-"):
                return f"Subtraction: {first_num - second_num}"
            elif(operation_symbole=="*"):
                return f"Multiplication: {first_num * second_num}"
            elif(operation_symbole=="/"):
                return f"Division: {first_num / second_num}"
        else:
            print("Incorrect Symbole | Please specify among '+ - * /' ")
    else:
        print("Please Enter correct number !")
    print("two_number_calculator completed.")

# Get user inputs and assign it in the variables
num1 = input("Enter first number: \n")
num2 = input("Enter second number: \n")
oper = input("Please specify calculation operation among '+ - * /' : \n")

# Print the result of the calculator
print(two_number_calculator(float(num1),float(num2),oper))