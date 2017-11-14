#Write a Python Program to Find the Largest Among Three Numbers
class largest:
    def largest_number(self,number1, number2, number3):
        if number1 > number2:
            if number1 > number3:
                print ('the First {} Number is Largest'.format(number1))
            else:
                print ('the third {} Number is Largest'.format(number3))
        elif number2 > number3:
            print ('the second {} Number is Largest'.format(number2))
        else:
            print ('the third {} Number is Largest'.format(number3))

    def insert(self):
        first = raw_input("Enter the First Number\n")
        if first.isalpha() == True:
            first = self.reset()
        second = raw_input("Enter the second Number\n")
        if second.isalpha() == True:
            second = self.reset()
        third = raw_input("Enter the third Number\n")
        if third.isalpha() == True:
            third = self.reset()
        self.largest_number(first, second, third)

    def reset(self):
        global x
        x = raw_input("Enter number only\n")
        return x

n = largest()
n.insert()