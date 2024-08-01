# Calculator using Python 

num1 = int(input("Enter First no.: "))
sign = input("Enter the Sign: ")
num2 = int(input("Enter Second no.: "))

if sign == '+':
    print("Your Result is:" + str(num1+num2))
elif sign == '-':
    print('Your Result is:' + str(num1-num2))
elif sign == '*':
    print('Your Result is:' + str(num1*num2))
elif sign == '/':
    print('Your Result is:' + str(num1/num2))

else:
    print("Please Enter +,-,*,/")