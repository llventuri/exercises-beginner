
drivers_list = []

while True:
    print(f"Drives Management System")
    print(f"Before using the system remember to Load the file to have updated licenses status")
    print("(1) View active drivers")
    print("(2) Add new driver")
    print("(3) Remove driver")
    print("(4) Save file")
    print("(5) Load file")
    print("(6) Exit")

    option = input("Select an option: ").strip().upper()

    if option == "1":
        print("\nActive Drivers\n")
        for driver in drivers_list:
            print(driver)
        print()    

    elif option == "2":
        while True:
            name_driver = input(f"Enter driver name (X to exit): ").title()

            if name_driver.upper() == 'X':
                break  

            license_number = input("Enter license number(X to exit): ")

            with open("licenses.txt", "r") as file:
                licenses = file.read().splitlines()
                #print(licenses) debugin

            found = False

            for line in licenses:
                parts = line.split(",")
                code = parts[0]
                status = parts[1]

                #print(code, status) debugin
            
                if code == license_number:
                    found = True

                    if status == "False":
                        print(f"The license for {name_driver} is not valid")
                    
                    else:
                        drivers_list.append(f"{name_driver}, {license_number}")
                        print(f"{name_driver} added to the list")

                    break
            
                if not found:
                    print("License not found.")
    
    elif option == "3":
        name_driver = input("Enter the driver's name (X for exit): ").strip().title()
        
        if name_driver.upper() == 'X':
                break  
        

        found_in_list = False #flag up
        
        for entry in drivers_list:
            name_part = entry.split(", ")[0]
            
            if name_part == name_driver:
                drivers_list.remove(entry)
                found_in_list = True #flag down, loop stops
                print(f"{name_part} removed from list.")
                break 

            if not found_in_list:
                print("Driver not found.")
    
    elif option == "4": #save
        with open("database-drivers.txt", "w", encoding="utf-8") as file:
            for driver in drivers_list:
                file.write(driver + "\n")
        
        print("File updated.")
    
    elif option == "5": #load
        with open("database-drivers.txt", "r", encoding="utf-8") as file:
            drivers_list = []  # limpa lista antes de carregar

            for line in file:
                drivers_list.append(line.strip())
                
        print("File loaded successfully.")

    elif option == "6":
        print("Goodbye!")
        break