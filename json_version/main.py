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
    if not os.path.exists("donotopen.key"):
        key = Fernet.generate_key()
        with open("donotopen.key", "wb") as file:
            file.write(key)
        if os.path.getsize("donotopen.key") == 0:
            key = Fernet.generate_key()
            with open("donotopen.key", "wb") as file:
                file.write(key)
    else:
        if os.path.getsize("donotopen.key") == 0:
            key = Fernet.generate_key()
            with open("donotopen.key", "wb") as file:
                file.write(key)
        with open("donotopen.key", "rb") as file:
            key = file.read()
    return key

def __encrypt__(txt):
    key = __check_key__()
    fernet = Fernet(key)
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\" + txt
    with open(tru_path, "r") as file:
        txt_content = file.read()
        if txt_content == '':
            return "empty"
    new_data = fernet.encrypt(txt_content.encode())
    new_data = str(new_data)
    new_data = new_data[2:-1]
    with open(tru_path, "w") as file:
        file.write(new_data)
    return "complete"

def __decrypt__(txt):
    key = __check_key__()
    fernet = Fernet(key)
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\" + txt
    with open(tru_path, "r") as file:
        txt_content = file.read()
        if txt_content == '':
            return "empty"
    new_data = fernet.decrypt(txt_content.encode())
    new_data = str(new_data)
    new_data = new_data[2:-1]
    with open(tru_path, "w") as file:
        file.write(new_data)
    return "complete"

def create_account():
    username = easygui.enterbox("Enter a username:")
    if username == None:
        easygui.msgbox("Username cannot be empty.")
        return
    password = easygui.passwordbox("Enter a password:")
    if password == None:
        easygui.msgbox("Password cannot be empty.")
        return
    if verify(username, password) == True:
        easygui.msgbox("Username already exists. Please choose a different username.")
        return
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\user_info.json"
    with open(tru_path, "r", encoding="utf-8") as file:
        users = json.load(file)["users"]
        users[len(users) + 1] = {
            "username": username,
            "password": password
        }
    json_data = {"users": users}
    with open(tru_path, "w", encoding="utf-8") as file:
        json.dump(json_data, file)
    try:
        with open(f"{username}.txt", "x") as file:
            file.write("")
    except FileExistsError:
        with open(f"{username}.txt", "w") as file:
            file.write("")

        try:
            __encrypt__(f"{username}.txt")
        except:
            easygui.msgbox("Failed to encrypt user file. Your data may not be secure. Please run the program again.")
        

def verify(username, password):
    dir_path = Path(__file__).resolve().parent
    tru_path = str(dir_path) + "\\user_info.json"
    try:
        __decrypt__(tru_path)
    except:
        pass
    with open(tru_path, "r", encoding="utf-8") as file:
        users = json.load(file)["users"]
    try:
        __encrypt__(tru_path)
    except:
        pass
    if username in [user["username"] for user in users.values()]:
        if password == [user["password"] for user in users.values() if user["username"] == username][0]:
            return True
    return False

def open_in_default_editor(file_path):
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(file_path)
        elif os.name == 'posix':  # For macOS and Linux
            subprocess.call(('open', file_path))
        return True
    except Exception as e:
        easygui.msgbox(f"Failed to open the file: {e}")
        return False

def __init__():

    while True:
        choice = easygui.buttonbox("Welcome to the login system!", choices=["Login", "Create Account", "Exit"])
        if choice == "Login":
            username = easygui.enterbox("Enter your username:")
            if username == None:
                easygui.msgbox("Username cannot be empty.")
                continue
            password = easygui.passwordbox("Enter your password:")
            if password == None:
                easygui.msgbox("Password cannot be empty.")
                continue
            if verify(username, password):
                easygui.msgbox("You have successfully logged in!")
                try:
                    __decrypt__(f"{username}.txt")
                except:
                    pass
                open_in_default_editor(f"{username}.txt")
                try:
                    __encrypt__(f"{username}.txt")
                except:
                    pass
            else:
                easygui.msgbox("Invalid username or password.")
        elif choice == "Create Account":
            create_account()
        elif choice == "Exit":
            sys.exit()

__init__()
