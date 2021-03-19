dict = {'Nama': 'Nadya Indah A',
        'Hobi1': 'Menggambar', 'Hobi2': 'Berenang', 'Hobi3': 'Traveling',
        'Sosmed1': '@nadyaarifinn_', 'Sosmed2': 'line', 'Sosmed3': '085713258855',
        'Lagu Favorit': ['To the bone', 'Resah jadi luka', 'Berlari Tanpa kaki'],
        'Makanan1': 'Nasi goreng', 'Makanan2': 'Ayam crispy', 'Makanan3': 'Bakso',}

dict['Hobi1'] = 'Menyanyi'
dict['Sosmed2'] = 'Telegram'

del dict['Makanan1']
del dict['Makanan2']

dict['Hobi4'] = 'Berkebun'

print(dict.keys())
print(dict.values())
print(dict.items())








