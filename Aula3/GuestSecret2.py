import random


with open ("score.txt", 'r') as best_file:
    best_score = best_file.read()
 #   print(len (best_score))
 #   for line in best_score:
    print("Best Score is : " + best_score)

secret = random.randint(1,30)
attempts = 0

while True:

    guess =int(input("Guess the secret number ( between 1 end 30):"))

    if guess == secret :
        print("Congrulatations")
        with open("score.txt", 'r') as best_file:
            best_score = best_file.read()
            if int(best_score) == attempts :
                print("New best score")

        break
    elif guess < secret:

        print ("Increase value")
        attempts = attempts + 1
        if attempts < int(best_score):
            with open("score.txt", 'w') as best_file:
                best_file.write(str(attempts))
    elif guess > secret:
        print ("Decrease Value")
        attempts = attempts + 1
        if attempts < int(best_score):
            with open("score.txt", 'w') as best_file:
                best_file.write(str(attempts))


