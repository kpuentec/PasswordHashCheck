# PasswordHashCheck

Password Hash Check is a simple Python tool designed to securely store and verify passwords using salted SHA-256 hashing. It allows users to add passwords with randomly generated salts and later verify passwords either by providing a salt or by searching through stored password hashes. This project focuses on fundamental password hashing concepts, secure comparison, and file-based storage.

Features:

* Secure password storage with random salts, SHA-256 hashing of salt + password for strong hashing.

* Verification options:
    * Verify password with user-provided salt.
    * Verify password by searching stored hashes with saved salts.

* Secure hash comparisons using secrets.compare_digest to prevent timing attacks.

* Simple text file-based storage (hashes.txt) for password salts and hashes.

Requirements:

Install Python3 onto your system(If you don't have it already).

Install:

1. Clone repository:

         git clone https://github.com/kpuentec/PasswordHashCheck.git

2. Navigate to the project directory: cd PassHashCheck

Run:

* python main.py for to start the password hash checker.

You will be presented with a menu:

1. Add New Password — Generates salt, hashes password, and stores them.

2. Verify Password — Verify a password using either a known salt or by searching stored hashes.

3. Quit — Exit the program.


Structure:

* main.py — Main script handling user interaction, adding, and verifying passwords.
  
* .gitignore — Specifies files and folders to be ignored by Git.
  
* LICENSE : Project license info

* README.md: This file

Output:

* hashes.txt — Text file storing salts and hashed passwords (created automatically). Edit the file name by changing the variable HASH_FILE at the top of main.py

**Notes:**

This project uses a simple file-based system for demonstration purposes and is not recommended for production use.

The program securely compares hashes to prevent timing attacks but does not handle other security considerations such as brute force protection or encryption of the storage file.

Changes to the code and other features are susceptible in the future

2025
