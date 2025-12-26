# CSV Merger

**CSV Merger** to prosty, praktyczny program w Pythonie do łączenia wielu plików CSV w jeden.  

Projekt powstał, aby pomóc w automatyzacji pracy z danymi i oszczędzić czas przy ręcznym scalaniu wielu plików CSV.

---

## Funkcjonalności

- Łączenie wielu plików CSV z jednego folderu w jeden plik `merged.csv`
- Zachowanie nagłówka tylko raz
- Nadawanie nowych, unikalnych ID dla każdego wiersza
- Obsługa folderów z dużą ilością plików
- Wersja konsolowa – prosta w użyciu

---

## Wymagania

- Python 3.8+
- Moduły standardowe: `os`, `csv`

---

## Jak używać

1. Skopiuj repozytorium
2. Umieść wszystkie pliki CSV w jednym folderze
3. Uruchom program:
```bash
python csv_merger.py
Podaj ścieżkę do folderu z plikami CSV

Program utworzy plik merged.csv w tym samym folderze

W terminalu zobaczysz podsumowanie:

ile plików scalono

ile wierszy zapisano

Przykład działania
styczen.csv

bash
Skopiuj kod
id,produkt,cena
1,telefon,1200
2,laptop,3500
luty.csv

bash
Skopiuj kod
id,produkt,cena
1,monitor,800
2,mysz,120
Po scaleniu (merged.csv)

bash
Skopiuj kod
id,produkt,cena
1,telefon,1200
2,laptop,3500
3,monitor,800
4,mysz,120
Cel projektu
Projekt pokazuje, jak automatyzować pracę z danymi i jest świetnym przykładem dla GitHub portfolio lub praktyk.

Autor
Twoje Imię i Nazwisko | Twój GitHub

yaml
Skopiuj kod
