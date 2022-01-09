def for_loop_example(table_num):
    try:
        table_num = int(table_num)
        print(f"Table of {table_num} is:")
        for i in range(1,11):
            print(table_num*i)
    except ValueError:
        print("An error occurred.")

for_loop_example(input("Ebter the number to find the table:  \n"))
