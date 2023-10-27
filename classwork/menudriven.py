nameList = []

def showMenu():
    print("-"*30)
    print("Name Mgmt. Prgm")
    print("-"*30)
    print("1. Enter a name")
    print("2. Search a name")
    print("3. List names")
    print("4. Exit")
    print("-"*30)

def addName(name):
    name = name.strip().upper()
    nameList.append(name)


def printNames():
    print(nameList)

def searchName(name):
    name = name.strip().upper()
    if name in nameList:
        print("Name exists..!")
    else:
        print("Name doesnot exist..!")

while True:

    showMenu()

    val = input("Enter a number : ").strip()
    
    if val == "1":
        n = input("Enter a Name : ")
        addName(n)
    elif val == "2":
        n = input("Enter the name that have to be searched : ")
        searchName(n)
    elif val == "3":
        printNames()
    elif val == "4":
        exit()
    else:
        print("Invalid Choice !")
