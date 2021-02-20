
while True:

    answer = int (input(" Please Insert a Number between 1 and 100"))

    rest = answer%3
    if rest == 0:
        print("fizz")

    rest = answer%5
    if rest == 0:
        print("buzz")

    #print(" Rest Vale " + str(rest))

    again = input(" Do you want convert more ?")

    if  again != "Y" :
        print("See you soon")
        break


