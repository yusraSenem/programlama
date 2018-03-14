
####1.soru

#tsm:toplam satış miktarı
#hmm:hammadde maliyeti
#bkog:bakım onarım giderleri
#svg:sevkiyat giderleri
#sah:satın alınan hizmet giderleri
#KDC:katma değer ciro
print("katma değer ciro hesaplama")
def katmaDCiro(tsm,hmm,bkog,svg,sah):
    global KDC
    KDC=tsm-(hmm+bkog+svg+sah)
    if KDC>1000:
        print("işletme katma değer cironuz yüksek.",KDC)
    elif 500<KDC<999:
        print("işletme katma değer cironuz normal.",KDC)
    elif KDC<500:
        print("katma değer cironuz düşük.",KDC)
    return KDC
tsm=int(input("toplam satış miktarı giriniz:"))
hmm=int(input("hammadde maliyeti giriniz:"))
bkog=int(input("bakım onarım giderlerinizi giriniz:"))
svg=int(input("sevkiyat giderlerini giriniz:"))
sah=int(input("satın alınan hizmet giderleriniz:"))

katmaDegerCiro=katmaDCiro(tsm,hmm,bkog,svg,sah)

####2.soru
print("müşteri çalışma süreleri hesaplama ve karşılaştırma")
def birinciYl(cs,tms):
    global birinciYil
    birinciYil=cs/tms
    print("birinci yıla ait müşteri çalışma süresi:",birinciYil)
    return birinciYil
def ikinciYl(css,tmss):
    global ikinciYil
    ikinciYil=css/tmss
    print("ikinci yıla ait müşteri çalışma süresi:",ikinciYil)
    return ikinciYil
def karsilastir(birinciYil,ikinciYil):
    sonuc=birinciYil-ikinciYil
    if sonuc>0:
        print("müşterilerle çalışma süresi karşılaştırdığınız yıla göre bir gelişme kaydetti:",sonuc)
    elif sonuc==0:
        print("müşterilerle çalışma süresi herhangi bir değişiklik göstermemiştir:",sonuc)
    else:
        print("karşılaştırdığınız yıla göre müşterilerle çalışma süresinde bir düşüklük kaydedildi:",sonuc)
    return sonuc
birinciYil=int(input("lütfen bir yıl giriniz:"))
cs=int(input("yıla ait çaışılan süreyi giriniz:"))
tms=int(input("yıla ait toplam müşteri sayısını giriniz:"))
ikinciYil=int(input("lütfen karşılaştırmak istediğiniz yılı giriniz:"))
css=int(input("yıla ait çaışılan süreyi giriniz:"))
tmss=int(input("yıla ait toplam müşteri sayısını giriniz:"))

nCSR=birinciYl(cs,tms)
mCSR=ikinciYl(css,tmss)
kRSL=karsilastir(birinciYil,ikinciYil)
    







####3.soru

print("işletme karını hesaplama")

def ilkGlr(yg,fgl,usg):
    global ilkDonemGelir
    ilkDonemGelir=yg+fgl+usg
    print("ilk altı aydaki toplam geliriniz:",ilkDonemGelir)
    return ilkDonemGelir
def ilkGdr(cm,kd,dm):
    global ilkDonemGider
    ilkDonemGider=cm+kd+dm
    print("ilk altı aydaki toplam gideriniz:",ilkDonemGider)
    return ilkDonemGider
def ilkKar(ilkDonemGelir,ilkDonemGider):
    global ilkDonemKar
    ilkDonemKar=ilkDonemGelir-ilkDonemGider
    print("ilk altı aydaki toplam karınız:",ilkDonemKar)
    return ilkDonemKar
def sonGlr(ygg,sl,egl,usgg):
    global sonDonemGelir
    sonDonemGelir=ygg+sl+egl+usgg
    print("son altı aydaki toplam geliriniz:",sonDonemGelir)
    print()
    return sonDonemGelir
def sonGdr(cmm,kdd,bm):
    global sonDonemGider
    sonDonemGider=cmm+kdd+bm
    print("son altı aydaki toplam gideriniz:",sonDonemGider)
    return sonDonemGider
