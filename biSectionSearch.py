#Matthew Shrago
#implementation of bisection search.
import math
low = 0
high = 100
ans = int((high + low)/2)

print "Please think of a number between 0 and 100!"
while ans != 'c':
    #print high, low
    print "Is your secret number " + str(ans) + "?",
    number = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter\n'c' to indicate I guessed correctly. ")
    if number == 'c':
        break
    if number == 'l':
        low = ans
    elif number == 'h':
        high = ans
    else:
        print "Sorry, I did not understand your input."
    ans = int((high + low)/2)

print "Game over. Your secret number was: " + str(ans)

    
    