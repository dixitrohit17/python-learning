def calculate_factorial(input_num):
    try:
        do_fact = input_num = int(input_num)
        while input_num > 1:
            input_num = input_num - 1
            do_fact *= input_num
        return do_fact
    except ValueError:
        print("Exit from the application")

input_number=""
while input_number != "exit":
    input_number = input("Enter number to calculate the factorial or type 'exit' to close the program: \n")
    print(f"Factorial of {input_number} is {calculate_factorial(input_number)} ")
else:
    print("Application exits")
