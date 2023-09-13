konu = "\033[97mÇOK AMAÇLI İŞLEM MAKİNESİ"

print("\033[31m╔"+"═"*(len(konu)-3)+"╗")   
print("║"+" "+konu+" "+"\033[31m║")  
print("╠"+"═"*(len(konu)-3)+"╣\033[0m")

print("\033[31m║\033[0m"+" "+"\033[97m1-DÖRT İŞLEM"+"              "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                 "+"\033[31m║")
print("\033[31m║"+" "+"                          "+"║")
print("\033[31m╚"+"═"*(len(konu)-3)+"╝\033[0m")

secim = input("Çok amaçlı menüden hangi işlemi yapmak istersiniz?")

if secim == "1" :
    islem = "\033[97mDÖRT İŞLEM"
    print("\033[31m╔"+"═"*(len(konu)-4)+"╗")   
    print("║"+"        "+islem+"        "+"\033[31m║")  
    print("╠"+"═"*(len(konu)-4)+"╣\033[0m")
    print("\033[31m║\033[0m"+" "+"\033[97m1-TOPLAMA"+"                "+"\033[31m║")
    print("\033[31m║\033[0m"+" "+"\033[97m1-ÇIKARMA"+"                "+"\033[31m║")
    print("\033[31m║\033[0m"+" "+"\033[97m1-ÇARPMA"+"                 "+"\033[31m║")
    print("\033[31m║\033[0m"+" "+"\033[97m1-BÖLME"+"                  "+"\033[31m║")
    print("\033[31m║"+" "+"                         "+"║")
    print("\033[31m╚"+"═"*(len(konu)-4)+"╝\033[0m")
    dortislem = input("Hangi işlemi yapmak istersiniz?")

    if secim == "1" : 
        toplanacaksayi = int(input("Kaç tane sayı toplamak istiyorsunuz?"))
        for k in range(toplanacaksayi) :
            toplam = 0
            sayi1 = int(input("Toplamak istediğiniz sayıları giriniz? :"))
            for sayi1 in range (0, (sayi1 + 1)) : 
                toplam = toplam + sayi1
            print(toplam)

