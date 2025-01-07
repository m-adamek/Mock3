def f(n):
    # Zamiana liczby na listę cyfr
    digits = []
    for d in str(n):
        digits.append(int(d))
    
    # Wyodrębnienie cyfr nieparzystych
    odd_digits = []
    for d in digits:
        if d % 2 != 0:
            odd_digits.append(d)
    
    # Jeśli brak cyfr nieparzystych, zwróć -1
    if len(odd_digits) == 0:
        return -1
    
    # Obliczenie największej i najmniejszej cyfry nieparzystej
    max_odd = max(odd_digits)
    min_odd = min(odd_digits)
    
    # Zwrócenie różnicy między największą a najmniejszą cyfrą
    return max_odd - min_odd

# Przykłady:
print(f(10852))    # 4 (największa: 5, najmniejsza: 1)
print(f(723597))   # 6 (największa: 9, najmniejsza: 3)
print(f(4388))     # 0 (największa i najmniejsza: 3)
print(f(846206))   # -1 (brak cyfr nieparzystych)
