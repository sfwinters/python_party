user_name = input("What is your name? ")
# print(f"Hello {user_name}!")

# Logic gates, aka if statements, aka flow control

if user_name == "Francis":
    print(f"Hello {user_name}!")
elif user_name == "Roy":
    print(f"Oh hell no, what up {user_name}?")
elif "a" or "b" in user_name.lower():
    print(f"{user_name}, are you for real?")
else:
    print(f"{user_name}!?!? GTFO")

# Comparison operators: and, or, !=

# "if a in user_name" checks to see if the entered value contains the letter a; easy way to iterate through to find something

