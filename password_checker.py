test = "manuel"
first_char = test[0]
print(first_char.isupper())

# islower()

print(test.find("a"))
#return the index if it finds it 
#returns -1 if it cant find it 

#step 1
#prompt the user to enter their password
#check the following:
# - if the password contains the letter z
# - if the password ends with an !
# - if the password begins with an uppercase letter
#if yes to all three, print accept
#if any of these are not true, print reject

password = input("please make a password ")
password = password.strip()
symbols = [" @ "," # "," $ "," % "," ^ "," & ", " * ", " ( ", " ) "]
if "z" and str(symbols) in password and password[-1] == "!" and password[0].isupper():
    print("accept")
else:
    print("please try again ")

