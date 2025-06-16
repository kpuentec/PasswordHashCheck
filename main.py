# python main.py
import hashlib, secrets

def hash(): 

    password = input("Enter password to store: ")
    salt = secrets.token_hex(16)
    hashed_pass = hashlib.sha256((salt + password).encode()).hexdigest()
    # store in txt


def verify():

    password = input("Enter password to verify: ")

    print("1. Input salt to verify")
    print("2. Fetch from stored file")
    while True:
        choice = input("Choose: ")
        if choice == "1":
            salt = input("Enter salt to verify: ")
        elif choice == "2":
            # Need to write logic salt = 
            print("Success")
        else:
            print("Invalid choice. Try again.\n")

def main():

    while True:
        print("=== Password Hash Checker ===")
        print("1. Add New Password")
        print("2. Verify Password")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            hash()
        elif choice == "2":
            verify()
        elif choice == "3":
            print("Bye Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()