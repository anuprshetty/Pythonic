users = [
    (0, "Anup", "mypass"), # Same username
    (1, "Ram", "rampass"),
    (2, "Anup", "mypass2"), # Same username
    (3, "Alice", "alicepass")
]

# Dictionary comprehension.
username_mapping = {user[1]: user for user in users}

# Dictionary updated with latest value for key "Anup".
print(username_mapping) # {'Anup': (2, 'Anup', 'mypass2'), 'Ram': (1, 'Ram', 'rampass'), 'Alice': (3, 'Alice', 'alicepass')}

print(username_mapping["Anup"]) # (2, 'Anup', 'mypass2')

# Usage:
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if username_input in username_mapping:
    _, username, password = username_mapping[username_input]
    if username_input == username and password_input == password:
        print("Authentication is successful!")
    else:
        print("Authentication failed!")
else:
    print("Invalid username")
