# Konstruksi Dasar Python
# SEQUENTIAL : eksekusi berurutan
print('Hello world')
print('by Eko')
print('Tanggal 10 Juni 2020')
print('---'*3)

# PERCABANGAN : eksekusi terpilih
ingin_cepat = True
if ingin_cepat:
    print('Jalan lurus saja')
else:
    print('Jalan lain')

# Perulangan
jumlah_anak = 4
for index_anak in range(1, jumlah_anak+1):
    print(f'Halo anak {index_anak}')
