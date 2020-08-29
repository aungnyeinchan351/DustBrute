# DustBrute
Dust BRUTE is a Facebook bruteforce attack tool developed in Aug 26, 2020. It was created by Zin Yaw from Dust. 
You can use your own wordlist file for bruteforce attack.

DUST BRUTE ဆိုတာ ၂၀၂၀ခုနှစ်၊ဩဂုတ်လ၊၂၆ရနေ့ကဖန်တီးလိုက်တဲ့ Facebook Bruteforce tool တသ်ခုဖြစ်ပါတယ်။
Bruteforce attack အတွက်သင်ဟာသင့်ရဲ့ကိုယ်ပိုင် passwords file(wordlist)ကိုအသုံးပြုနိုင်ပါတယ်။

# Installation on Termux
To install this script in termux, type the following commands
ဒီဟာကို Termux မှာ install လုပ်ဖို့ဒီcommand များကိုရိုက်ထည့်ပါ။
```
>>pkg install git
>>pkg install python
>>git clone https://github.com/aungnyeinchan351/DustBrute
>>pip3 install requests bs4
>>pip install mechanize
>>cd DustBrute
>>python3 dustbrute.py
```
You will see like this. Enter username of account that you wanna hack

သင်ဒီလိုမြင်ရလိမ့်မယ်။သင် hack ချင်တဲ့ account username ထည့်ပါ။
![Capture 1](https://github.com/aungnyeinchan351/DustBrute/blob/master/IMG_20200828_115844.jpg)

After filling username of Target, hit enter. And you will see like this.

Target ရဲ့ username ဖြည့်ပြီးနောက် ပြထားတဲ့ပုံအတိုင်းမြင်ရပါမယ်။
![Capture 2](https://github.com/aungnyeinchan351/DustBrute/blob/master/IMG_20200828_100833.jpg)

This is asking you that do you want to use the wordlist in the script.
If you want to use type "y".

ဒါကတော့သင့်ကို tool နဲ့အတူပါလာတဲ့ wordlist ကိုသုံးချင်လားမေးတာပါ။သုံးမယ်ဆိုရင် "y" လို့ရိုက်ပေးပါ။

If you don't wanna use the wordlist, type"n". But, if you type "n" 
You must input your own wordlist.

သင်ကအသင့်ပါလာတဲ့ wordlist ကိုမသုံးချင်ရင်‌‌တော့ "n" လို့ရိုက်ပါ။
ဒါပေမယ့်သင်ဟာ wordlist တစ်ခုကိုတော့ထည့်ပေးရပါမယ်။

If your wordlist is in the same folder of script, type "filename.txt" eg(pass.txt)

သင့်ရဲ့ wordlist က script နဲ့ folder တစ်ခုထဲမှာရှိမယ်ဆိုရင် filename.txt ပုံစံနဲ့ရိုက်ထည့်ပါ။(ဥပမာ-pass.txt)

```
Do you want to use built in wordlist.(y/n)n
Enter your wordlist: pass.txt
```
If your wordlist is in different folder, enter file path.eg(data/passwords/pass.txt)

Wordlist ကတခြား folder ထဲမှာဆိုရင် file လမ်းကြောင်းနဲ့ထည့်ပေးပါ။ ဥပမာ(data/passwords/pass.txt)
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
