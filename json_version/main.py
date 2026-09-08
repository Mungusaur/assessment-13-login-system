import json
import easygui
import os
from cryptography.fernet import Fernet
import subprocess
import sys

default_users = {
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
    tru_path = txt
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
    tru_path = txt
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