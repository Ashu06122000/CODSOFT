import os

def display_todo_list():
    with open('todo.txt', 'r') as file:
        todo_list = file.readlines()
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for index, item in enumerate(todo_list, start=1):
                print(f"{index}. {item.strip()}")

def add_todo_item(item):
    with open('todo.txt', 'a') as file:
        file.write(item + '\n')
    print(f"'{item}' has been added to your to-do list.")

def remove_todo_item(index):
    try:
        with open('todo.txt', 'r') as file:
            todo_list = file.readlines()
        
        if 1 <= index <= len(todo_list):
            removed_item = todo_list.pop(index - 1)
            
            with open('todo.txt', 'w') as file:
                file.writelines(todo_list)
            
            print(f"'{removed_item.strip()}' has been removed from your to-do list.")
        else:
            print("Invalid index. Please enter a valid index.")

    except FileNotFoundError:
        print("Your to-do list is empty.")

def main():
    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a new item")
        print("3. Remove an item")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_todo_list()
        elif choice == '2':
            item = input("Enter the task you want to add: ")
            add_todo_item(item)
        elif choice == '3':
            index = int(input("Enter the index of the item you want to remove: "))
            remove_todo_item(index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if not os.path.isfile('todo.txt'):
        with open('todo.txt', 'w'):
            pass

main()