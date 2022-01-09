# Variables
var_num1 = 100

# Decision Making - If Else
def check_greater_number(_number):
    try:
        if(var_num1 > _number): 
            print(f"Entered number is lesser")
        else: print(f"Entered number is greater")    
    except ValueError:
        print("Exception")

# Decision Making - Nested If Else
def check_digit_or_decimal_number(_number):
    try:
        if(_number != ""):
            if _number.isdigit():
                print(f"{_number} is a digit number.")
                check_greater_number(float(_number))
            else:
                print("Entered number is not digit.")
    except ValueError:
        print("Exception")
        
_number = input("Enter the digit: \n")

check_digit_or_decimal_number(_number)