def sonKar(sonDonemGelir,sonDonemGider):
    global sonDonemKar
    sonDonemKar=sonDonemGelir-sonDonemGider
    print("son altı aydaki toplam karınız:",sonDonemKar)
    return sonDonemKar
def isletKar(ilkDonemKar,sonDonemKar):
    yilSKar=ilkDonemKar-sonDonemKar
    if yilSKar>5000:
        print("işletme çok karlı.",yilSKar)
    elif 1000<=yilSKar<=5000:
        print("işletme karı normal.",yilSKar)
    elif yilSKar<1000:
        print("işletme yeterince karda değil.",yilSKar)
    else:
        print("işletme zararda.",yilSKar)
    return yilSKar

yg=int(input("ilk altı ayın yazılım gelirini giriniz:"))
fgl=int(input("ilk altı ayın finansman gelirini giriniz:"))
usg=int(input("ilk altı ayın satış gelirini giriniz:"))
cm=int(input("ilk altı ayın çalışan maaşlarını giriniz:"))
kd=int(input("ilk altı ayın kira giderini giriniz:"))
dm=int(input("ilk altı ayın donanım maliyetini giriniz:"))
ygg=int(input("son altı ayın yazılım gelirini giriniz:"))
sl=int(input("son altı ayın sponsorluk gelirini giriniz:"))
egl=int(input("son altı ayın e-ticaret gelirini giriniz:"))
usgg=int(input("son altı ayın ürün satış gelirini giriniz:"))
cmm=int(input("son altı ayın çalışan maaşlarını giriniz:"))
kdd=int(input("son altı ayın kira giderini giriniz:"))
bm=int(input("son altı ayın bakım maliyetlerini giriniz:"))


birinciGelir=ilkGlr(yg,fgl,usg)
birinciGider=ilkGdr(cm,kd,dm)
birinciKar=ilkKar(ilkDonemGelir,ilkDonemGider)
ikinciGelir=sonGlr(ygg,sl,egl,usgg)
ikinciGider=sonGdr(cmm,kd,bm)
ikinciKar=sonKar(sonDonemGelir,sonDonemGider)
karZarar=isletKar(ilkDonemKar,sonDonemKar)


####4.soru

print("dönem başı ve dönem sonu stok hesaplama")

def donemBasi(ks=1000,ys=1000,ds=1000):
    global donemBasiStok
    donemBasiStok=ks+ys+ds
    print("dönem başı stok miktarı",donemBasiStok)
    return donemBasiStok
def girilenS(donemBasiStok,kss,yss,dss):
    global girilenStok
    girilenStok=donemBasiStok+kss+yss+dss
    print("dönem içi stok miktarı",girilenStok)
    return girilenStok
def donemSonu(girilenStok,ksy,ysy,dsy):
    global donemSonuStok
    donemSonuStok=girilenStok-(ksy+ysy+dsy)
    print("dönem sonu toplam stok miktarı:",donemSonuStok)
    return donemSonuStok
    
def ortStok(donemBasiStok,donemSonuStok):
    ortalamaStok=(donemBasiStok+donemSonuStok)/2
    print("ortalama stok miktarı:",ortalamaStok)
    return ortalamaStok

kss=int(input("stoğa eklenecek koltuk miktarı:"))
yss=int(input("stoğa eklenecek yatak miktarı:"))
dss=int(input("stoğa eklenecek dolap miktarı:"))
ksy=int(input("stoktan düşülecek koltuk miktarı:"))
ysy=int(input("stoktan düşülecek yatak miktarı:"))
dsy=int(input("stoktan düşülecek dolap miktarı:"))

ilkStok=donemBasi(ks=1000,ys=1000,ds=1000)
girilenSK=girilenS(donemBasiStok,kss,yss,dss)
sonStok=donemSonu(girilenStok,ksy,ysy,dsy)
ortalamaStok=ortStok(donemBasiStok,donemSonuStok)
    
    
    











    
    
