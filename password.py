import random
print("Welcome to the PyPassword Generator!")

letters=int(input("How many letters would you like in you password? "))
symbols=int(input("How many symbols would you like in you password? "))
numbers=int(input("How many nummbers would you like in you password? "))

password_list=[]

all_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
all_symbols=["!","@","#","$","%","^","&","*","(",")","_","-","+","=","?","/",">","<",".",",","~","`"]
all_numbers=["1","2","3","4","5","6","7","8","9","0"]

for i in range(0,letters+1):
    password_list.append(random.choice(all_letters))
for i in range(0,symbols+1):
    password_list.append(random.choice(all_symbols))
for i in range(0,numbers+1):
    password_list.append(random.choice(all_numbers))

random.shuffle(password_list)
password=""
for i in password_list:
    password += i
print(f"Here is your password: {password}")
