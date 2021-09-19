contacts=[]
print("Wellcome to contacts BY MASOOUD69")
#functions
#show menu
def pr_option():
    print("\033c",end="")
    print("1.ADD")
    print("2.SEARCH")
    print("3.EDIT")
    print("4.DELETE")
    print("5.FILTER")
    print("6.PRINT")
    print("7.EXIT")
#get family name and phone
def add_contact(family,name,phone):
    contacts.append("{},{},{}".format(family,name,phone))
    return contacts
# None Wise
def pr_save():
    print("SAVED...")
def pr_continue():
    input("Please Enter to continue")
#search index of list according family and name
def srch_index(family,name):
    for index in range(len(contacts)):
        if contacts[index].startswith("{},{},".format(family,name)):
            return index
    return None
#search phone of list according family and name
def srch_phone(family,name,phone="not found"):
    for contact in contacts:
        if contact.startswith("{},{},".format(family, name)):
            phone=contact.split(",")[2]
    return phone
#delete contact according family and name
def del_contact(family,name):
    phone=srch_index(family,name)
    if phone==None:
        print("Phone: NOT found!!!")
    else:
        print("Phone: " + srch_phone(family,name))
        sure=""
        while sure!="y" and sure!="n":
            sure=input("Are you sure(y/n)? ")
            if sure=="y":
                contacts.pop(phone)
                pr_save()
                return contacts
#add newphone according on family and name
def add_edit(family,name,newphone):
    contacts[int(srch_index(family,name))]=("{},{},{}".format(family,name,newphone))
    return contacts
def edit_contact(family,name):
    phone=srch_index(family,name)
    if phone==None:
        print("Phone: NOT found!!!")
    else:
        print("Phone: " + srch_phone(family,name))
        newphone=input("New Phone: ")
        add_edit(family,name,newphone)
        pr_save()
##search family,name and phone of list according txt
def srch_txt(txt):
    print("{:<20}{:<20}{}".format("FAMILY","NAME","PHONE"))
    for index in contacts:
        if txt in index:
            l=index.split(",")
            print("{:<20}{:<20}{}".format(l[0],l[1],l[2]))
    pr_continue()
#begining program
while 1:
    pr_option()
    option=input("Please enter the Option(1-7): ")
    if option=="1":
        print("***ADD***")
        family=input("Family: ").lower()
        name=input("Name: ").lower()
        phone=input("Phone: ")
        add_contact(family,name,phone)
        pr_save()
        pr_continue()
    elif option=="2":
        print("***SEARCH***")
        family=input("Family: ").lower()
        name=input("Name: ").lower()
        print(srch_phone(family,name))
        pr_continue()
    elif option=="3":
        print("***EDIT***")
        family=input("Family: ").lower()
        name=input("Name: ").lower()
        edit_contact(family,name)
        pr_continue()
    elif option=="4":
        print("***DELETE***")
        family=input("Family: ").lower()
        name=input("Name: ").lower()
        del_contact(family,name)
        pr_continue()
    elif option=="5":
        print("***FILTER***")
        txt=input("txt: ").lower()
        srch_txt(txt)
    elif option=="6":
        print("***PRINT ALL***")
        srch_txt("")
    elif option=="7":
        print("***EXIT***")
        print("THANKS FOR YOUR CONCIDERATION")
        pr_continue()
        break