# Makes Python recognize json files.
import json
# An intuitive GUI library for Python.
import easygui
# Allows program to read the oprerating system of the user and run some system commands.
import os
# Encrypting module. Keeps user data private.
from cryptography.fernet import Fernet
# Allows program to run system commands on a wider base of devices. Used to open user's txt tile on a linux and Posix environment.
import subprocess
# Allows for alternative loop breaking methods. Used to exit the program.
import sys
# Allows program to find the directory of current file and uses it to find user files.
from pathlib import Path

# This data is added to user_info.json if it doesn't exist. It is used to create default users for testing purposes.
DEFAULT_USERS = {
    1: {
        "username": "default_1",
        "password": "password_1",
        "user_file": "default_1.txt"
    },
    2: {
        "username": "default_2",
        "password": "password_2",
        "user_file": "default_2.txt"
    }
}

def __check_key__():
    # Function checks if the encryption key exists and creates it if it doesn't. Returns the encryption key.
    try:
        __decrypt__("user_info.json")
    except:
        pass
    # Attempts to decrypt the user_info.json file. If it fails, it means that the file is already decrypted or the key is missing.
    if not os.path.exists("donotopen.key"):
        key = Fernet.generate_key()
        with open("donotopen.key", "wb") as file:
            file.write(key)
        if os.path.getsize("donotopen.key") == 0:
            key = Fernet.generate_key()
            with open("donotopen.key", "wb") as file:
                file.write(key)
    # Uses os module to check if the encryption file exists. If not then it creates the file and generates a new key.
    else:
        if os.path.getsize("donotopen.key") == 0:
            key = Fernet.generate_key()
            with open("donotopen.key", "wb") as file:
                file.write(key)
        with open("donotopen.key", "rb") as file:
            key = file.read()
    # Uses os module to check if the key file is empty. If it is then it generates a new key and writes it to the file. If not then it reads the key from the file.
    try:
        __encrypt__("user_info.json")
    except:
        pass
    # Attempts to encrypt the user_info.json file. If it fails, it means that the file is already encrypted or the key is missing.
    return key

def __encrypt__(__file__):
    # Function uses the Fernet module to encrypt the designated file.
    key = __check_key__()
    # Calls the __check_key__ function to get the encryption key.
    fernet = Fernet(key)
    # Initializes the Fernet module with the encryption key.
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\" + __file__
    # Gets the full path of the file to be encrypted.
    with open(tru_path, "r") as file:
        txt_content = file.read()
        if txt_content == '':
            return "empty"
    # Returns "empty" if the file is empty to remove the error that occurs when trying to encrypt an empty file.
    new_data = fernet.encrypt(txt_content.encode('utf-8'))
    # Makes sure that the data is encoded in UTF-8 before encrypting it to avoid errors with special characters or conversion artifacts.
    new_data = str(new_data)
    new_data = new_data[2:-1]
    # Converts the encrypted data to a string and removes the b'' prefix and suffix that is added when converting bytes to string.
    with open(tru_path, "w") as file:
        file.write(new_data)
    # Writes the encrypted data back to the file.
    return "complete"

def __decrypt__(__file__):
    # Function uses the Fernet module to decrypt the designated file.
    key = __check_key__()
    # Calls the __check_key__ function to get the encryption key.
    fernet = Fernet(key)
    # Initializes the Fernet module with the encryption key.
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\" + __file__
    # Gets the full path of the file to be decrypted.
    with open(tru_path, "r") as file:
        txt_content = file.read()
        if txt_content == '':
            return "empty"
    # Returns "empty" if the file is empty to remove the error that occurs when trying to decrypt an empty file.
    new_data = fernet.decrypt(txt_content.encode('utf-8'))
    # Makes sure that the data is encoded in UTF-8 before decrypting it to avoid errors with special characters or conversion artifacts.
    new_data = str(new_data)
    new_data = new_data[2:-1]
    # Converts the decrypted data to a string and removes the b'' prefix and suffix that is added when converting bytes to string.
    with open(tru_path, "w") as file:
        file.write(new_data)
    # Writes the decrypted data back to the file.
    return "complete"

