import sys
from PyQt4.QtGui import*
uyg=QApplication(sys.argv)
pencere=QWidget()
pencere.setWindowTitle("Yakıt Hesaplaması")
pencere.setGeometry(350, 200, 400, 200)

yol=QLabel(" <b>Gideceğiniz yol:</b>")
fiyat=QLabel("<b>Yakıt fiyatı:</b>")
yakit=QLabel("<b>100 km'de tüketilen yakıt:</b>")
tutar=QLabel("<b>Toplam Tutar:</b>")

hesapla=QPushButton("Hesapla")

way=QLineEdit()
money=QLineEdit()
benzin=QLineEdit()


butun=QVBoxLayout()
yollar=QHBoxLayout()
fiyatlar=QHBoxLayout()
yakitlar=QHBoxLayout()
tutarlar=QHBoxLayout()
hesaplama=QHBoxLayout()




yollar.addWidget(yol)
yollar.addWidget(way)
fiyatlar.addWidget(fiyat)
fiyatlar.addWidget(money)
yakitlar.addWidget(yakit)
yakitlar.addWidget(benzin)
tutarlar.addWidget(tutar)
hesaplama.addWidget(hesapla)




butun.addLayout(yollar)
butun.addLayout(fiyatlar)
butun.addLayout(yakitlar)
butun.addLayout(tutarlar)
butun.addLayout(hesaplama)



pencere.setLayout(butun)
pencere.show()
uyg.exec_
