import os           #For clearing the console
import time         #For path creation

Count = 0           #The main iterator
NumsToCheck = 0     #The amount of numbers to check
NumToStopAt = 0     #The number that the program will stop checking at

#Checks to see if a given number is prime
def IsPrime(num):

    divisor = 2
    halfnum = num/2

    #Begin main calculation loop  
    while True:
        if num % divisor == 0:      # If this number is wholey divisible by a number smaller than half of itself, then it cannot be a prime.
            return False
        else:
            divisor += 1
            if divisor > halfnum:   # If the divisor has surpassed half of the size of the num in question, then the rest of the divisors can't
                return True         # possibly be divisible to 0.
            
#Main Loop
while True:
    NumsFound = 0

    #Asking what number to start at
    while True:
            try:
                Count = int(input("Please enter the number you wish to start searching at:\n>"))
                if Count >= 0:
                    break
                else:
                    print ("Invalid input, please enter a number higher than 1:\n")
            except:
              print("Invalid input, please enter a number to try again:\n")

    #Asking how many numbers to check
    while True:
            try:
                NumsToCheck = int(input("Please enter the amount of numbers you wish to check:\n>"))
                if NumsToCheck >= 0:
                    break
                else:
                    print ("Invalid input, please enter a number higher than 1:\n")
            except:
              print("Invalid input, please enter a number to try again:\n")


    os.system("cls")
    print ("Searching...")

    # Open a file to save to
    t = str(time.ctime())
    t = t.replace("  ", "_")
    t = t.replace(" ", "_")
    t = t.replace(":", ".")
    f = open(f"PrimeNumbers_{t}.txt","w+")

    #Manually get through the edge cases that IsPrime can't/shouldn't do for optimization sake
    if Count == 0:
        Count += 1
        NumsToCheck -= 1
    if Count == 1:
        Count += 1
        NumsToCheck -= 1
    if Count == 2:
        print(str(Count))
        f.write(str(Count) + "\n")
        NumsFound += 1
        Count += 1
        NumsToCheck -= 1

    #Checking the specified numbers
    NumToStopAt = Count + NumsToCheck
    while Count < NumToStopAt:

        if IsPrime(Count):
            print(str(Count))
            f.write(str(Count) + "\n")
            NumsFound += 1

        Count += 1

    f.close()
    print (f"\nLog file \"PrimeNumbers_{t}.txt\" created.\n{NumsFound} prime numbers were found.\nYou may continue to search for numbers:\n\n")