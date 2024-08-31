import random
print("\t\t\tLET'S GENERATE RANDOM PASSWORD")

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#&!?"
#asking user for the length of password
length=int(input("Enter desired length of the password : "))
#initializing an empty list to password
password= [ ]
for x in range(length):
    password.append(random.choice(letters))
#joining password to form a word
newPassword= " ".join(password)
#required password
print("Password generated is",newPassword)