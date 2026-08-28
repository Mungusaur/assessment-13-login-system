# This is the notice saying that I Astle van Dam say this is all my own work
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
    with open(tru_path, "w") as file:
        file.write(dictionary)

def txt_to_dict(txt, dictionary):
    dir_path = Path(__file__).resolve().parent
    near_tru_path = str(dir_path) + "/"
    tru_path = near_tru_path + txt
    with open(tru_path, "r") as file:
        a = file.read()
    b = dict(a)
    dictionary = b
    return dictionary

def __encrypt__(txt):
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
    key = check_key()
    fernet = Fernet(key)
    new_data = fernet.decrypt(txt_content)
    new_data = str(new_data)
    new_data = new_data[3:-1]
    with open(tru_path, "w") as file:
        file.write(new_data)

def encrypt_user(txt, user):
    pass

def decrypt_user(txt, user):
    pass

def verify(username, password):
    __decrypt__("user_info.txt")
    with open("user_info.txt", "r") as file:
        a = file.read()
    __encrypt__("user_info.txt")
    list_of_users = []
    for i in range(len(list(users.keys()))):
        list_of_users.append(users[users[i+1]])
        print(users[users[i+1]])

def __init__():
    while True:
        login_signin = buttonbox(choices=["Login", "Sign in"])
        while login_signin == "Login":
            login_details = multenterbox(msg="Enter your login details:", fields=["Username", "Password"])
            verify(login_details[0], login_details[1])
        while login_signin == "Sign in":
            pass

__init__()
    