import os
import getpass
import pathlib
import json

def func1():
    os.system("cls")
    print("user_name is -> ", getpass.getuser())

    #dir = os.path.dirname(os.path.abspath(__file__))
    #full_path = os.path.join(dir, *path_components)

    src_path_components = ("x1", "y1", "sourceData")
    dest_path_components = ("x2", "y2", "json")
    log_path_components = ("x3", "y3", "logs")

    home_directory = os.path.expanduser("~")
    full_path = os.path.join(home_directory, *src_path_components)

    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print("sourceData folder created")

    if os.path.exists(full_path):
        print("folder found -> ", full_path)

   
func1()
print(".........done...........")
name = "system"
hostname = "localhost"

html1 = f"'Hello': {name}, 'Hostname': {hostname}"
print(html1)

html2 = f"<h3>Hello {name} ! </h3> <b> Hostname:</b> {hostname}"
print(html2.format(name=name, hostname=hostname))