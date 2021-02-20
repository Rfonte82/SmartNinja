import random

secret = random.randint(1,10)
#guess = False

# while guess != secret:
for x in range(1,5,1):
    print("Try "+str(x))
    guess =int(input("Guess the secret number ( between 1 end 10):"))

    if guess == secret :
        print( " Congrulatations ")
        break
    elif guess < secret:
        print ("Increase value")
    elif guess > secret:
        print ("Decrease Value")
    else:
        print ("Try againg")

print(" Game Over  ")
print(" Secret Number is " + str(secret))