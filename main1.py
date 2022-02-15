import random 

# chars= 'abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ123456'

lower = "abcefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
symbol = "{}[]#@_-;"
number = "12345678910"

all = lower + upper + symbol + number 
length = 9
password = "".join(random.sample(all,length))
print("The password generated is :",password)
