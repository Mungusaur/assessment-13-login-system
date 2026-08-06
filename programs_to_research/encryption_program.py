from cryptography.fernet import Fernet

# Generate a secure random key
key = Fernet.generate_key()

# Save the key to a file safely
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# 1. Load the previously saved key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

# 2. Initialize the Fernet class with your key
fernet = Fernet(key)

# 3. Read the original data from your target file
with open('data.txt', 'rb') as file:
    original_data = file.read()

# 4. Encrypt the data
encrypted_data = fernet.encrypt(original_data)

# 5. Write the encrypted data back to the file (or a new file)
with open('data.txt', 'wb') as file:
    file.write(encrypted_data)

print("File successfully encrypted.")