import hashlib
import requests

def hash_password(password_):
    sha1_hash = hashlib.sha1(password_.encode("utf-8")).hexdigest().upper()
    return sha1_hash
def split_hash(sha1_hash):
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    return prefix, suffix
def check_pwned_api(prefix):
    url = "https://api.pwnedpasswords.com/range/" + prefix
    response = requests.get(url)
    return response.text
print()
password = input("Enter password:")
full_hash = hash_password(password)
prefix, suffix = split_hash(full_hash)
print()
print("prefix (sent to API):", prefix)
print("suffix (kept local):", suffix)

response = check_pwned_api(prefix)
print()
print(response)