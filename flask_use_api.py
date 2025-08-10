users = {}
next_id = 1

def list_users():
    if not users:
        print("No users found.")
    else:
        for uid, user in users.items():
            print(f"ID: {uid}, Name: {user['name']}, Email: {user['email']}")

def add_user():
    global next_id
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    if name and email:
        users[next_id] = {'name': name, 'email': email}
        print(f"User added with ID {next_id}")
        next_id += 1
    else:
        print("Name and email cannot be empty.")

def update_user():
    uid = int(input("Enter user ID to update: "))
    if uid in users:
        name = input(f"Enter new name (leave blank to keep '{users[uid]['name']}'): ").strip()
        email = input(f"Enter new email (leave blank to keep '{users[uid]['email']}'): ").strip()
        if name:
            users[uid]['name'] = name
        if email:
            users[uid]['email'] = email
        print("User updated.")
    else:
        print("User not found.")

def delete_user():
    uid = int(input("Enter user ID to delete: "))
    if uid in users:
        users.pop(uid)
        print("User deleted.")
    else:
        print("User not found.")

def main():
    while True:
        print("\nUser Management")
        print("1. List Users")
        print("2. Add User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            list_users()
        elif choice == '2':
            add_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__== "__main__":
    main()
        
   
