import os
import csv

print("=== CSV MERGER ===")

# 1. Pobieramy ścieżkę do folderu
folder_path = input("Podaj ścieżkę do folderu z plikami CSV: ").strip()

# 2. Nazwa pliku wynikowego
output_file = os.path.join(folder_path, "merged.csv")

# 3. Szukamy wszystkich plików .csv w folderze
csv_files = [
    f for f in os.listdir(folder_path)
    if f.lower().endswith(".csv")
]

# 4. Jeśli nie ma CSV – kończymy
if not csv_files:
    print("Brak plików CSV w folderze.")
    input("Enter aby zakończyć")
    exit()

files_merged = 0
rows_written = 0
header_written = False
current_id = 1

# 5. Otwieramy plik wynikowy do zapisu
with open(output_file, "w", newline="", encoding="utf-8") as out_file:
    writer = None

    # 6. Iterujemy po wszystkich plikach CSV
    for filename in csv_files:
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as in_file:
            reader = csv.reader(in_file)

            # 7. Pobieramy nagłówek
            header = next(reader, None)

            # 8. Zapisujemy nagłówek tylko raz
            if header and not header_written:
                header[0] = "id"
                writer = csv.writer(out_file)
                writer.writerow(header)
                header_written = True

            # 9. Zapisujemy wszystkie wiersze danych
            for row in reader:
                row[0] = str(current_id)
                writer.writerow(row)
                current_id += 1
                rows_written += 1

        files_merged += 1

# 10. Informacja końcowa
print(f"Połączono {files_merged} plików CSV")
print(f"Zapisano {rows_written} wierszy danych")
print(f"Plik wynikowy: {output_file}")

input("Wciśnij Enter aby zakończyć")
