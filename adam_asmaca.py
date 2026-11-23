
import random
kelimeler=["dexter","tahtoyunlari","sürekidizi","vikings","dark","lost","lucifer"]
kelime=random.choice(kelimeler)
doğru_harfler=[]
yanliş_harfler=[]
can=5
while True:
    print("\nkelime:",end="")
    bulunan_harf=0
    for harf in kelime:
        if harf in doğru_harfler:
            print(harf,end=" ")
            bulunan_harf+=1
        else:
            print("_",end=" ")
    print("kalan can:",can)
    print("girilen yanliş harfler:",yanliş_harfler)
    if bulunan_harf == len(kelime):
        print("Tebrikler kelimeyi dogru buldunuz!✅")
        break
    harf=input("\nbir harf giriniz:(cikmak için (q) ya basiniz!!)")
    if harf =="q":
        print("oyundan cikiliyor!!")
        break
    if len(harf) !=1:
        print("sadece bir harf giriniz!")
        continue
    if harf in doğru_harfler or harf in yanliş_harfler:
        print("bu harfi daha önce girdiniz!!!")
        continue
    if harf in kelime:
        print("doğru harf")
        doğru_harfler.append(harf)
    else:
        print("yanliş harf")
        yanliş_harfler.append(harf)
        can-=1
        if can == 1:
            print("son canin kaldi:",can)
    if can<=0:
        print("caniniz bitmiştir tekrar denyiniz:")
        break  
