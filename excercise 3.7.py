#Contoh cara menghapus pada Dictionary Python

dict = {'Name':'Zara', 'Age': 7, 'Class': 'Frst'}

del dict['Name'] #Hapus entri dengan key'Name'
dict.clear() #hapus semua entri di dict
del dict #hapus dictionary yang sudah ada

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
