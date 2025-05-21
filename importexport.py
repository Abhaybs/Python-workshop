import os
import csv

folder_path = "D:/Users"
file_path = os.path.join(folder_path, "goods.csv")

def create_file():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")

    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Item", "Quantity", "Country"])
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")

def write_file(good_type, item, quantity, country):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([good_type, item, quantity, country])
    print(f"Recorded: {good_type} - {item}, Qty: {quantity}, Country: {country}")

def read_file():
    if not os.path.exists(file_path):
        print("No data file found.")
        return
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

def search_item(search_item):
    found = False
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1].lower() == search_item.lower():
                print("Item Found:", ', '.join(row))
                found = True
    if not found:
        print("Item not found.")

def clear_data():
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Item", "Quantity", "Country"])
    print("All records cleared.")

def validate_input(good_type):
    item = input("Enter item name: ").strip()
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Quantity must be a number.")
    country = input("Enter country name: ").strip()
    return good_type, item, quantity, country

if __name__ == "__main__":
    create_file()
    while True:
        print("\nChoose an option:")
        print("1. Import Goods")
        print("2. Export Goods")
        print("3. View All Records")
        print("4. Search Item by Name")
        print("5. Clear All Records")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            data = validate_input("Import")
            write_file(*data)
        elif choice == "2":
            data = validate_input("Export")
            write_file(*data)
        elif choice == "3":
            read_file()
        elif choice == "4":
            search = input("Enter item name to search: ")
            search_item(search)
        elif choice == "5":
            confirm = input("Are you sure you want to delete all records? (yes/no): ")
            if confirm.lower() == "yes":
                clear_data()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")