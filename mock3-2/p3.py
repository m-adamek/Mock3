def f(d):
    # Obliczanie łącznej liczby pasażerów
    total_passengers = 0
    for passengers in d.values():
        total_passengers += passengers
    
    # Obliczanie średniej liczby pasażerów
    num_flights = len(d)
    average_passengers = total_passengers / num_flights
    
    # Licznik lotów, w których liczba pasażerów przekracza średnią
    count = 0
    for passengers in d.values():
        if passengers > average_passengers:
            count += 1
    
    # Zwracanie wyniku
    return count

# Przykłady:
print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))  # 2
print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))   # 1
