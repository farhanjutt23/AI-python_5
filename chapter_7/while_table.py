'''Get the input the a number from the user to print the table of the anynumber'''
table=int(input("Enter the number"))
i=0
while(i<=10):
    print(f"{table} * {i} = {table*i}")
    i+=1
    