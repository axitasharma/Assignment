assignment 1
def sum_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    sum_result = num1 + num2
    print("The sum of {num1} and {num2} is {sum_result}")

sum_two_numbers()

#Q2
num= float(input("enter a number: "))
if (num%2==0):
    print("even")

elif (num%2!=0) :
    print("odd")
    


#Q3 (factorial)

num= int(input("enter a number: "))
fact= 1
if (num==0) or (num==1):
    fact=1
elif num<0:
    print(" cannot calculate factorial of negative numbers ")
    fact= 'Inf'
else:
    while(num>0):
        fact= fact * num
        num= num - 1
        print("the factorial of number is: ", fact)
