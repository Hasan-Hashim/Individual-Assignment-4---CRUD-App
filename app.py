import json

DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def display_data():
    data = load_data()
    for index, item in enumerate(data, start=1):
        print(f"{index}. {item['title']} - {item['description']}")

def add_data():
    title = input("Enter title: ")
    description = input("Enter description: ")
    data = load_data()
    data.append({'title': title, 'description': description})
    save_data(data)
    print("Data added successfully.")

def update_data():
    display_data()
    data = load_data()
    index = int(input("Enter the number of the item to update: ")) - 1
    if 0 <= index < len(data):
        data[index]['title'] = input("Enter new title: ")
        data[index]['description'] = input("Enter new description: ")
        save_data(data)
        print("Data updated successfully.")
    else:
        print("Invalid item number.")

def delete_data():
    display_data()
    data = load_data()
    index = int(input("Enter the number of the item to delete: ")) - 1
    if 0 <= index < len(data):
        del data[index]
        save_data(data)
        print("Data deleted successfully.")
    else:
        print("Invalid item number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display Data")
        print("2. Add Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_data()
        elif choice == '2':
            add_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
