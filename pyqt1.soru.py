from PyQt4.QtGui import*
from PyQt4.QtCore import*

class tabloyaAktarma(QDialog):
    def __init__(self,ebeveyn=None):
        
        super(tabloyaAktarma,self).__init__(ebeveyn)
        self.initUI()

    def initUI(self):
        self.setGeometry(500,300,400,200)
        self.setWindowTitle("Tablo")
    
        grid=QGridLayout()
        self.setLayout(grid)

        veri={"Adı":["Can","Semih","Büşra"],
              "ZBolum":["YBS","YBS","İktisat"],
              "Soyadı":["Aydın","Yarar","Demirgüreşçi"],
              }

        table=QTableWidget(self)
        table.setRowCount(3)
        table.setColumnCount(3)

        liste=[]
        for n, key in enumerate(sorted(veri.keys())):
            liste.append(key)
            for m, item in enumerate(veri[key]):
                yeniItem=QTableWidgetItem(item)
                table.setItem(m,n,yeniItem)

        
        table.setHorizontalHeaderLabels(liste)
       
        

        grid.addWidget(table,0,0)

        self.show()




uyg=QApplication([])
pencere=tabloyaAktarma()
pencere.show()
uyg.exec_()

