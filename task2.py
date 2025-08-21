username = input("Enter username please: ")
password = input("Enter password please: ")

user = username.lower()           
user = user.replace(" ", "_") 
password_length = len(password)

print(f" Username: {user}")
print(f"Password Length: {password_length}")
print("Password length >= 8:", password_length >= 8)
print("Username is 'admin':", user == "admin")
print("Password is '1234':", password == "1234")
print("Default Account (admin + 1234):", user == "admin" and password == "1234")
print(f"\n Welcome , {user} Glad to see you 🤍")
