contacts=dict()
print("OPTIONS:")
print("Add=    1")
print("Search= 2")
print("Edit=   3")
print("Delete= 4")
print("Filter= 5")
print("Print=  6")
print("Exit=   7")
while True:
    user_input=input("lotfan option ra vared konid :\n")
    num_con=0
    if user_input=="7":#Exit
        break
    elif user_input=='1':#Add
        Name_con=input("Name jadid ra vared konid:\n ")
        Famil_con=input("Family jadid ra vared konid:\n ")
        Number_con=input("Telefon ra vared konid:\n ")
        contacts[Name_con,Famil_con]=Number_con
        continue
        #num_con+=1
    elif user_input=='2':#Search
        Name_con=input("Name ra kamel vared konid: \n")
        Famil_con=input("Family ra kamel vared konid: \n")
        m=list(contacts.keys())
        for (i,j) in m:
            l=str(i+j)
            f=Name_con + Famil_con
            if f in l:
                 print("shomare mored nazaret BACHE KOONI:\n " + (i) +' ' + (j) +":"+ contacts[(i,j)])
            else:print('name mored nazar sabt nashode ast')
        continue
    elif user_input=='3':#Edit
        Name_con=input("Name ra vared konid: \n")
        Famil_con=input("Family ra vared konid: \n")
        if (Name_con,Famil_con) in contacts:
            print("shomare ghabli: "+ contacts[(Name_con,Famil_con)])
        else:
            print("name mojood nist")
            continue
        Number_con1=input("Telefon JADID ra vared konid: \n")
        contacts[(Name_con,Famil_con)]=Number_con1
        print('telefone jadid ba movafaghiat sabt shod')
        continue
    elif user_input=='4':#Delete
        Name_con=input("baraye hazf Name ra vared konid: \n")
        Famil_con=input("baraye hazf Family ra vared konid: \n")
        if (Name_con,Famil_con) in contacts:
            contacts.pop((Name_con,Famil_con))
            print("shomare hazf shod")
        else:
            print('name mored nazar mojood nist')
        continue
    elif user_input=='5':#Filter
        s1=input("bakhsi az Name ra vared konid: \n")
        m=list(contacts.keys())
        for (i,j) in m:
            l=str(i+j)
            if s1 in l:
                print("shomare mored nazaret BACHE KOONI:\n " + (i) +' ' + (j) +":"+ contacts[(i,j)])
            else:
                print('name mored nazar sabt nashode ast')
        continue
    elif user_input=='6':#Print
        print(contacts)
        continue
    else:
        print("Option SAHIH ra vared konid:\n")
        continue
    #contacts={(Name_con,Famil_con):Number_con}
#contacts.update([(Name_con,Famil_con)],Number_con)
#print("shomare mored nazar:\n"+ (Name_con)+ " " +(Famil_con)+ ':' +contacts[(Name_con,Famil_con)])
print(contacts)
print('Thanks For Your Concideration, See You Later')
