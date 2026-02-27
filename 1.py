# O sistema deve armazenar os dados em uma lista, e deve possuir um menu com as opções mínimas:
# Visualizar dados
# Adicionar item
# Remover item
# Salvar dados em um arquivo
# Carregar dados de um arquivo
# Sair/Encerrar

# O programa deve rodar em um loop infinito, que encerra quando o usuário escolher a opção de Sair.

from datetime import date

import random


map_seat = [
    ["01A", "01B", "01C", "| |", "01D", "01E", "01F"],
    ["02A", "02B", "02C", "| |", "02D", "02E", "02F"],
    ["03A", "03B", "03C", "| |", "03D", "03E", "03F"],
    ["04A", "04B", "04C", "| |", "04D", "04E", "04F"],
    ["05A", "05B", "05C", "| |", "05D", "05E", "05F"],
    ["06A", "06B", "06C", "| |", "06D", "06E", "06F"],
    ["07A", "07B", "07C", "| |", "07D", "07E", "07F"],
    ["08A", "08B", "08C", "| |", "08D", "08E", "08F"],
    ["09A", "09B", "09C", "| |", "09D", "09E", "09F"],
    ["10A", "10B", "10C", "| |", "10D", "10E", "10F"]
]

passenger_list = []

while True:
    print(f"Flight US4583 Sao Paulo - Salvador {date.today()} \n\n What do you want to access? \n\n - Check Passengers List (C) \n - Add Passenger (A) \n - Remove Passenger (R) \n - Load Passengers (L) \n - Save Passengers (S) \n - Check Map Seat (M) \n - Exit (Q)\n")

    option = input("Select an option: ").strip().upper()

    if option == "C":
        print("\nVoo US4583 Sao Paulo - Salvador\n")
        for passenger in passenger_list:
            print(passenger.title())
        print()    

        if not passenger_list:
            print("Nenhum passageiro no voo.\n") 
            print("---------------------------------")    

    elif option == "A":
        while True:
            new_passenger = input(f"Digite nome completo do novo passageiro (S para sair): ").strip().title()

            if new_passenger.upper() == 'S':
                break  

                #seat selection
            found_seat = False #flag up
            while not found_seat:
                row_idx = random.randint(0, 9)  #random row
                #skip index 3 (the corridor)
                seat_idx = random.choice([0, 1, 2, 4, 5, 6])

                current_value = map_seat[row_idx][seat_idx]
                
                if current_value != " X ":
                    # Assign the seat
                    seat_code = current_value 
                    map_seat[row_idx][seat_idx] = " X "
                    
                    passenger_list.append(f"{new_passenger}, {seat_code}")
                    
                    print(f"{new_passenger} alocado no assento {seat_code}.")

                    found_seat = True #flag down, loop stops
                else:
                    # If hit 'X', the loop continues
                    continue    

    elif option == "R":
        target_passenger = input("Nome completo do passageiro a ser remover (S para sair): ").strip().title()
        
        if target_passenger.upper() == 'S':
                break  
        

        found_in_list = False #flag up
        
        for entry in passenger_list:
            #print(f"Checking: '{target_passenger}' against '{entry}'") 

            #take the name
            name_part = entry.split(", ")[0]
            
            if name_part == target_passenger:
                
                #take the seat
                seat_to_free = entry.split(", ")[1]
                
                passenger_list.remove(entry)

                found_in_list = True #flag down, loop stops
                
                for row in map_seat:
                    if row[0][:2] == seat_to_free[:2]:
                        for i in range(len(row)):
                            letters = ["A", "B", "C", "dummy", "D", "E", "F"]
                            if row[i] == " X ":
                                current_letter = letters[i]
                                if current_letter == seat_to_free[2]:
                                    row[i] = seat_to_free
                
                print(f"{name_part} removido(a).")
                break 

        if not found_in_list:
            print("Erro: Passageiro não encontrado.")

    elif option == "S":

        with open("flight_us4583.txt", "w", encoding="utf-8") as file:
            file.write("Flight US4583\n\n")
            for line in passenger_list:
                file.write(line + "\n")
        
        print("Arquivo de passageiros salvo.")

    elif option == "L":

        with open("flight_us4583.txt", "r", encoding="utf-8") as file:
                # 1. Read all lines into a list
                all_lines = file.readlines()
                
                # 2. Clear the current list so we don't have duplicates
                passenger_list.clear()
                
                # 3. Process each line
                for line in all_lines:
                    line = line.strip()
                    # We only want lines that have a comma (the passengers)
                    if "," in line:
                        passenger_list.append(line)
                        
                        # 4. Update the Map (Put the ' X ' back)
                        parts = line.split(", ")
                        seat_code = parts[1] # e.g., "07C"
                        
                        row_idx = int(seat_code[:2]) - 1
                        letters_map = {"A":0, "B":1, "C":2, "D":4, "E":5, "F":6}
                        col_idx = letters_map[seat_code[2]]
                        
                        map_seat[row_idx][col_idx] = " X "
                
                print(f"Sucesso! {len(passenger_list)} passageiros carregados e mapa atualizado.")      

    elif option == "M":
        print("\nMapa Atualizado:\n")
        for row in map_seat:
            print(" ".join(row))
        print()    
    
    elif option == "Q":
        print("Goodbye!")
        break