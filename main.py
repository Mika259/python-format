# main.py
# Source code untuk dibaca
# made in malaysia/melayu

from datetime import datetime

def contoh_format_nombor():
    nombor = 123.456789
    nombor_terbatas = "{:.2f}".format(nombor)
    print(nombor_terbatas)  # Output: 123.46

def contoh_menyisipkan_variabel():
    nama = "John"
    usia = 25
    teks = f"Nama: {nama}, Usia: {usia}"
    print(teks)  # Output: Nama: John, Usia: 25

def contoh_penataan_teks():
    nama = "John"
    usia = 25
    teks = "{:10} {:5}".format(nama, usia)
    print(teks)  # Output: John            25

def contoh_format_tarikh():
    tarikh = datetime.now()
    format_tarikh = "{:%Y-%m-%d %H:%M:%S}".format(tarikh)
    print(format_tarikh)  # Output: 2024-07-16 12:34:56 (mengikut masa sekarang)

def contoh_format_float():
    nombor = 12345.6789
    nombor_notasi = "{:.2e}".format(nombor)
    print(nombor_notasi)  # Output: 1.23e+04

def contoh_format_peratus():
    nisbah = 0.75
    format_nisbah = "{:.2%}".format(nisbah)
    print(format_nisbah)  # Output: 75.00%

# Panggil fungsi-fungsi contoh di atas
info = "Anda boleh baca kod sumber dengan membuka file ini."
def main():
    print(\n{info}\n)
    print("Contoh 1: Memformat Nombor")
    contoh_format_nombor()
    print()

    print("Contoh 2: Menyisipkan Variabel ke dalam Teks")
    contoh_menyisipkan_variabel()
    print()

    print("Contoh 3: Mengatur Penataan Teks")
    contoh_penataan_teks()
    print()

    print("Contoh 4: Memformat Tanggal dan Waktu")
    contoh_format_tarikh()
    print()

    print("Contoh 5: Mengontrol Tampilan Floating Point")
    contoh_format_float()
    print()

    print("Contoh 6: Memformat Peratus")
    contoh_format_persatus()

if __name__ == "__main__":
    main()
