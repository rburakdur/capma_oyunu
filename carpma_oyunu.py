#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import randint
z = 1
print("+"*60)
print("\t\tÇarpma Oyununa Hoşgeldiniz")
print("+"*60)
print("""
Lütfen Zorluk Seçiniz....
----------------------------------

1. Kolay 
2. Orta Oyun
3. Zor Oyun

----------------------------------

Çıkış için "q" ya basınız...

""")
liste = ['q','1','2','3']
def carpim(i,j,r):
    global z
    if i*j != r:
        print("Cevabınız yanlış. Doğru cevap: ",i*j)
    else:
        z += 1
        print("Tebrikler cevabınız Doğru...")

secim = input(">>")
while True:

    if secim in liste:
        secim = secim
    else:
        print("Yanlış Tuşa Bastınız!")
        secim = input(">>")

    if secim == 'q':
        print("Çıkış Yapılıyor...")
        break

    elif secim == '1':
        while z <= 5:
            i = int(randint(1,5))
            j = int(randint(1,5))
            print("{} X {} = ?".format(i,j))
            r = int(input(">>"))
            carpim(i,j,r)
        print("5 doğru cevap verdiniz. Lütfen zorluğu arttırın.")
        z = 1
        secim = input(">>")

    elif secim == '2':
        while z <= 5:
            i = int(randint(5,10))
            j = int(randint(5,10))
            print("{} X {} = ?".format(i,j))
            r = int(input(">>"))
            carpim(i,j,r)

        print("5 doğru cevap verdiniz. Lütfen zorluğu arttırın.")
        z = 1
        secim = input(">>")

    elif secim == '3':
        while z <= 5:
            i = int(randint(10,15))
            j = int(randint(10,15))
            print("{} X {} = ?".format(i,j))
            r = int(input(">>"))
            carpim(i,j,r)

        print("Çarpma Oyunu'nu Başarı ile tamamladınız...\n\n\nÇıkış için 'q' ya basınız.")
        secim = input(">>")
        while secim == 'q':
            if secim != "q":
                print("Oyunu zaten bitirdiniz. Lütfen 'q'ya basınız.")






