storage = []
inventory = []

print("\nAre you a 1. seller or 2. buyer?\n")

while True:
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:  # Seller
        print("\nSeller Menu:")
        print("1. Add items to storage")
        print("2. Move items to inventory")
        print("3. View storage")
        print("4. View inventory")
        
        seller_choice = int(input("Enter option (1-4): "))
        
        if seller_choice == 1:
            n = int(input("Enter number of items to add: "))
            for _ in range(n):
                item = input("Enter item to add: ")
                storage.append(item)
            print(f"Storage updated: {storage}")
            
        elif seller_choice == 2:
            if not storage:
                print("Storage is empty!")
                continue
                
            print(f"Storage: {storage}")
            item = input("Enter item to move to inventory: ")
            if item in storage:
                storage.remove(item)
                inventory.append(item)
                print(f"Moved '{item}' to inventory. Inventory: {inventory}")
            else:
                print("Item not in storage!")
                
        elif seller_choice == 3:
            print(f"Current storage: {storage}")
            
        elif seller_choice == 4:
            print(f"Current inventory: {inventory}")
            
        else:
            print("Invalid seller option!")
    
    elif choice == 2:  # Buyer
        if not inventory:
            print("Inventory is empty! Please check back later.")
            continue
            
        print(f"Available items: {inventory}")
        item = input("Enter item to buy: ")
        if item in inventory:
            inventory.remove(item)
            print(f"Purchased '{item}'. Remaining inventory: {inventory}")
        else:
            print("Item not available in inventory!")
    
    else:
        print("Invalid choice. Please select 1 (Seller) or 2 (Buyer).")