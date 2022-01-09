# Variables
var_num1 = 100
var_num2 = 10

# Calculation
print(f"Addition: {var_num1 + var_num2}")
print(f"Subtraction: {var_num1 - var_num2}")
print(f"Multiplication: {var_num1 * var_num2}")
print(f"Division: {var_num1 / var_num2}")

# Function
def two_number_operation():
    print("two_number_operation started")
    print(f"Addition: {var_num1 + var_num2}")
    print("two_number_operation completed.")
    
two_number_operation()

# Function with parameter
def three_number_operation(var_num3):
    print("three_number_operation started")
    print(f"Addition: {var_num1 + var_num2 + var_num3}")
    print("three_number_operation completed.")
    
three_number_operation(10)


# Function with parameter and IF-ELSE
def two_number_calculator(first_num, second_num, operation_symbole):
    print("two_number_calculator started")
    if(first_num !="" and second_num != ""):
        if(operation_symbole=="+"):
            print(f"Addition: {first_num + second_num}")
        elif(operation_symbole=="-"):
            print(f"Subtraction: {first_num - second_num}")
        elif(operation_symbole=="*"):
            print(f"Multiplication: {first_num * second_num}")
        elif(operation_symbole=="/"):
            print(f"Division: {first_num / second_num}")
        else:
            print("Incorrect Symbole | Please specify among '+ - * /' ")
    else:
        print("Please Enter correct number !")
    print("two_number_calculator completed")

two_number_calculator(10,10,"+")
two_number_calculator(10,10,"u")
two_number_calculator(10,10,"")

# Function with parameter and Variable scope
global_vaiable = "I am a global variable"

def scope_check():
    local_vaiable = "I am a local variable"
    print(global_vaiable)
    print(local_vaiable)
    
scope_check()
print(global_vaiable)    ## global_vaiable is defined outside the function so it will be accessable. 
#print(local_vaiable)    ## local_vaiable is defined inside the function so it will give the error on accessing. 