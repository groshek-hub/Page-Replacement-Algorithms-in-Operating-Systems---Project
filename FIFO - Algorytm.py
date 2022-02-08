import Generator_danych_stron  # importowanie pliku jako moduł
from Generator_danych_stron import *

wartosci = open("wartosci.txt", "r")  # odczytywanie pliku
wynik = open("wynik.txt", "w")  # plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana

Generator_danych_stron.generator()  # wywołanie z Generator_danych_stron funkcji generator()


def funkcja_FIFO():
    # listy
    ramka = []  # przechowuje strony
    ak_dlugosc = 0  # aktualna długość
    zamiany = 0  # zamiany

    # poniżej wprowadzamy ilość ramek na jakiej wykonamy próby
    ramki = int(input("Wprowadz ilosc ramek: "))

    while ak_dlugosc < ramki:  # pętla while dla odpowiedniego warunku
        nast_st = int(wartosci.readline())  # następna strona
        if nast_st not in ramka:
            ramka.insert(ak_dlugosc, nast_st) # metoda ramka.insert() wstawia element na listę o określonym indeksie
            ak_dlugosc += 1  # inkrementacja aktualnej długości

    while ak_dlugosc < 100:
        nast_st = wartosci.readline()
        if nast_st not in ramka:
            for i in range(ramki - 1):
                ramka[i] = ramka[i + 1]

            ramka[ramki - 1] = nast_st
            zamiany += 1  # inkrementacja liczby zamian

        ak_dlugosc += 1  # inkrementacja aktualnej dlugłości

    # wypisanie do pliku - wyniki - ilosci zastąpionych stron dla danej ilosci ramek oraz liczba ich zamian
    wynik.write("Ilosc zastapionych stron dla " + str(len(ramka)) + " ramek, wynosi = " + str(zamiany) + "\n")

    wartosci.close()  # zamykanie pliku
    wynik.close()  # zamykanie pliku


funkcja_FIFO()  # wywołanie funkcji
