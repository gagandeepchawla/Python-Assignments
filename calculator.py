#Write a Python Program to Make a Simple Calculator
def calculator(number1,number2):
    reasult =0
    retry = True
    while retry:
        print ("1 for add")
        print("2 for subtract")
        print ("3 for multiple")
        print ("4 for divide")
        temp = int(raw_input("Enter choice\n"))
        if temp == 1:
            reasult = number1 + number2
            print ("the sum of the number", reasult)
            retry = False
        if temp == 2:
            reasult = number1 - number2
            print ("the subtract of the number", reasult)
            retry = False
        if temp == 3:
            reasult = number1 * number2
            print ("the multiple of the number", reasult)
            retry = False
        if temp == 4:
            reasult = number1 / number2
            print ("the divie of the number", reasult)
            retry = False
    else:
        retry = True


first = int(raw_input("Enter the First Number\n"))
second = int(raw_input("Enter the second Number\n"))
calculator(first,second)