import Generator_danych_stron  # importowanie pliku jako moduł
from Generator_danych_stron import *

wartosci = open("wartosci.txt", "r")  # odczytywanie pliku
wynik = open("wynik.txt", "w")  # plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana

Generator_danych_stron.generator()  # wywołanie z Generator_danych_stron funkcji generator()


def funkcja_LRU():
    # listy
    ramka = []  # przechowuje strony
    ak_dlugosc = 0  # aktualna długość
    zamiana = 0  # zamiany
    nst_miejsce = 0  # najstarsze miejsce

    # poniżej wprowadzamy ilość ramek na jakiej wykonamy próby
    ramki = int(input("Wprowadz ilosc ramek: "))

    while ak_dlugosc < ramki:  # pętla while dla odpowiedniego warunku
        nast_st = wartosci.readline()  # następna strona, odczytywanie pliku - wartosci

        if nast_st not in ramka:
            ramka.insert(ak_dlugosc, nast_st)  # metoda ramka.insert() wstawia element na listę o określonym indeksie
            ak_dlugosc += 1  # inkrementacja aktualnej długości

    while ak_dlugosc < 100:  # pętla while dla odpowiedniego warunku
        nast_st = wartosci.readline()  # przyrownanie zmiennej do pliku wartosci i
        # odczytywanie pliku pojedyńczymi liniami

        if nast_st not in ramka:
            ramka[nst_miejsce] = nast_st
            nst_miejsce = (nst_miejsce + 1) % ramki
            zamiana += 1  # inkrementacja liczby zamian
        else:
            nst_miejsce = (nst_miejsce + 1) % ramki

        ak_dlugosc += 1  # inkrementacja aktualnej dlugłości

    # wypisanie do pliku - wyniki - ilosci zastąpionych stron dla danej ilosci ramek oraz liczba ich zamian
    wynik.write("Ilosc zastapionych stron dla " + str(len(ramka)) + " ramek, wynosi = " + str(zamiana) + "\n")

    wartosci.close()  # zamykanie pliku
    wynik.close()  # zamykanie pliku


funkcja_LRU()  # wywołanie funkcji
