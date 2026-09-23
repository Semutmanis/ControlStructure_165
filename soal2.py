angka1=int(input("masukan angka pertama: "))
angka2=int(input("masukan angka kedua: "))
angka3=int(input("masukan angka ketiga: "))

if angka1>angka2 and angka1>angka3:
  print("angka pertama adalah yang terbesar")
elif angka2>angka1 and angka2>angka3:
  print("angka pertama adalah yang terbesar")
elif angka3>angka1 and angka3>angka2:
  print("angka pertama adalah yang terbesar")
else:
  print("tidak ada angka yang sama!!!")