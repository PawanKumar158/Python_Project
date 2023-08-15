# importing th module 
import random 

# Lower case alphabate
lower = "abcdefghijklmnopqrstuvwxyz"
# Upper case alphabate
upper = "ABCDEFGHIJKLMNOPWRSTUVWXYZ"
# Numbers adding
number = "0123456789"
# Symbols adding
symbols = "+-/*#$@%^&?~"

#mixing  all Lower, Uppar, Number, and Symbols
all = lower + upper + number +symbols

# Passowrd Length
length = 8

# Password Randomaly arrange fix of length
password ="".join(random.sample(all,length)) 

# Print password
print(password)