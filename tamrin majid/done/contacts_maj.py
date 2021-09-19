contacts= []
while 1:
    print("\033c",end='')
    contacts.sort()
    print("1.Add")
    print("2.Search")
    print("3.Edit")
    print("4.Delete")
    print("5.Filter")
    print("6.Print")
    print("7.Exit")
    option = input("Please enter your choice(1-7): ")
#    print("\033c",end='')
    if option=="1":
        print("***ADD***")
        name = input("Name :").lower()
        family = input("Family :").lower()
        phone = input("Phone :")
        contacts.append("{},{},{}".format(family,name,phone))
        print("Saved...")
        input("Press enter to continue")
    elif option=="2":
        print("***SEARCH***")
        name = input("Name :").lower()
        family = input("Family :").lower()
        phone="Not found!"
        for contact in contacts:
            if contact.startswith("{},{},".format(family,name)):
                phone=contact.split(",")[2]
                break
        print("Phone : "+phone)        
        input("Press enter to continue")         
    elif option=="3":
        print("***EDIT***")
        name = input("Name :").lower()
        family = input("Family :").lower()
        phone="Not found!"
        for index in range(len(contacts)):
            if contacts[index].startswith("{},{},".format(family,name)):
                print("Phone : "+contacts[index].split(",")[2])
                phone = input("New phone :")
                contacts[index]="{},{},{}".format(family,name,phone)
                print("Edited...")
                break                
        if phone=="Not found!":
            print("Phone : Not found")        
        input("Press enter to continue") 
    elif option=="4":
        print("***DELETE***")
        name = input("Name :").lower()
        family = input("Family :").lower()
        phone="Not found!"
        for index in range(len(contacts)):
            if contacts[index].startswith("{},{},".format(family,name)):
                print("Phone : "+contacts[index].split(",")[2])
                while phone!="y" and phone!="n":
                    phone=input("Are you sure(y/n):")
                    if phone=="y":
                        contacts.pop(index)
                        print("Deleted...")                                  
                break                
        if phone=="Not found!":
            print("Phone : Not found")        
        input("Press enter to continue")  
    elif option=="5":
        print("***FILTER***")
        filter = input("Text :").lower()
        print("{:<20}{:<20}{}".format("Family","Name","Phone"))
        for contact in contacts:
            if filter in contact:
                splited = contact.split(",")
                print("{:<20}{:<20}{}".format(splited[0],splited[1],splited[2]))
        input("Press enter to continue")  
    elif option=="6":
        print("***PRINT***")
        print("{:<20}{:<20}{}".format("Family","Name","Phone"))
        for contact in contacts:
            splited = contact.split(",")
            print("{:<20}{:<20}{}".format(splited[0],splited[1],splited[2]))
        input("Press enter to continue") 
    elif option=="7":
        break