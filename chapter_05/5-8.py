usernames = ["admin", "bob", "george", "rob", "chris"]
for username in usernames:
    if "admin" in username:
        print(f"hello " + username +
              ", would you like to see a status report?")
    else:
        print(f"hello " + username + ", thank you for logging in again")
