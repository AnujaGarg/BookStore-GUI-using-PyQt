# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewAllBooks.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Cart import Ui_ViewCartWindow
import sqlite3
pushButton_=[]
spinBox=[]
class Ui_ViewAllBooksWindow(object):
    cart_Count=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openCart)
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 5)
        row_no=self.loadBooks()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_grp = QtWidgets.QButtonGroup()
        for i in range (0,row_no+1):
            self.btn_grp.addButton(pushButton_[i]) 
        self.btn_grp.buttonClicked.connect(self.callCart)
        #pushButton_[0].clicked.connect(lambda:self.cart(0))
         
    def loadBooks(self):
        _translate = QtCore.QCoreApplication.translate
        conn=sqlite3.connect('Book.db')
        c=conn.cursor()
        c.execute("select * from books")
        book_data=c.fetchall()
        count=0
        c.execute("PRAGMA table_info(books)")
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
                self.tableWidget.insertColumn(column_no+1)
                self.tableWidget.insertColumn(column_no+2)
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
            pushButton_[row_no].setObjectName("pushButton")
            spinBox.append(QtWidgets.QSpinBox())
            pushButton_[row_no].setText(_translate("MainWindow", "Add to Cart"))
            self.tableWidget.setCellWidget(row_no,column_no+1,spinBox[row_no])
            self.tableWidget.setCellWidget(row_no,column_no+2,pushButton_[row_no])
        '''for i in range(0,row_no+1):
            pushButton_[i].clicked.connect(self.cart,i)'''
        vertical=[]
        for i in range(0,row_no+1):
            vertical.append("S.No."+str(i+1))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setVerticalHeaderLabels(vertical)
        for i in range(0,row_no+1):
            self.tableWidget.verticalHeaderItem(i).setFont(font)
            if(i<column_no+1):
                self.tableWidget.horizontalHeaderItem(i).setFont(font)
        #self.tableWidget.item(0,4).setFont(font)
        #self.tableWidget.cellClicked.connect(self.cart)
        conn.close()
        return row_no
    def callCart(self):
        i=self.tableWidget.currentRow()
        self.cart(i)
        
    def cart(self,i):
        _translate = QtCore.QCoreApplication.translate
        #print(spinBox[i].text())
        if(spinBox[i].text()=="0"):
            self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">*</span><span style=\" color:#008080;\">Quantity of Books must be at least 1 to be added to Cart<br/></span></p></body></html>"))
        else:
            _translate = QtCore.QCoreApplication.translate
            self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#008080;\">Added to Cart<br/></span></p></body></html>"))
            Cart=sqlite3.connect("Cart.db")
            Book=sqlite3.connect("Book.db")
            v=Cart.cursor()
            c=Book.cursor()
            record=self.tableWidget.item(i,1).text()
            quantity=spinBox[i].text()
            record=record.replace("'","''")
            c.execute("select Price from books where title='"+record+"'")
            b_price=c.fetchone()
            total=b_price[0]*int(quantity)
            c.execute("select * from books where title like'%"+record+"%';")
            item=[]
            item.append(c.fetchone())
            b_title=item[0][1]
            #item[0][1]=item[0][1].replace("'","''") //item is a list and item[0][1] is a part of tuple in the list, and item assignment not allowed in tuple.
            b_title=b_title.replace("'","''")
            v.execute("select BookID from viewCart where title like'%"+b_title+"%';")
            b_id=v.fetchone()
            if(b_id==None):
                v.execute("insert into viewCart(BookID,Title,Author,Price,Category,Quantity,Total_Cost) values(?,?,?,?,?,?,?)",(item[0][0],item[0][1],item[0][2],item[0][3],item[0][4],quantity,total))
            else:
                v.execute("update viewCart set BookID=?,Title=?,Author=?,Price=?,Category=?,Quantity=?,Total_Cost=? where title like'%"+record+"%'",(item[0][0],item[0][1],item[0][2],item[0][3],item[0][4],quantity,total))
            Cart.commit()
            Cart.close()
            Book.commit()
            Book.close()

    def openCart(self):
        if(self.cart_Count==0):
            self.viewCart=QtWidgets.QMainWindow()
        self.ui=Ui_ViewCartWindow()
        self.ui.setupUi(self.viewCart)
        self.viewCart.show()
        self.cart_Count=self.cart_Count+1
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Books"))
        self.pushButton.setText(_translate("MainWindow", "View Cart"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewAllBooksWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewAllBooksWindow()
    ui.setupUi(ViewAllBooksWindow)
    ViewAllBooksWindow.show()
    sys.exit(app.exec_())

