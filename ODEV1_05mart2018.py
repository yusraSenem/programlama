
##1) KAR HESAPLAMA

def start():
    print("İşletme Takip Programı")
    print("Kar hesabı için 1 \n OEE için 2 \n Adam Başı Ciro için 3  ü tuşlayınız")
    state = int(input("İşlem Numarası Giriniz"))

    if(state == 1 ):
        kar()
    elif(state==2):
        oee()
    elif(state==3):
        abc()

def kar():
    finGelir=int(input("finansman geliri:"))
    pzrGelir=int(input("pazar geliri:"))
    kiraGelir=int(input("kira geliri:"))
    toplamGelir=finGelir+pzrGelir+kiraGelir
    print("toplam gelir:",toplamGelir)
    ucret=int(input("ücret:"))
    finGider=int(input("finansman gideri:"))
    pzrGider=int(input("pazar gideri:"))
    kiraGider=int(input("kira gideri:"))
    mhsbGider=int(input("muhasebe gideri:"))
    toplamGider=ucret+finGider+pzrGider+kiraGider+mhsbGider
    print("toplam gider:",toplamGider)
    karZarar=toplamGelir-toplamGider
    if karZarar>1000:
        print("karlı bir dönem:",karZarar)
    elif karZarar==0:
        print("başabaş noktasındasınız:",karZarar)
    elif karZarar>0:
        print("karınız maliyetleri karşılamıyor:")
    else:
        print("bu dönem zarardasınız:",karZarar)
    return karZarar








##2) İŞLETMENİN EKİPMAN KULLANILABİLİRLİK ORANI


def oee():
    püs=int(input("planlanmış üretim süresi:"))
    pzd=int(input("plansız duruş:"))
    kullanilabilirlik=(püs-pzd)/püs
    print("kullanılabilirlik oranı:",kullanilabilirlik)
    scz=int(input("standart çevrim zamanı:"))
    umik=int(input("üretim miktarı:"))
    performans=(scz*umik)/(püs-pzd)
    print("performans oranı:",performans)
    sumik=int(input("sağlam ürün miktarı:"))
    tumik=int(input("toplam üretim miktarı:"))
    kalite=sumik/tumik
    print("kalite oranı:",kalite)
    oee=(kullanilabilirlik*performans*kalite)
    oeeOran=oee/100
    return ("İşletmenin Ekipman Kullanılabilirlik Oranı:",oeeOran)







##3)ADAM BAŞI CİRO HESAPLAMA

def abc():
    calisan=25
    stmik=int(input("satış miktarını giriniz:"))
    bsf=int(input("birim satış fiyatını giriniz:"))
    ciro=stmik*bsf
    print("döneme ait cironuz:",ciro)
    adamBasiCiro=ciro/calisan
    return ("Adam Başı Ciro:",adamBasiCiro)

    
while (True):
    try:
        
        start()
    except KeyboardInterrupt: 
         interruptState = input("Çıkmak için e tuşla devam etmek için c : ")
         if(interruptState == "e"):
             exit()
         elif (interruptState == "c" ):
             pass
