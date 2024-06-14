mobil = ('Porsche', 4200, 0.7 , 250 )
merk, cc , berat , top_speed = mobil
print(mobil[0])
print(mobil[:2])
print(mobil[2:])
print(mobil.index(4200))
print(0.7 in mobil)
print('mobil {} memiliki berat {} ton, kapasitas {} cc dan top speed {} km/jam'.
format(merk,berat,cc,top_speed)) 