def hanoi(n, z_ustawienia, na_ustawienie, za_pomoca_ustawienia):
    if n == 1:
        print(f"Przenies dysk 1 z ust. {z_ustawienia} na ust. {na_ustawienie}")
        return
    hanoi(n-1, z_ustawienia, za_pomoca_ustawienia, na_ustawienie)
    print(f"Przenies dysk {n} z ust. {z_ustawienia} na ust. {na_ustawienie}")
    hanoi(n-1, za_pomoca_ustawienia, na_ustawienie, z_ustawienia)

n = 5
hanoi(n, 'A', 'C', 'B')