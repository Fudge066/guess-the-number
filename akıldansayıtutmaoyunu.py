from random import randint

rand = randint(1, 100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ila 100 arasında bir sayı giriniz ('0' çıkış): "))
    
    if sayi == 0:
        print("Oyundan çıkış yapılıyor...")
        break
    elif sayi > rand:
        print("Daha küçük bir sayı giriniz.")
    elif sayi < rand:
        print("Daha büyük bir sayı giriniz.")
    elif sayi == rand:
        print("Tebrikler {}. denemede doğru sayıya ulaştınız! ".format(sayac))
        break