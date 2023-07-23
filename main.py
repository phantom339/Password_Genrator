#Password Generator Project
import os
from ea_ha import easy
from ea_ha import hard
from art import logo

should_continue=True
while should_continue:
    print(logo)
    print("Welcome to the PyPassword Generator!")
    eaha=input("Do You want a A-Strong password or an B-easy password: ").lower()
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    if eaha=="b":
      print(easy(nr_letters, nr_symbols, nr_numbers))
      again=input("Would you like to try again: Y/N ").lower()
    else:
      print(hard(nr_letters, nr_symbols, nr_numbers)) 
      again=input("Would you like to try again: Y/N ").lower() 

    if again=="n":
       should_continue=False
       print("Good Bye!!!")
    else:
       os.system("clear")
          
         

  


    
      












