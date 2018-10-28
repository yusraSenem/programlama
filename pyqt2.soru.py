##Ortalama personel sayısı (100+140)/2 yani 120'dir.
##
##Personel devir oranı için Ocak-Aralık 2013 dönemi içinde toplam işten ayrılan personel sayısı gereklidir. 12 personel işten ayrıldı diyelim.
##Personel devir oranı (12/120).100 yani %10'dur.
from PyQt4.QtGui import*
from PyQt4.QtCore import*

class personelDevirHizi(QDialog):
    def __init__(self,ebeveyn=None):
        
        super(personelDevirHizi,self).__init__(ebeveyn)
    
        grid=QGridLayout()

        grid.addWidget(QLabel("Dönem seçiniz:"),0,0)
        self.yil=QSpinBox()
        self.yil.setRange(1997,2020)
        self.yil.setValue(2000)
        grid.addWidget(self.yil,0,1)
    
    
        grid.addWidget(QLabel("Dönem başı personel sayısı:"),1,0)
        self.donemBasiPersonel=QLineEdit()
        grid.addWidget(self.donemBasiPersonel,1,1)

        grid.addWidget(QLabel("Dönem sonu personel sayısı:"),2,0)
        self.donemSonuPersonel=QLineEdit()
        grid.addWidget(self.donemSonuPersonel,2,1)

        grid.addWidget(QLabel("ortalama personel sayısı:"),3,0)

        self.ortalamaPersonel=QLabel("")
        grid.addWidget(self.ortalamaPersonel,3,1)

        grid.addWidget(QLabel("Dönem içinde işten ayrılan personel sayısı:"),4,0)
        self.istenAyrilan=QLineEdit()
        grid.addWidget(self.istenAyrilan,4,1)


        hesaplaDugme=QPushButton("Hesapla")
        grid.addWidget(hesaplaDugme,5,1)
        self.connect(hesaplaDugme,SIGNAL("pressed()"),self.personelDevir)
    
        grid.addWidget(QLabel("Personel Devir Oranı:"),6,0)
        self.devir=QLabel("")
        grid.addWidget(self.devir,6,1)

                

        self.setLayout(grid)
        self.setWindowTitle("Personel Devir Oranı Hesaplama")
        self.resize(250,150)
    def personelDevir(self):
        dbp=int(self.donemBasiPersonel.text())
        dsp=int(self.donemSonuPersonel.text())
        yillar=int(self.yil.text())
        iap=int(self.istenAyrilan.text())
        ops=(dbp+dsp)/2
        devirOran=(iap/ops)*100
        self.ortalamaPersonel.setText("<font color='blue'><b>%0.1f</b></font>"%ops)
        self.devir.setText("<font color='blue'><b>%0.1f</b></font>"%devirOran)

uyg=QApplication([])
pencere=personelDevirHizi()
pencere.show()
uyg.exec_()
    
    
    
