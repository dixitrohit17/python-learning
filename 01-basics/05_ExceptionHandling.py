# Decision Making - If Else
def check_exception_function(inputnumber):
    try:
        print(f"output:  {int(inputnumber) +  100}")
    except:
        print("An error occurred.")

inputnumber = input("Enter any number: \n")

check_exception_function(inputnumber)