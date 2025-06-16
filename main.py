# python3 main.py
import hashlib, secrets, os

HASH_FILE = "hashes.txt"

def add(): 

    password = input("Enter password to store: ")
    salt = secrets.token_hex(16)
    hashed_pass = hashlib.sha256((salt + password).encode()).hexdigest()
    with open(HASH_FILE, "a") as f:
        f.write(f"{salt}, {hashed_pass}\n")
    print("Password hash has been stored successfully.\n")


def verify():

    password = input("Enter password to verify: \n")

    print("1. Input salt to verify")
    print("2. Fetch from stored file")
    print("3. I changed my mind, return to main menu\n")
    choice = input("Choose: ").strip()
    if choice == "1":
        salt = input("Enter salt to verify: \n")
        test_hash = hashlib.sha256((salt + password).encode()).hexdigest()
        # Search
        found = False
        with open (HASH_FILE, "r") as f:
            for line in f:
                saved_salt, saved_hash = line.strip().split(", ")
                if salt == saved_salt and secrets.compare_digest(test_hash, saved_hash):
                    print("Password matches with stored data.\n")
                    found = True
                    break
        if not found:
            print("No match found for given salt + password combination.\n")
    elif choice == "2":
        # Search with stored salt
        found = False
        with open (HASH_FILE, "r") as f:
            for line in f:
                saved_salt, saved_hash = line.strip().split(", ")
                test_hash = hashlib.sha256((saved_salt + password).encode()).hexdigest()
                if secrets.compare_digest(test_hash, saved_hash):
                    print(f"Password matches with stored data. Salt used was: {saved_salt}\n")
                    found = True
                    break
        if not found:
            print("No match found for given password. \n")
    elif choice == "3":
        print("\n")
    else:
        print("Invalid choice. Returning to main menu. \n")

def main():

    if not os.path.exists(HASH_FILE):
        with open(HASH_FILE, "w") as f:
            pass

    while True:
        print("===== Password Hash Checker =====\n")
        print("1. Add New Password")
        print("2. Verify Password")
        print("3. Quit\n")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add()
        elif choice == "2":
            verify()
        elif choice == "3":
            print("Bye Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()