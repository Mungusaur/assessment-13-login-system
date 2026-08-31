# This is the notice saying that I Astle van Dam say this is all my own work
# Unfortunately I cannot find out how to fix the bug where the open(file, x) command doesn't work on my computer so I am unable to automate the creation of files.
# When creating a new user please make sure to create a file with the name of user_file[insert number here].txt so that the program will recognise it and open it when,
# it calls for the user file linked to it.
from easygui import *
from cryptography.fernet import Fernet
from pathlib import Path
import subprocess
import sys
import os

users = {
    1:{
        "user_name":"default_1",
        "password":"password_1",
        "user_file":"file_1"
       },
    2:{
        "user_name":"default_2",
        "password":"password_2",
        "user_file":"file_2"
       }

}

def open_in_default_editor(filepath):
    # Ensure the file exists before opening
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return False

    # Windows platform
    if sys.platform == "win32":
        os.startfile(filepath)
        return True
        
    # macOS platform
    elif sys.platform == "darwin":
        subprocess.Popen(["open", filepath])
        return True
        
    # Linux and Unix-like platforms
    else:
        subprocess.Popen(["xdg-open", filepath])
        return True

def check_key():
    dir_path = Path(__file__).resolve().parent
    a = str(dir_path) + r"\donotopen.key"
    with open(a, "r") as file:
        b = file.read()
    if b == "":
        key = Fernet.generate_key()
        key = str(key)
        with open(a, "w") as file:
            file.write(key)
    with open(a, "r") as file:
        key = file.read()
    key = key[2:-1]
    key = key.encode('utf-8')
    return key

def dict_to_txt(txt, dictionary):
    dir_path = Path(__file__).resolve().parent
    near_tru_path = str(dir_path) + "/"
    tru_path = near_tru_path + txt
    dictionary = str(dictionary)
    with open(tru_path, "w") as file:
        file.write(dictionary)

def txt_to_dict(txt, dictionary):
    __decrypt__("user_info.txt")
    dir_path = Path(__file__).resolve().parent
    near_tru_path = str(dir_path) + "/"
    tru_path = near_tru_path + txt
    with open(tru_path, "r") as file:
        a = file.read()
    b = dict(a)
    dictionary = b
    __encrypt__("user_info.txt")
    return dictionary

def __encrypt__(txt):
    # Currently bug fixing.
    dir_path = Path(__file__).resolve().parent
    near_tru_path = str(dir_path) + "/"
    tru_path = near_tru_path + txt
    with open(tru_path, "r") as file:
        txt_content = file.read()
    key = check_key()
    fernet = Fernet(key)
    txt_content = txt_content.encode("utf-8")
    new_data = fernet.encrypt(txt_content)
    new_data = str(new_data)
    new_data = new_data[2:-1]
    with open(tru_path, "w") as file:
        file.write(new_data)
    return "complete"

def __decrypt__(txt):
    dir_path = Path(__file__).resolve().parent
    near_tru_path = str(dir_path) + "/"
    tru_path = near_tru_path + txt
    with open(tru_path, "r") as file:
        txt_content = file.read()
        if txt_content == '':
            return "empty"
    key = check_key()
    fernet = Fernet(key)
    new_data = fernet.decrypt(txt_content)
    new_data = str(new_data)
    new_data = new_data[3:-1]
    with open(tru_path, "w") as file:
        file.write(new_data)
    return "complete"

def verify(username, password):
    __decrypt__("user_info.txt")
    with open("user_info.txt", "r") as file:
        a = file.read()
    __encrypt__("user_info.txt")
    list_of_users = []
    for i in range(len(list(users.keys()))):
        list_of_users.append(users[list(users.keys())[i]])
        print(users[list(users.keys())[i]])
    if username in [user["user_name"] for user in list_of_users]:
        if password == [user["password"] for user in list_of_users if user["user_name"] == username][0]:
            msgbox("Login successful!")
            user_file = [user["user_file"] for user in list_of_users if user["user_name"] == username][0]
            __decrypt__(user_file + ".txt")
            a = open_in_default_editor(user_file + ".txt")
            while a == False:
                make_files()
                a = open_in_default_editor(user_file + ".txt")
            __encrypt__(user_file + ".txt")
        else:
            msgbox("Incorrect password.")
# This is still not complete.

def make_files():
    __decrypt__("user_info.txt")
    users = txt_to_dict("user_info.txt", users)
    for i in range(len(list(users.keys()))):
        user_file = users[list(users.keys())[i]]["user_file"]
        if not os.path.exists(user_file + ".txt"):
            with open(user_file + ".txt", "x") as file:
                file.write("This is the file for " + users[list(users.keys())[i]]["user_name"])
            __encrypt__(user_file + ".txt")
        print("file created")

def __init__():
    make_files()
    __decrypt__("user_info.txt")
    if not os.path.exists("user_info.txt"):
        dict_to_txt("user_info.txt", users)
    else:
        users = txt_to_dict("user_info.txt", users)
    while True:
        login_signin = buttonbox(choices=["Login", "Sign in", "Exit"])
        if login_signin == "Exit":
            break
        while login_signin == "Login":
            login_details = multenterbox(msg="Enter your login details:", fields=["Username", "Password"])
            verify(login_details[0], login_details[1])
        while login_signin == "Sign in":
            new_user_details = multenterbox(msg="Enter your new user details:", fields=["Username", "Password"])
            users[len(users)+1] = {
                "user_name":new_user_details[0],
                "password":new_user_details[1],
                "user_file":"file_" + str(len(users)+1)
            }
            __decrypt__("user_info.txt")
            dict_to_txt("user_info.txt", users)
            __encrypt__("user_info.txt")
            login_signin = buttonbox(choices=["Login", "Sign in", "Exit"])

__init__()
    