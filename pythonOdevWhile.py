#1.soru
sm=500
bsf=20
ciro=5000
i=1#ay
while True:
    print(i)
    sm=sm+200
    bsf=bsf+10
    ciro=sm*bsf
    if (ciro>500000):
        print(i,"ay sonra ciro 500.000'den fazla oldu. cironuz:",ciro)
        break
    i=i+1#ay


#2.soru

gcyilstk=10000
i=1#ay
while True:
    gcyilstk=gcyilstk+(100-500)
    if (gcyilstk==0):
        print(i,"ay sonra stok miktarı sıfırlanır.gcyilstk:",gcyilstk)
        break
    i=i+1#ay

#3.soru

i=""
kalan=0
while (i!=0):
    
    i=int(input("bir sayı giriniz: not:çıkmak isterseniz 0'a basın."))
    if i==0:
        print("program sonlandırıldı.")
    else:
        j=(i%3)
        print("3 ile bölümünden kalan:",j)
        kalan=kalan+j
        print("kalan toplamı:",kalan)
        


#4.soru

print("YBS Firması")
cls=50
hfS=40#saat/hafta
yvm=90#tl
msuc=yvm*(10/100)#tl
hfms=""
while True:
    hfms=int(input("haftalık mesai saati:"))
    if (4*hfms>22):
        print("belirlenen mesai saati dolmuştur.")
        break
    aylms=(4*hfms*msuc)
    print("aylık mesai ücreti:",aylms,"TL")
    odnnmaas=(cls*30*yvm)+aylms
    print("aylık ödenen toplam personel maaşı:",odnnmaas,"TL")       
    if (4*hfms>22):
        print("Aylık belirlenen mesai saatini aştınız!")
        break
    

#5.soru


print("tekstil firması pantolon üretimi")
gun=200
defo=0
toplam=0
i=1#gün
while True:
    defo=int(input("defolu ürün sayısı:"))
    if defo>gun*(20/100):
        print("uyarı! günlük defolu ürün sayısı belirlenen sınırı aştı.")
        break
    toplam=toplam+defo
    print(i,"günlük defolu ürün sayısı:",toplam)
    i=i+1
        
    


