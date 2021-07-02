"""
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP : KEY VALUE PAIR
dictionary : Kamus

"""

kamus_indo_eng = {'anak': 'son','ayah':'father','ibu':'mother' ,'istri': 'wive'}
print(kamus_indo_eng)
print(kamus_indo_eng['anak'])
print(kamus_indo_eng['istri'])

print('data ini dikirim dari sever gojek,untuk memberikan data infor driver di sekitar  pemakai aplikasi')
data_dari_server_gojek ={
    'tanggal' : '2021-7-2',
    'driverList' : [
        {'nama':'eko','jarak':10},
        {'nama':'dwi','jarak':30},
        {'nama':'joko','jarak':40},
        {'nama':'tio','jarak':1000}
    ]
}
print(data_dari_server_gojek)
print(f"\n driver disekitar sini{data_dari_server_gojek['driverList']}")
print(f"driver disekitar sini nomor#1{data_dari_server_gojek['driverList'][0]}")
print(f"Driver terdekat {data_dari_server_gojek ['driverList'][0] ['jarak']} meter")