def create_account():
    # Function creates a new user account and file for the user and adds the user to the user_info.json file.
    username = easygui.enterbox(msg="Enter a username:", title="Create Account")
    if username == None:
        easygui.msgbox(msg="Username cannot be empty.", title="Error")
        return
    # Forces user to enter a username to avoid having null fields in the user_info.json file.
    password = easygui.passwordbox(msg="Enter a password:", title="Create Account")
    if password == None:
        easygui.msgbox(msg="Password cannot be empty.", title="Error")
        return
    # Forces user to enter a password to avoid having null fields in the user_info.json file.
    if verify(username, password) == True:
        easygui.msgbox(msg="Username already exists. Please choose a different username.", title="Error")
        return
    # Forces user to choose a different username if the username already exists in the user_info.json file to prevent another user from being able to access another's account.
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\user_info.json"
    # Gets the full path of the user_info.json file.
    with open(tru_path, "r", encoding="utf-8") as file:
        users = json.load(file)["users"]
        users[len(users) + 1] = {
            "username": username,
            "password": password
        }
    # Adds the new user info into the dictionary being used by the program.
    json_data = {"users": users}
    # Adds the "users" key back into the dictionary to solve the deletion of the "users" key when the user_info.json file is read and written to.
    with open(tru_path, "w", encoding="utf-8") as file:
        json.dump(json_data, file)
    # Writes the updated dictionary back to the user_info.json file.
    try:
        with open(f"{username}.txt", "x") as file:
            file.write("")
    except FileExistsError:
        with open(f"{username}.txt", "w") as file:
            file.write("")
    # Attempts to create a new file for the user. If the file already exists, it will overwrite the existing file with an empty file as a security measure to prevent another user from accessing the file.
        try:
            __encrypt__(f"{username}.txt")
        except:
            easygui.msgbox(msg="Failed to encrypt user file. Your data may not be secure. Please run the program again.", title="Error")
        

def verify(username, password):
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\user_info.json"
    # Gets the full path of the user_info.json file.
    try:
        __decrypt__(tru_path)
    except:
        pass
    with open(tru_path, "r", encoding="utf-8") as file:
        users = json.load(file)["users"]
    # Reads the user_info.json file and loads the data into a dictionary.
    try:
        __encrypt__(tru_path)
    except:
        pass
    if username in [user["username"] for user in users.values()]:
        if password == [user["password"] for user in users.values() if user["username"] == username][0]:
            return True
    return False
    # Returns True if the username and password match an existing user in the user_info.json file. Returns False if they do not match.

def open_in_default_editor(file_path):
    # Function reads the operating system of the user and opens the designated file in the default text editor for that operating system.
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(file_path).wait()
        elif os.name == 'posix':  # For macOS and Linux
            subprocess.call(('open', file_path)).wait()
        return True
    except Exception as e:
        easygui.msgbox(msg=f"Failed to open the file: {e}", title="Error")
        return False
    # Returns True if the file was opened successfully. Returns False if there was an error opening the file.

def __init__():
    if not os.path.exists("user_info.json"):
        with open("user_info.json", "w") as file:
            json.dump(DEFAULT_USERS, file)
        try:
            with open("default_1.txt", "x") as file:
                file.write("This is the default user 1 file.")
            with open("default_2.txt", "x") as file:
                file.write("This is the default user 2 file.")
        except FileExistsError:
            pass
    # Checks for the existence of the user_info.json file. If it doesn't exist, it creates it and assumes that the default files don't exist either.
    # However it does have a try/except block to catch the FileExistsError in case the default files do exist but the user_info.json file doesn't.
    while True:
        choice = easygui.buttonbox(msg="Welcome to the login system!", title="Login System", choices=["Login", "Create Account", "Exit"])
        if choice == "Login":
            username = easygui.enterbox(msg="Enter your username:", title="Login")
            if username == None:
                easygui.msgbox(msg="Username cannot be empty.", title="Error")
                continue
            password = easygui.passwordbox(msg="Enter your password:", title="Login")
            if password == None:
                easygui.msgbox(msg="Password cannot be empty.", title="Error")
                continue
        # This section asks for the user's username and password but makes them retry if they enter nothing in a field.
            if verify(username, password):
                easygui.msgbox(msg="You have successfully logged in!", title="Login Successful")
                try:
                    __decrypt__(f"{username}.txt")
                except:
                    pass
                open_in_default_editor(f"{username}.txt")
                try:
                    __encrypt__(f"{username}.txt")
                except:
                    pass
        # This section checks if the username and password match an existing user in the user_info.json file.
        # If they do, it decrypts the user's file, opens it in the default text editor, and then encrypts it again after the user is done.
            else:
                easygui.msgbox(msg="Invalid username or password.", title="Error")
        elif choice == "Create Account":
            create_account()
        elif choice == "Exit":
            sys.exit()
        # Calls the sys module to close the program.

__init__()
