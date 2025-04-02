num1=int(input("enter you first number: "))
num2=int(input("Enter you second number:"))
choice=input("enter your choice (+,-,*,/)")
if choice=="+":
    print(num1+num2)
elif choice=="-":
    print(num1-num2)
elif choice=="*":
    print(num1*num2)
elif choice=="/":
    print(num1/num2)
else:
    print("you entered you wrong information")