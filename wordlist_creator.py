import os
import pyfiglet
os.system("clear")
print(pyfiglet.figlet_format("Dust Gen"))
print("Dust Gen wordlist creator!")
print("Created by Zin Yaw")
print("(File name must be in .txt extension)")
file_name = input("Enter wordlist file name: ")
fhand = open(file_name,"w")
passwords = input("Enter password or (0) for end: ")
while passwords != "0":
	fhand.write(passwords)
	fhand.write("\n")
	passwords = input("Enter password or(0) for end: ")
fhand.close()
print("Your wordlist is successfully created. You can call it as ",file_name)