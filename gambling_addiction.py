import random
from time import sleep

#print ascii number boxes
def print_number(number1, number2, number3, winning_array):
    sleep_var = 0.01
    print("               --- --- ---")
    print(f"Winning slots: |{round(number1)}| |{round(number2)}| |{round(number3)}|")
    print("               --- --- ---")
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
    print(f"|{round(number_1)}| |{round(number_2)}| |{round(number_3)}|")
    print("--- --- ---")

    if round(number_1) == round(winning_array[0]) and round(number_2) == round(winning_array[1]) and round(number_3) == round(winning_array[2]):
        return True
    else:
        return False
def gamble():
    # randomize the random winning chance array
    winning_array = [float(random.randint(0, 9)), float(random.randint(0, 9)), float(random.randint(0, 9))]
    win_lose = print_number(float(random.randint(0, 9)), float(random.randint(0, 9)), float(random.randint(0, 9)), winning_array=winning_array)
    
    if win_lose:
        print("YOU WON!!!")
        print(" ")
    else:
        print("You lost it all")
        print(" ")
def main():
    while True:
        start = input("Type 'spin' to spin: ")
        if start == "spin":
            gamble()
main()