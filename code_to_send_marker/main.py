# This is the notice saying that I Astle van Dam say this is all my own work
from cryptography.fernet import Fernet
from pathlib import Path
import subprocess
import sys
import os


def check_key():
    dir_path = Path(__file__).resolve().parent
    a = dir_path + r"\donotopen.key"
    with open(a, "r") as file:
        b = file.read()
    if a == "":
        key = Fernet.generate_key()
        with open(a, "w") as file:
            file.write(key)
    else:
        fernet = Fernet(key)
        return fernet

def dict_to_txt(txt, dictionary):
    with open(txt, "w") as file:
        file.write(dictionary)

def txt_to_dict(txt, dictionary):
    with open(txt, "r") as file:
        a = file.read()
    b = dict(a)
    dictionary = b
    return dictionary

def encrypt(txt):
    with open(txt, "r") as file:
        txt_content = file.read()
    key = check_key
    fernet = Fernet(key)
    #Continue this function
