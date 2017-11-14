#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
def check(letter):
    lower,upper = 0,0
    for i in letter:
        if i.islower() == True:
             lower = lower+1
        if i.isupper()  == True:
             upper = upper+1

    print("the sum of the lower {} and upper {} in word {}".format(lower,upper,letter))

word = raw_input('Enter the String\n')
check(word)






