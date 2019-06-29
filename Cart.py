# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cart.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
pushButton_=[]
pushButton=[]
spinBox=[]
class Ui_ViewCartWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("N:/Python Programs/Module 6- Develop GUI with PyQt/icon-1415760__340.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        row_no=self.loadCart()
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_grp = QtWidgets.QButtonGroup()
        for i in range (0,row_no+1):
            self.btn_grp.addButton(pushButton_[i]) 
        self.btn_grp.buttonClicked.connect(self.callCart)

        self.btn_grp1 = QtWidgets.QButtonGroup()
        for i in range (0,row_no+1):
            self.btn_grp1.addButton(pushButton[i])
        self.btn_grp1.buttonClicked.connect(self.removeItem)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadCart(self):
        _translate = QtCore.QCoreApplication.translate
        conn=sqlite3.connect('Cart.db')
        c=conn.cursor()
        c.execute("select * from viewCart")
        book_data=c.fetchall()
        count=0
        c.execute("PRAGMA table_info(viewCart)")
        record=c.fetchall()
        for row_no,row_data in enumerate(book_data):
            self.tableWidget.insertRow(row_no)
            count=count+1
            if(count==1):
                for column_no,data in enumerate(row_data):
                    self.tableWidget.insertColumn(column_no)
                horiz=[]
                for i in range(0,column_no+1):
                    horiz.append(record[i][1])
                horiz.append('')
                horiz.append('')
                horiz.append('')
                self.tableWidget.insertColumn(column_no+1)
                self.tableWidget.insertColumn(column_no+2)
                self.tableWidget.insertColumn(column_no+3)
                self.tableWidget.setHorizontalHeaderLabels(horiz)
            for column_no,data in enumerate(row_data):
                _translate = QtCore.QCoreApplication.translate
                self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            pushButton_.append(QtWidgets.QPushButton())
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            pushButton_[row_no].setFont(font)
            pushButton_[row_no].setObjectName("pushButton_")
            pushButton.append(QtWidgets.QPushButton())
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            pushButton[row_no].setFont(font)
            pushButton[row_no].setObjectName("pushButton")
            spinBox.append(QtWidgets.QSpinBox())
            pushButton_[row_no].setText(_translate("MainWindow", "Add to Cart"))
            pushButton[row_no].setText(_translate("MainWindow", "Remove Item"))
            self.tableWidget.setCellWidget(row_no,column_no+1,spinBox[row_no])
            self.tableWidget.setCellWidget(row_no,column_no+2,pushButton_[row_no])
            self.tableWidget.setCellWidget(row_no,column_no+3,pushButton[row_no])
        vertical=[]
        for i in range(0,row_no+1):
            vertical.append("S.No."+str(i+1))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setVerticalHeaderLabels(vertical)
        for i in range(0,row_no+1):
            self.tableWidget.verticalHeaderItem(i).setFont(font)
        for i in range(0,column_no+1):
            self.tableWidget.horizontalHeaderItem(i).setFont(font)
        #self.tableWidget.item(0,4).setFont(font)
        #self.tableWidget.cellClicked.connect(self.cart)
        conn.close()
        return row_no
    def callCart(self):
        i=self.tableWidget.currentRow()
        self.cart(i)

    def removeItem(self):
        i=self.tableWidget.currentRow()
        Cart=sqlite3.connect("Cart.db")
        v=Cart.cursor()
        record=self.tableWidget.item(i,1).text()
        record=record.replace("'","''")
        v.execute("delete from viewCart where title like'%"+record+"%'")
        #self.tableWidget.removeCellWidget(i,7)
        del pushButton[i]
        del pushButton_[i]
        del spinBox[i]
        self.tableWidget.removeRow(i)
        Cart.commit()
        Cart.close()
        
    def cart(self,i):
        _translate = QtCore.QCoreApplication.translate
        if(spinBox[i].text()=="0"):
            self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">*</span><span style=\" color:#008080;\">Quantity of Books must be at least 1 to be added to Cart<br/></span></p></body></html>"))
        else:
            _translate = QtCore.QCoreApplication.translate
            self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#008080;\">Added to Cart<br/></span></p></body></html>"))
            Cart=sqlite3.connect("Cart.db")
            v=Cart.cursor()
            record=self.tableWidget.item(i,1).text()
            quantity=spinBox[i].text()
            record=record.replace("'","''")
            v.execute("select Price from viewCart where title='"+record+"'")
            b_price=v.fetchone()
            total=b_price[0]*int(quantity)
            v.execute("update viewCart set Quantity=?,Total_Cost=? where title like'%"+record+"%'",(quantity,total))
            self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(quantity))
            self.tableWidget.setItem(i,6,QtWidgets.QTableWidgetItem(str(total)))
            Cart.commit()
            Cart.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#008080;\">CART</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewCartWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewCartWindow()
    ui.setupUi(ViewCartWindow)
    ViewCartWindow.show()
    sys.exit(app.exec_())

