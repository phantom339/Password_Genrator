#Eazy Level - Order not randomised:
import random
#lists of letters,symbols and numbers:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

def easy(nr_letters, nr_symbols, nr_numbers):
    password=""
    for n in range(0,nr_letters):
        le=random.choice(letters)
        password+=le
    for n in range(0,nr_symbols):
        sy=random.choice(symbols)
        password+=sy
    for n in range(0,nr_numbers):
        nu=random.choice(numbers)
        password+=nu 
    return password

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def hard(nr_letters, nr_symbols, nr_numbers):
    password_list=[]
    for n in range(0,nr_letters):
        password_list.append(random.choice(letters)) 
    for n in range(0,nr_symbols):
        password_list.append(random.choice(symbols))
    for n in range(0,nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password=""
    for m in password_list:
        password+=m     
    return password