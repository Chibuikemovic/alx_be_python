shopping_list = []

def display_menu():
    print("\n===== Shopping List Menu =====")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
display_menu()

def add_item():
    item = input("Enter item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item():
    item = input("Enter item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' not found in your shopping list.")

def view_list():
    print("\n Your Shopping List:")
    if not shopping_list:
        print("   (Empty)")
    else:
        for idx, item in enumerate(shopping_list, 1):
            print(f"   {idx}. {item}")

# Main loop
while True:
    display_menu()
    choice = input("Select an option (1-4): ").strip()

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_list()
    elif choice == '4':
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
