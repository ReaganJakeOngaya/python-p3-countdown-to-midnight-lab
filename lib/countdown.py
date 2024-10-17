# your code goes here!
def countdown():
    x = 10
    while x >= 0:
        if x == 0:
            print("HAPPY NEW YEAR")
        else:
            print(f'{x} SECOND(S)!')
        x -= 1
countdown()