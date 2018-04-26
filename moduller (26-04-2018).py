
#(karCiroHesabi) (modul)
def kar(gelir,gider):
    gelir=int(gelir)
    gider=int(gider)
    print("toplam işletme karı:",gelir-gider)

def adamBasiCiro(toplamCiro,toplamCalisan):
    toplamCiro=int(toplamCiro)
    toplamCalisan=int(toplamCalisan)
    print("Adam Başı Ciro:",toplamCiro/toplamCalisan)

#(birinci yöntem) modul_cagirma
from karCiroHesabi import*
kar(500,300)
adamBasiCiro(1000,300)

#(ikinci yöntem) modul_cagirma
from karCiroHesabi import*
x=(input("toplam gelirinizi girin:"))
y=(input("toplam giderinizi girin:"))
t=(input("toplam cironuzu girin:"))
z=(input("çalışan sayısını girin:"))
kar(x,y)
adamBasiCiro(t,z)


#(bilancoHesabi) (modul)
   
   
def aktif(kasa,alinanCek,bankaH,alacakSenetleri,ticariMal,binalar,tasitlar,demirbaslar):
    kasa=int(kasa)
    alinanCek=int(alinanCek)
    bankaH=int(bankaH)
    alacakSenetleri=int(alacakSenetleri)
    ticariMal=int(ticariMal)
    binalar=int(binalar)
    tasitlar=int(tasitlar)
    demirbaslar=int(demirbaslar)
    
    donenVarliklar=kasa+alinanCek+bankaH+alacakSenetleri+ticariMal
    print ("Dönen Varlıklar Toplamı:",donenVarliklar)
    
    duranVarliklar=binalar+tasitlar+demirbaslar
    print ("Duran Varlıklar Toplamı:",duranVarliklar)
    
    aktifToplami=donenVarliklar+duranVarliklar
    return aktifToplami



def pasif(bankaKredileri,saticilar,uzVadeliBankaKredileri,uzVadeliBorcSenedi,sermayeHesabi):
    bankaKredileri=int(bankaKredileri)
    saticilar=int(saticilar)
    uzVadeliBankaKredileri=int(uzVadeliBankaKredileri)
    uzVadeliBorcSenedi=int(uzVadeliBorcSenedi)
    sermayeHesabi=int(sermayeHesabi)

    
    kvyk=bankaKredileri+saticilar
    print("Kısa Vadeli Yabancı Kaynaklar Toplamı:",kvyk)
    
    uvyk=uzVadeliBankaKredileri+uzVadeliBorcSenedi
    print("Uzun Vadeli Yabancı Kaynaklar Toplamı:",uvyk)

    ozKaynaklar=sermayeHesabi
    print("Toplam Öz Kaynaklar:",ozKaynaklar)
    
    pasifToplami=kvyk+uvyk+ozKaynaklar
    return pasifToplami

    
#(modul_cagirma)
from bilancoHesabi import*
aktifler=aktif(20000,10000,5000,28000,65000,150000,25000,8000)
pasifler=pasif(42000,60000,35000,115000,59000)
if aktifler==pasifler:
    print("bilanço doğru hesaplanmıştır.","aktif toplamı:",aktifler,"pasif toplami:",pasifler)
else:
    print("bilanço yanlış hesaplanmıştır.","aktif toplamı:",aktifler,"pasif toplami:",pasifler)
	


#(grup_etkileşim_oranı) (modul)
class etkilesim:
    def __init__(self,begeniSayisi,yorumSayisi,paylasimSayisi,icerikSayisi,takipciSayisi):
        self.begeniSayisi=begeniSayisi
        self.yorumSayisi=yorumSayisi
        self.paylasimSayisi=paylasimSayisi
        self.icerikSayisi=icerikSayisi
        self.takipciSayisi=takipciSayisi
        etkilesimOrani=(((self.begeniSayisi + self.yorumSayisi + self.paylasimSayisi)/self.icerikSayisi)/self.takipciSayisi) * 100
        print("grup etkileşim oranı:",float(etkilesimOrani))
        if float(etkilesimOrani) >0.20:
            print("etkilesim oranı yüksek")
        else:
            print("etkilesim oranı düşük")

  

#(modul_cagirma)

from classla_cozum import etkilesim


ybs1=etkilesim(365000,65000,870,500,1125000)
print("ybs1 grubu:",ybs1)

ybs2=etkilesim(450000,25000,380,100,1450000)
print("ybs2 grubu:",ybs2)

ybs3=etkilesim(582000,52000,1200,650,2000000)
print("ybs3 grubu:",ybs3)






            
        
        
    







    
   

  






    

    





