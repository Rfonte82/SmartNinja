
KmtoMiles = 0.621371
answer = "Y"
while True:

    if answer == "Y" or answer == "y":
        print(" Welcome to Unit Converter")
        km = float(input("Please insert number of km"))
        print("Total miles is " + str(km * KmtoMiles))
        answer = input(" Do you want convert more ?")
    elif answer != "Y" :
        print("See you soon")
        break








