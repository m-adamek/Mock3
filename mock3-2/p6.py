import re

def f(mnumbers):
    # Wyrażenie regularne sprawdzające poprawność numeru
    pattern = r"^[+-]?([1-7a-dA-D])+"
    valid_count = 0
    
    # Iterujemy przez wszystkie numery i sprawdzamy ich zgodność z wzorem
    for num in mnumbers:
        if re.match(pattern, num):
            valid_count += 1
    
    return valid_count

# Przykłady:
print(f(["A15", "-31", "7abC", "+D1", "-gH"]))  # 5
print(f(["A05", "-3+1", "7ab8C", "+D1", "-22k"]))  # 1


# ^ — Dopasowanie zaczyna się od początku ciągu.
# [+-]? — Opcjonalny znak + lub - (numer może zaczynać się od tych znaków, ale nie musi).
# ([1-7a-dA-D])+ — Ciąg musi zawierać przynajmniej jedną cyfrę od 1 do 7 lub literę od a do d (lub ich wielką wersję).
# Znak + oznacza, że takie znaki mogą się powtarzać dowolną liczbę razy.
