drivers_list = []
licenses_list = []

while True:
    print(f"\nMytaxi System\n")
    print("(1) Licenses Menu")
    print("(2) Drivers Menu")
    print("(3) Shut down\n")

    option = input("Select an option: ").strip().upper()

    if option == "1":

        while True:
            print(f"\nLicenses Indexing\n")
            print("(0) Check license list")
            print("(1) Add new license")
            print("(2) Update license")
            print("(3) Remove license")
            print("(4) Salve licenses")
            print("(5) Load licenses")
            print("(6) Exit\n")
        
            option = input("Select an option: ").strip().upper()

            if option == "0":
                print("\nLicense List\n")
                
                for license in licenses_list:
                    print("".join(license))
                    print()    

                if not licenses_list:
                    print("List empty.\n") 

            elif option == "1":
                
                license = input(f"Enter license (X to exit): ").upper()
                if license.upper() == 'X':
                    break  

                license_validity = input("Value (X to exit): ").title()

                licenses_list.append(f"{license},{license_validity}")
                print(f"\nLicense {license} added to list as {license_validity}.\n")
            
            elif option == "2":
                edit_license = input("Enter license to update validity (X to exit): ").strip().title()
                new_value = input("New value: ").strip().title()
            
                if edit_license.upper() == 'X':
                    break 
            
                found_in_list = False
            
                for i in range(len(licenses_list)):
                    entry = licenses_list[i]
                    license_part, validity = entry.split(",")

                    if license_part == edit_license:
                        licenses_list[i] = f"{license_part},{new_value}"
                        found_in_list = True
                        break  

                    if not found_in_list:
                        print("\nError: License not found. \n")
                    else:                      
                        print(f"\n{edit_license} set as {new_value}.\n")

            elif option == "3":
                target_license = input("Enter license to be removed (X to exit): ").strip().title()
            
                if target_license.upper() == 'X':
                    break  
            
                found_in_list = False
            
                for entry in licenses_list:
                    license_part = entry.split(",")[0]
                    if license_part == target_license:
                        licenses_list.remove(entry)
                        found_in_list = True
                        break  
                    if not found_in_list:
                        print("\nError: License not found.\n")
                                
                print(f"\n{target_license} removed from the list.\n")
            
            elif option == "4": #save
                with open("licenses.txt", "w", encoding="utf-8") as file:
                    for license in licenses_list:
                        file.write(license + "\n")

                print("\nFile updated.\n")
    
            elif option == "5": #load
                with open("licenses.txt", "r", encoding="utf-8") as file:
                    licenses_list = []  # limpa lista antes de carregar

                    for line in file:
                        licenses_list.append(line.strip())
                
                print("\nFile loaded successfully.\n")

            elif option == "6":
                break

    if option == "2":

        while True:
            print(f"\nDrives Management System")
            print(f"Before using the system remember to Load the file to have updated licenses status\n")
            print("(1) View active drivers")
            print("(2) Add new driver")
            print("(3) Remove driver")
            print("(4) Save file")
            print("(5) Load file")
            print("(6) Exit\n")

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
                                print(f"\nThe license for {name_driver} is not valid\n")
                            
                            else:
                                drivers_list.append(f"{name_driver}, {license_number}")
                                print(f"\n{name_driver} added to the list\n")

                            break
                    
                        if not found:
                            print("\nLicense not found.\n")
            
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
                        print(f"\n{name_part} removed from list.\n")
                        break 

                    if not found_in_list:
                        print("\nDriver not found.\n")
            
            elif option == "4": #save
                with open("database-drivers.txt", "w", encoding="utf-8") as file:
                    for driver in drivers_list:
                        file.write(driver + "\n")
                
                print("\nFile updated.\n")
            
            elif option == "5": #load
                with open("database-drivers.txt", "r", encoding="utf-8") as file:
                    drivers_list = []  # limpa lista antes de carregar

                    for line in file:
                        drivers_list.append(line.strip())
                        
                print("\nFile loaded successfully.\n")

            elif option == "6":
                break
        
    if option == "3":
        print("\nGoodbye!\n")
        break
          