#1
def konversi_suhu(value, suhu):
    if suhu == 'C':
        # Mengonversi Celsius ke Fahrenheit
        return (value * 9/5) + 32
    elif suhu == 'F':
        # Mengonversi Fahrenheit ke Celcius
        return (value - 32) * 5/9
    else:
        raise ValueError("Suhu tidak valid. Gunakan"\
            " 'C' untuk Celsius atau 'F' untuk Fahrenheit.")
print(konversi_suhu(200, 'C'))
print(konversi_suhu(38, 'F'))

#2
luas_lingkaran = lambda jari_jari : 3.14 * (jari_jari ** 2)

n = float(input("Masukkan jari-jari lingkaran: "))

print("Luas lingkaran dengan jari jari", n, "adalah: ", luas_lingkaran(n))