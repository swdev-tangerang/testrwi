"""
Contoh komentar di dalam python
yang multi baris
"""
kamus_ind_eng = {'anak':'son', 'istri':'wife', 'ayah':'father', 'ibu':'mother'}
print(kamus_ind_eng)
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['ayah'])

print('Data ini dikiriman oleh server gojek mengenai driver yang ada di sekitar kamu')
data_dari_server_gojek = {
    'tanggal':'2020-06-12',
    'driver_list': [
        {'nama':'Eko', 'jarak': 10},
        {'nama':'Tri', 'jarak': 20},
        {'nama':'Dwi', 'jarak': 30},
        {'nama':'Catur', 'jarak': 40}
    ]
}
print(data_dari_server_gojek)
print(f"Driver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1  {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #2  {data_dari_server_gojek['driver_list'][1]}")
print(f"Driver #3  {data_dari_server_gojek['driver_list'][2]}")
print(f"Driver #4  {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat adalah {data_dari_server_gojek['driver_list'][0]['jarak']}")