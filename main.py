def tipareste_meniu():
    print("1. Citire date")
    print("2. Cea mai lunga secventa in care toate elementele sunt patrate perfecte")
    print("3. Cea mai lunga secventa in care toate elementele au acelasi numar de biti de 1 in reprezentarea binara")
    print("4. Cea mai lunga secventa in care toate elementele sunt pare")
    print("5. Iesire")


def citeste_lista(lista: list) -> list[int]:
    """
    Citeste de la tastatura elementele unei liste
    :param lista: lista care trebuie citita de la tastatura
    :return: lista cu elemente citite de la tastatura
    """
    numar_elemente = int(input("Dati numarul de elemente ale liste: "))
    for i in range(numar_elemente):
        lista.append(int(input("Lista["+str(i)+"]= ")))
    return lista


def is_perfect_square(n: int) -> bool:
    """
    Verifica daca un numar este patrat perfect sau nu
    :param n: Numarul care trebuie verificat
    :return: True daca numarul este patrat perfect sau False in caz contrar
    """
    for i in range(1, n+1):
        if i*i == n:
            return True
        elif i*i > n:
            return False


def test_is_perfect_square():
    assert(is_perfect_square(16)) is True
    assert(is_perfect_square(10)) is False
    assert (is_perfect_square(100)) is True


def toate_elementele_patrate_perfecte(lista: list) -> bool:
    """
    Verifica daca toate elementele unei liste sunt patrate perfecte
    :param lista: Lista asupra careia se face verificarea
    :return: True daca toate elementele sunt patrate perfecte sau False in caz contrar
    """
    for x in lista:
        if is_perfect_square(x) is False:
            return False
    return True


def test_toate_elementele_patrate_perfecte():
    assert(toate_elementele_patrate_perfecte([16, 9, 36])) is True
    assert (toate_elementele_patrate_perfecte([15, 9, 36])) is False
    assert (toate_elementele_patrate_perfecte([16, 9, 36, 64, 100])) is True


def get_longest_all_perfect_squares(lista: list) -> list[int]:
    """
    Determina cea mai lunga secventa de patrate perfecte dintr-o lista
    :param lista: Lista asupra careia se face verificarea
    :return: Se returneaza elementele celei mai lungi subsecvente de patrate perfecte
    """
    subsecventa_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if toate_elementele_patrate_perfecte(lista[i:j + 1]) and len(subsecventa_max) < len(lista[i:j + 1]):
                subsecventa_max = lista[i:j + 1]
    return subsecventa_max


def test_get_longest_all_perfect_squares():
    assert(get_longest_all_perfect_squares([16, 9, 1, 5, 36, 49])) == [16, 9, 1]
    assert (get_longest_all_perfect_squares([101, 10, 12, 5, 6, 50])) == []
    assert (get_longest_all_perfect_squares([9, 1, 5, 36, 49, 12, 16, 25, 100])) == [16, 25, 100]


def get_number_of_bits_equal_to_one(x: int) -> int:
    """
    Determina cati biti sunt egali cu 1 in reprezentarea binara a unui numar dat
    :param x: Numarul al carui numar de biti este calculat
    :return: Returneaza numarul de biti egali cu 1
    """
    numar_biti = 0
    while x != 0:
        if x % 2 == 1:
            numar_biti += 1
        x = x//2
    return numar_biti


def test_get_number_of_bits_equal_to_one():
    assert(get_number_of_bits_equal_to_one(12)) == 2
    assert (get_number_of_bits_equal_to_one(19)) == 3
    assert (get_number_of_bits_equal_to_one(55)) == 5


def toate_elementele_au_numar_egal_de_biti(lista: list) -> bool:
    """
    Verifica daca toate elementele unei liste au acelasi numar de biti egali cu 1
    :param lista: Lista asupra careia se efectueaza verificarea
    :return: True daca toate elementele listei au acelasi numar de biti egal cu 1 sau False in caz contrar
    """
    numar_biti = get_number_of_bits_equal_to_one(lista[0])
    for x in lista[:len(lista)]:
        if get_number_of_bits_equal_to_one(x) != numar_biti:
            return False
    return True


def test_toate_elementele_au_numar_egal_de_biti():
    assert(toate_elementele_au_numar_egal_de_biti([12, 15, 17])) is False
    assert (toate_elementele_au_numar_egal_de_biti([12, 17, 18])) is True
    assert (toate_elementele_au_numar_egal_de_biti([12, 18, 24])) is True


def get_longest_same_bit_counts(lista: list) -> list[int]:
    """
    Determina cea mai lunga secventa de numere ce au acelasi numar de biti egali cu 1 in reprezentarea binara
    :param lista: Lista asupra careia se efectueaza operatia
    :return: Returneaza cea mai lunga subsecventa ce indeplineste conditia
    """
    subsecventa_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if toate_elementele_au_numar_egal_de_biti(lista[i:j + 1]) and len(subsecventa_max) < len(lista[i:j + 1]):
                subsecventa_max = lista[i:j + 1]
    return subsecventa_max


def test_get_longest_same_bit_counts():
    assert(get_longest_same_bit_counts([12, 17, 15, 21, 22, 25])) == [21, 22, 25]
    assert (get_longest_same_bit_counts([11, 12, 15, 27])) == [15, 27]
    assert (get_longest_same_bit_counts([14, 19, 21, 30, 31])) == [14, 19, 21]


def toate_elementele_pare(lista: list) -> bool:
    """
    Verifica daca toate elementele unei liste sunt pare
    :param lista: Lista asupra careia se efectueaza verificarea
    :return: Returneaza True daca toate elementele listei sunt pare sau False in caz contrar
    """
    for x in lista:
        if x % 2 == 1:
            return False
    return True


def test_toate_elementele_pare():
    assert(toate_elementele_pare([2, 4, 18, 66])) is True
    assert(toate_elementele_pare([6, 12, 15, 18])) is False
    assert (toate_elementele_pare([])) is True


def get_longest_all_even(lista: list) -> list[int]:
    """
    Determina cea mai lunga subsecventa de numere pare dintr-o lista
    :param lista: Lista asupra careia se efectueaza determinarea
    :return: Cea mai lunga subsecventa care contine doar numere pare
    """
    subsecventa_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if toate_elementele_pare(lista[i:j + 1]) and len(subsecventa_max) < len(lista[i:j + 1]):
                subsecventa_max = lista[i:j + 1]
    return subsecventa_max


def test_get_longest_all_even():
    assert(get_longest_all_even([5, 4, 6, 8, 9, 16, 12, ])) == [4, 6, 8]
    assert (get_longest_all_even([50, 48, 25, 16, 32, 36])) == [16, 32, 36]
    assert (get_longest_all_even([10, 12, 14, 15, 25])) == [10, 12, 14]


def main():
    test_is_perfect_square()
    test_toate_elementele_patrate_perfecte()
    test_get_longest_all_perfect_squares()
    test_get_number_of_bits_equal_to_one()
    test_toate_elementele_au_numar_egal_de_biti()
    test_get_longest_same_bit_counts()
    test_toate_elementele_pare()
    test_get_longest_all_even()
    while True:
        tipareste_meniu()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = []
            citeste_lista(lista)
        elif optiune == "2":
            print(get_longest_all_perfect_squares(lista))
        elif optiune == "3":
            print(get_longest_same_bit_counts(lista))
        elif optiune == "4":
            print(get_longest_all_even(lista))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita, incercati din nou!")


main()
