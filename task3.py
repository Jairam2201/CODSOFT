import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter desired length of the password: "))
        if length < 3:
            print("Password length should be at least 3.")
            return
        password = generate_password(length)
        print("Generated password:\n", password)
    except ValueError:
        print("please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
