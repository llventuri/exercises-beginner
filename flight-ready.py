import random 
from datetime import date

passenger_list = []

while True:
    print(f"Flight US4583 Sao Paulo - Salvador {date.today()} \n\n What do you want to access? \n\n - Check Passengers List (C) \n - Add Passenger (A) \n - Edit Passenger (E) \n - Remove Passenger (R) \n - Save Passengers (S) \n - Load Passengers (L) \n - Check Map Seat (M) \n - Exit (Q)\n")

    option = input("Select an option: ").strip().upper()

    if option == "C":
        print("\nVoo US4583 Sao Paulo - Salvador\n")
        for passenger in passenger_list:
            print("".join(passenger))
        print()    

        if not passenger_list:
            print("Nenhum passageiro no voo.\n")   

    elif option == "A":
        while True:
            new_passenger = input(f"Digite nome completo do novo passageiro (S para sair): ").strip().title()

            if new_passenger.upper() == 'S':
                break    
            
            seat_taken = True

            while seat_taken: 
                seat_number = random.randint(1, 10)
                seat_letter = random.choice("ABCDEF")
                seat = f"{seat_number:02}{seat_letter}"

                seat_taken = False  

                for entry in passenger_list:
                    seat_part = entry.split(",")[1]
                    if seat_part == seat:
                      seat_taken = True
                      break
            
            passenger_list.append(f"{new_passenger},{seat}")
            print(f"\nPassageiro {new_passenger} alocado no assento {seat}.\n")

    elif option == "R":
        target_passenger = input("Nome completo do passageiro a ser remover (S para sair): ").strip().title()
        
        if target_passenger.upper() == 'S':
                break  
        
        found_in_list = False
        
        for entry in passenger_list:
            passenger_part = entry.split(",")[0]
            if passenger_part == target_passenger:
                passenger_list.remove(entry)
                found_in_list = True
                break  
            if not found_in_list:
                print("\nErro: Passageiro nao encontrado.\n")
                              
        print(f"{target_passenger} removido(a).")
    
    elif option == "E":
        edit_passenger = input("Nome completo do passageiro a ser editado (S para sair): ").strip().title()
        new_name = input("Digite o novo nome (S para sair): ").strip().title()
        
        if edit_passenger.upper() == 'S':
                break  
        
        found_in_list = False
        
        for i in range(len(passenger_list)):
            entry = passenger_list[i]
            name_part, seat = entry.split(",")

            if name_part == edit_passenger:
                passenger_list[i] = f"{new_name},{seat}"
                found_in_list = True
                break  

        if not found_in_list:
            print("\nErro: Passageiro nao encontrado.\n")
        else:                      
            print(f"\n{edit_passenger} renomeado(a) como {new_name}.\n")    

    elif option == "S":

        with open("flight_us4583.txt", "w", encoding="utf-8") as file:
            file.write("Flight US4583\n\n")
            
            for passenger in passenger_list:
                file.write(passenger + "\n")

        print("File saved successfully.\n")    

    elif option == "L":

        with open("flight_us4583.txt", "r", encoding="utf-8") as file:
            
            passenger_list = []  # limpa lista antes de carregar

            for line in file:
                line = line.strip()
                if "," in line:
                        passenger_list.append(line)
                
        print("\nFile loaded successfully.\n")    

    elif option == "M":
        print("\nMapa Atualizado:\n")

        for i in range(1, 11):
            for c in "ABCDEF":
                current_seat = f"{i:02d}{c}"
                
                occupied = False

                for entry in passenger_list:
                    name, seat = entry.split(",")

                    if seat == current_seat:
                        occupied = True
                        break

                if occupied:
                    print(" X ", end=" ")
                else:
                    print(current_seat, end=" ")
                if c == "C":
                    print("| |", end=" ")

            print()

        # seat = entry.split(",")[1]
        # for i in range(1, 11): # usamos 11 pois o range para 1 antes
        #     for c in "ABCDEF":
        #         for line in passenger_list:
        #             if f"{i:02d}{c}" == seat:
        #                 print(" X ", end=" ")
        #                 break
        #         else:
        #             print(f"{i:02d}{c}", end=" ")
        #         if c == "C":
        #             print("| | ", end=" ")
        #     print()
        # print()
    
    elif option == "Q":
        print("\nGoodbye!\n")
        break