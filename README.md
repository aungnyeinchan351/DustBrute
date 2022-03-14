# DustBrute
Dust BRUTE is a Facebook bruteforce attack tool. It was created by Zin Yaw from Dust. 
You can use your own wordlist file for bruteforce attack.

# Installation on Termux
To install this script in termux, type the following commands
```
>>pkg install git
>>pkg install python
>>git clone https://github.com/aungnyeinchan351/DustBrute
>>pip3 install requests bs4
>>pip3 install pyfiglet
>>pip install mechanize
>>cd DustBrute
>>python3 dustbrute.py
```

## Installation on ubuntu linux
```
sudo apt install python
sudo apt install git
git clone https://github.com/aungnyeinchan351/DustBrute
pip3 install requests bs4
pip3 install mechanize
pip3 install pyfiglet
cd DustBrute
python3 dustbrute.py
```
You will see like this. Enter username of account that you wanna hack
![Capture 1](https://github.com/aungnyeinchan351/DustBrute/blob/master/IMG_20200828_115844.jpg)

After filling username of Target, hit enter. And you will see like this.
![Capture 2](https://github.com/aungnyeinchan351/DustBrute/blob/master/IMG_20200828_100833.jpg)

This is asking you that do you want to use the wordlist in the script.
If you want to use type "y".

If you don't wanna use the wordlist, type"n". But, if you type "n" 
You must input your own wordlist.

If your wordlist is in the same folder of script, type "filename.txt" eg(pass.txt)

```
Do you want to use built in wordlist.(y/n)n
Enter your wordlist: pass.txt
```
If your wordlist is in different folder, enter file path.eg(data/passwords/pass.txt)

```
Do you want to use built in wordlist.(y/n)n
Enter your wordlist: data/passwords/pass.txt
```

## DUST GEN wordlist creator

You can create you wordlist with possible passwords using wordlist_creator.py script.
This script is built in DUST BRUTE. You can use it by typing..
```
>>python3 wordlist_creator.py
```
You can type passwords that you think possible again and again.
If you want to your list, type "0" and hit enter.
Then, you can call your password file from dustbrute.py by using its name.
### Example screenshot

![Capture 1](https://github.com/aungnyeinchan351/DustBrute/blob/master/IMG_20200829_103603.jpg)


Follow me on [GitHub](https://github.com/aungnyeinchan351)
Follow me on [Facebook](https://facebook.com/zinyaw3063)
