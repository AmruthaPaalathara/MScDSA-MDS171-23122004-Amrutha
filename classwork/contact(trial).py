# contact -> Name, Email, Phone, City
# {"Name": ___ , "Email": _____, "Phone": ____, "City": ____ }

# [ {"Name": ___ , "Email": _____, "Phone": ____, "City": ____ },
#  {"Name": ___ , "Email": _____, "Phone": ____, "City": ____ },
#   {"Name": ___ , "Email": _____, "Phone": ____, "City": ____ },
#    {"Name": ___ , "Email": _____, "Phone": ____, "City": ____ } ]

# CREATE
# SEARCH
# LIST ALL DETAILS



def clist():

    while True:

        dict={}
        list_d=[]
        dict["Name"]=input("enter the name: ")
        dict["Email"]=input("enter the mail id: ")
        dict["phone_number"]=int(input("enter the phone number: "))
        dict["city"]=input("enter the city: ")
        # print(dict)
        list_d.append(dict)
        print(list_d)    
clist()

print("-"*50)
print("contact mgmt program")
print("-"*50)
print("1. Create the list")
print("2. Search for details")
print("3. Exit the programme")
value=int(input("enter the value: "))


if value == 1:
    clist()
elif value==2:
    ph=int(input("Enter the phone number to search: "))
    if ph in  dict():
        print("phone number exists")
    else:
        print("doesn't exists")
elif value == 3:
    if value ==3:   
        exit()
        print("========E X I T E D========")
    
else:
    print("End the programme")


