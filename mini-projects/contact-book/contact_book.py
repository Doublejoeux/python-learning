#contact_book
contacts = []
def new():
    data = {"name": "", "phone": ""}
    name = input("Enter name: ").title()
    if any(c['name'] == name for c in contacts):
        print("Already Taken")
    else:    
        print(f"'name': {name}")
        data["name"] = name
        phone = input("Enter phone number: ")
        if phone.isdigit():
            print(f"'phone': {phone}")
            data["phone"] = phone
            contacts.append(data)
        else:
            print("only numbers allowed")
def view_contact():
    if len(contacts) == 0:
        print("No contacts available")
    else:
        by_name = sorted(contacts, key=lambda a: a["name"])
        for con in by_name:
            print(con)
def search_contact():
    if len(contacts) == 0:
        print("No contacts available")
    else:
        name = input("Enter a Name: ").title()
        if not any(c['name'] == name for c in contacts):
            print("Not found")
        else:
            search = next(c for c in contacts if c['name'] == name)
            print(search)
def remove_contact():
    if len(contacts) == 0:
        print("No contacts available")
    else:
        name = input("Enter a name: ").title()
        match = next((c for c in contacts if c['name'] == name), None)
        if match != None:
            contacts.remove(match)             
            print(f"{name} removed")
            view_contact()
            return
        else:
            print("Not found")
def edit():   
        if len(contacts) == 0:
            print("No contacts available")
        else:  
            name = input("Enter a name: ").title()
            match = next((c for c in contacts if c['name'] == name), None)
            if match == None:
                print("Not found")
            else:
                def edit_process():
                    edit_options = ["name", "number", "quit"]
                    choice = input("What to edit: Name, Number or Quit?: ").lower()
                    if choice not in edit_options:
                        print("Invalid")
                        return True
                    elif choice == "name":
                        edit_name = input("Enter new name: ").title()
                        match['name'] = edit_name
                        print(match)
                        return True
                    elif choice == "number":
                        edit_number = input("Enter new number: ")
                        if edit_number.isdigit():
                            match['phone'] = edit_number
                            print(match)
                        else:
                            print("Only numbers allowed")
                            return True
                    else:
                        print("Done")
                        return False
                editing = True
                while editing == True:
                    editing = edit_process()
def quit():
    print("End!")
    return False
def running():
    options = ["add", "view","search", "remove", "edit", "quit"]
    start = input("Add, View, Search, Remove, Edit, Quit: ").lower()
    if start not in options:
        print("Not allowed")
        return True
    elif start == "add":
        new()
        return True
    elif start == "view":
        view_contact()
        return True
    elif start == "search":
        search_contact()
        return True
    elif start == "remove":
        remove_contact()
        return True
    elif start == "edit":
        edit()
        return True
    else:
        quit()
        return False
def begin():
    start = True
    while start == True:
        start = running()
begin()