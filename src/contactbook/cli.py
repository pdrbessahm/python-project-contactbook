from . import services as svc

MENU = """
[1] List contacts
[2] Add contact
[3] Update contact
[4] Delete contact
[0] Exit
> 
"""

def _inp(msg: str) -> str:
    return input(msg).strip()

def main():
    while True:
        choice = _inp(MENU)
        
        if choice == "1":
            for c in svc.list_contacts():
                print(f"{c.id:03d} | {c.name} | {c.email or "-"} | {c.phone or "-"}")
        
        elif choice == "2":
            name = _inp("Name: ")
            email = _inp("Email (optional): ") or None
            phone = _inp("Phone (optional): ") or None
            c = svc.create_contact(name, email, phone)
            print(f"Created #{c.id}.")
        
        elif choice == "3":
            try:
                cid = int(_inp("ID to update: "))

            except ValueError:
                print("Invalid ID."); continue

            name = _inp("New name (blank to keep): ") or None
            email = _inp("New email (blank to keep): ") or None
            phone = _inp("New phone (blanka to keep): ") or None
            
            try:
                c = svc.update_contact(cid, name = name, email = email, phone = phone)
                print(f"Updated #{c.id}.")

            except ValueError as e:
                print(e)
        
        elif choice == "4":
            try:
                cid = int(_inp("ID to delete: "))
            
            except ValueError:
                print("Invalid ID."); continue
            
            try:
                svc.delete_contact(cid)
                print("Deleted.")

            except Exception as e:
                print(e)
        
        elif choice == "0":
            print("Bye!"); break
        else:
            print("Invalid option.")
    
if __name__ == "__main__":
    main()