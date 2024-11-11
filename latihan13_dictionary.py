nilai = { 'salma':89, 'Faisa':100, 'Ihsan':59,'Kamil':95}
print("Data nilai : ",nilai)

#akses nilai destionary
print (nilai["Ihsan"])

#looping semua key
for i in nilai.keys():
    kalimat = f"nilai {i} adalah \t:{nilai[i]}"
    print (kalimat)

#ubah nilai 
nilai["Ihsan"] = -10

#nambah data
nilai ["gilang"] = 86

#mengelurakan data
nilai.pop("salma")  

#menghapus data
del nilai ["gilang"]

print("----Cetak Items----")

# looping items (key & value)
for nama,score in nilai.items():
    kalimat = f"nilai {nama} adalah \t:{score}"
    print (kalimat)