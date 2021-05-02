
# Age calculator
birth_year = int(input("\n_______\n\nWhat is your birth year?\n"))
current_year = int(input("\nWhat is the current year?\n"))
user_age = current_year - birth_year
# Here we check if they are a minor
if user_age >= 18:
    age_difference = user_age - 18
    print(f"\nLooks like you're an adult. It has been {age_difference} years since you turned 18!")
elif user_age < 18:
    age_difference = 18 - user_age
    print(f"\nUh oh! You're still a minor. You will turn 18 in {age_difference} years!")
else:
    print("\nError: Invalid age")
print("\n______\n")
# user_name = input("\n\nWhat is your name?\n")
# user_age = input("\n\nWhat is your age?\n")
# user_id = input("\n\nWhat is your ID?\n")
# print(f"\nHello {user_name}! Your age is {user_age} and your ID is {user_id}\n")
