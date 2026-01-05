# here we check the strength of the password
import math
import string
from pwned_check import check_password_pwned
import time

def strengh_check(password): # function to check password strength
    poolsize = 0
    if any (char in string.ascii_lowercase for char in password) : poolsize += 26
    if any (char in string.ascii_uppercase for char in password) : poolsize += 26
    if any (char in string.digits for char in password) : poolsize += 10
    if any (char in string.punctuation for char in password) : poolsize += 32

    if poolsize == 0:
        return 0  # to avoid log2(0) error
    
    entropy = math.log2(poolsize) * len(password) # some formula to calculate entropy (idk how it works really)
    return round(entropy, 2)

# Get user input
password = input("Enter your password: ")
score = strengh_check(password)


# giving output
print("-" * 40)
print(f"Password Strength Score: {score}")
time.sleep(1)
# giving feedback based on score
if score < 37:
    print("Very Weak Password")
elif score < 60:
    print("Weak Password")
elif score < 75:
    print("Reasonable Password")
elif score < 90:
    print("Strong Password")
else:
    print("Very Strong Password") 

time.sleep(1)
print ("checking if your password has been pwned...")
time.sleep(2)  # adding a small delay for better user experience
check_password_pwned(password)
  
print("-" * 40)


