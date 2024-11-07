import os

list = []

def print_todo():
    for i in range(len(list)):
        prefix = "Title: "
        print("------------------------------------------------------------------------------------------------------------------------------\n")
        for j in range(len(list[i])):
            if j == 0:
                print(prefix + list[i][j].upper() + "\n")
            else:
                print(prefix + list[i][j] + "\n")
            prefix = "Description: "
    print("------------------------------------------------------------------------------------------------------------------------------\n")
    input()

def add_todo(title, desc):
    list.append([title, desc])

def remove_todo():
    print("Which one would you like to remove")
    for i in range(len(list)):
        print((i + 1), ": ", list[i][0])
    removeNum = int(input("1 - "+ str(i + 1) + ":\n"))
    os.system('cls')
    removeName = list[removeNum-1][0]
    list.pop(removeNum - 1)
    print("Removed", removeName)

def edit_todo():
    print("Which one would you like to change")
    for i in range(len(list)):
        print((i + 1), ": ", list[i][0])
    changeNum = int(input("1 - "+ str(i + 1) + ":\n")) - 1
    os.system('cls')
    changeItem = int(input("What would you like to change\n1: Title: " + list[changeNum][0] + "\n2: Description: " + list[changeNum][1] + "\n")) - 1
    os.system('cls')
    print(list[changeNum][changeItem])
    list[changeNum][changeItem] = input("Type in your changes:\n")

def save_todo():
    match input("Create a new file or overwrite an old one:\n"):
        case "new":
            input("saved")
        case "old":
            file = input("file location:\n")
        case _:
            input("invalid input\n")

def load_todo():
    file = input("file location:\n")

while True:
    os.system('cls')
    match input("Would you like to add, remove, edit a todo, print, save, or load the list: \n"):
        case "add":
            os.system('cls')
            add_todo(input("What is the title: \n"), input("What is the description: \n"))
        case "remove": 
            os.system('cls')
            remove_todo()
        case "edit":
            os.system('cls')
            edit_todo()
        case "print":
            os.system('cls')
            print_todo()
        case "save":
            os.system('cls')
            save_todo()
        case "load":
            os.system('cls')
            load_todo()
        case _:
            os.system('cls')
            input("Invalid Input")