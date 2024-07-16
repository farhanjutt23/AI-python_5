'''write a proram that the given number is the prime or not prime'''
number=int(input("Enter the number"))
for i in range(2,number):
    if(number%i)==0:
        print("The number is the not prime")
        break
else:
    print("The given number is the prime ")
    

