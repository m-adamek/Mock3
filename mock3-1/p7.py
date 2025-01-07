def f(arr2D):
    # Liczba kolumn - bierzemy długość pierwszego wiersza
    num_cols = len(arr2D[0])
    
    # Lista do przechowywania sum kolumn
    col_sums = []
    
    # Iterujemy po każdej kolumnie (indeks od 0 do num_cols - 1)
    for i in range(num_cols):
        col_sum = 0  # Suma bieżącej kolumny
        
        # Iterujemy po każdym wierszu
        for row in arr2D:
            # Sprawdzamy, czy bieżąca kolumna istnieje w danym wierszu
            if i < len(row):
                col_sum += row[i]  # Dodajemy wartość do sumy kolumny
        
        # Dodajemy sumę kolumny do listy wyników
        col_sums.append(col_sum)
    
    # Sprawdzamy, czy są duplikaty w listach sum kolumn
    unique_sums = set(col_sums)
    if len(col_sums) != len(unique_sums):
        return True  # Są kolumny z tą samą sumą
    else:
        return False  # Wszystkie kolumny mają unikalne sumy

# Przykłady:
print(f([[3, 4, 2], [5, 1, 6]]))              # True (suma kolumn: [8, 5, 8])
print(f([[3, 4, 2], [5, 1, 7]]))              # False (suma kolumn: [8, 5, 9])
print(f([[3, 4], [5, 1], [4, 7]]))            # True (suma kolumn: [12, 12])
print(f([[3, 4], [5, 9], [4, 7]]))            # False (suma kolumn: [12, 20])
