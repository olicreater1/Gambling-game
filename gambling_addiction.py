import random
from time import sleep

#print ascii number boxes
def print_number(number1, number2, number3, winning_array):
    sleep_var = 0.01
    print(f"Winning numbers are: {round(number1)}, {round(number2)}, {round(number3)}!")
    sleep(5)
    for i in range(40):
        number_1 = round(random.randint(0, 9))
        number_2 = round(random.randint(0, 9))
        number_3 = round(random.randint(0, 9))
        print("--- --- ---")
        print(f"|{number_1}| |{number_2}| |{number_3}|")
        print("--- --- ---")
        sleep(sleep_var)
        sleep_var = sleep_var +0.01
    
    print("--- --- ---")
    print(f"|{round(number1)}| |{round(number2)}| |{round(number3)}|")
    print("--- --- ---")

    if round(number1) == winning_array[0] and round(number2) == winning_array[1] and round(number3) == winning_array[2]:
        return "win"
    else:
        return "lose"
def gamble():
    # randomize the random winning chance array
    winning_array = [float(random.randint(0, 9)), float(random.randint(0, 9)), float(random.randint(0, 9))]
    win_lose = print_number(float(random.randint(0, 9)), float(random.randint(0, 9)), float(random.randint(0, 9)), winning_array=winning_array)
    
    if win_lose == "win":
        print("YOU WON!!!")
    else:
        print("You lost it all")  
def main():
    while True:
        start = input("Type 'spin' to spin: ")
        if start == "spin":
            gamble()
main()