import requests
import hashlib 

def check_password_pwned(password):
    shai_passwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # convert password to sha1
    first5, tail = shai_passwd[:5], shai_passwd[5:]

    url = f"https://api.pwnedpasswords.com/range/{first5}" # using k-anonymity model to check if password has been pwned
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")
        return False

    
    hashes = (line.split(':') for line in response.text.splitlines()) # splitting the response into hash and count (i don't really know why but it works)
    for h, count in hashes:
        if h == tail:
            print(f"Password has been pwned {count} times! Consider changing it.")
            return True
    print("Password is safe. it has not been pwned yet.")
    return False




