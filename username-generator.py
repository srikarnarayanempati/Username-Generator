import random

def generate_username(first_name, last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    
    base_username = first + last

    number = str(random.randint(1, 9999))
    style = random.choice([
        f"{base_username}_{number}",
        f"{first}_{last}{number}",
        f"{first}{last}_{number}",
        f"{first}_{last}_{number}",
        f"{first}{last}{number}"
    ])

    return style

def main():
    print("=== Username Generator ===")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    for i in range(5):
        username = generate_username(first_name, last_name)
        print(f"> {username}")

if __name__ == "__main__":
    main()
