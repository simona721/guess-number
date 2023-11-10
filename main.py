import random

userNumber = input("Enter a number between 1 - 100: ")

computerNumber = str(random.randint(1,100))

if (userNumber == computerNumber):
    print(userNumber)
    print(computerNumber)
    print("You guessed the number")
elif(userNumber > computerNumber):
    print(userNumber)
    print(computerNumber)
    print("Your guess was high")
elif(userNumber < computerNumber):
    print(userNumber)
    print(computerNumber)
    print("Your guess was low")



