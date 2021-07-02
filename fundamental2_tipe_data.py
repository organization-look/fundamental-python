# TIPE DATA SKALAR  = SEDERHANA
print('\n  TIPE DATA SEDERHANA')
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'joko'
anak4 = 'tio'
print(f'hallo {anak1}')
print(f'hallo {anak2}')

#TIPE DATA  ARRAY
print('\n ARRAY/LIST')
anak = ['eko', 'dwi', 'joko', 'tio']
print(anak)

# menambah nilai dalam array
anak.append('tika')
print(anak)

print('\n SAPA SATU ANAK')
print(f'hai {anak[1]}')

print('\n SAPA SEMUA ANAK :CARA MUDAH')
for a in (anak):
    print(f'{a}')


print('\n SAPA SEMUA ANAK :CARA RIBET')
for a in range (0,len(anak)):
    print(f'hai ke{a+1}. {anak[a]}')

