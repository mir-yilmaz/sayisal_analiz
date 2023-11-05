import math

x = math.pi / 5


#Cos(x) = 1 - (x^2) / 2! + (x^4) / 4!
tek_terimli = 1
iki_terimli = 1-(x**2)/math.factorial(2)

gercek_deger = math.cos(x)

tek_terimli_kesme_hatasi = gercek_deger-tek_terimli
iki_terimli_kesme_hatasi = gercek_deger-iki_terimli

print(f"tek terimli yakın değer : {tek_terimli}\n"
       f"iki terimli yakın değer : {iki_terimli}\n"
       f"gercek değer : {gercek_deger}\n"
       f"tek terimli kesme hatasi : {tek_terimli_kesme_hatasi}\n"
      f"iki terimli kesme hatasi : {iki_terimli_kesme_hatasi}\n"

      )