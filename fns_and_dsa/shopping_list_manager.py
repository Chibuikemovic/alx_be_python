def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
choice = int(input("Choose a number from 1 to 4 "))

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == '3':
            print("Your Shopping List:")
            if not shopping_list:
                print("   (List is empty)")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"   {i}. {item}")

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
