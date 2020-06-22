# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Visitor Check_Out.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QTextCursor
import sys
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox
import pdf, time

class Ui_MainWindow(object):

    def checkTheft(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="vishal2098",
            database="CRIMINAL"
        )

        self.notifyTheft = self.centralwidget
        mycur = mydb.cursor()

        numPlate = self.textEdit.toPlainText()

        self.NumPlate = ''
        for i in numPlate:
            if i != ' ':
                self.NumPlate += i
        print(self.NumPlate)
        checkQuerry = f"SELECT * FROM CRIMINALS WHERE NUMBER_PLATE = '{self.NumPlate}'"
        mycur.execute(checkQuerry)

        myresult = mycur.fetchall()
        print(myresult)

        if len(myresult) == 0:
            result = "Not found in theft record"
            print(result)
            QMessageBox.about(self.notifyTheft, 'Theft Status:', result)
        else:
            theftDetails = ''
            for row in myresult:
                for detail in row:
                    theftDetails += detail + ' '
            print(myresult[0][0], myresult[0][1], myresult[0][2])
            QMessageBox.about(self.notifyTheft, 'Theft Status:', theftDetails)
            QMessageBox.about(self.notifyTheft, 'Export PDF:', "PDF Ready")
            pdf.ExportPdf(myresult[0][0], myresult[0][1], myresult[0][2])
            mydb.close()

    def searchPrevVisitor(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="vishal2098",
            database="visitor"
        )

        mycur = mydb.cursor()
        print('connected')
        ids = self.textEdit_2.toPlainText()
        ids = ids.split(',')
        r = 0
        print(ids)
        for id in ids:
            print(id)
            search = f"select * from visitors where id = '{id}'"
            mycur.execute(search)

            myresult = mycur.fetchall()
            for row in myresult:
                in_veh_no = row[1]
                in_time = row[2]
                name = row[5]
                plot_no = row[4]
                print(in_veh_no, in_time, name, plot_no)
                self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(name))
                self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(plot_no))
                self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(in_veh_no))
                self.tableWidget.setItem(r, 3, QtWidgets.QTableWidgetItem(in_time))
            r +=1
        mydb.close()

    def checkOut(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="vishal2098",
            database="visitor"
        )

        mycur = mydb.cursor()
        print('connected')

        phoneNos = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        names = [self.tableWidget.item(row, 1).text() for row in range(self.tableWidget.rowCount())]
        plotNos = [self.tableWidget.item(row, 2).text() for row in range(self.tableWidget.rowCount())]

        print(phoneNos)
        print(names)
        print(plotNos)

        phoneNo, name, plotNo = [], [], []

        for i in phoneNos:
            if i != ' ':
                phoneNo.append(i)
        for i in names:
            if i != ' ':
                name.append(i)
        for i in plotNos:
            if i != ' ':
                plotNo.append(i)
        NumPlate = ''
        numPlate = self.textEdit.toPlainText()
        for i in numPlate:
            if i != ' ':
                NumPlate += i





    def setupUi(self, MainWindow, NumPlate):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 913)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        MainWindow.setWindowIcon(QtGui.QIcon("securitize.png"))
        self.tableWidget.setGeometry(QtCore.QRect(120, 440, 651, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setPixmap(QPixmap('Plates\\imgPlate.png'))
        self.img.setGeometry(120, 80, 950, 101)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 190, 411, 51))
        self.textEdit.setObjectName("textEdit")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 740, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.checkOut)

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 340, 471, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit_2.setFont(font)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 340, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.searchPrevVisitor)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 190, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.checkTheft)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, NumPlate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, NumPlate):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Securitize"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Plot No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "In Vehicle No"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "In Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Out Time"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("MainWindow", " "))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Visitor Check Out"))
        # self.label_2.setText(_translate("MainWindow", "image"))
        self.label_3.setText(_translate("MainWindow", "Out Vehicle No."))

        # Corrected NumPlate:

        correctNumPlate_Text = ''
        l = [n + ' ' for n in NumPlate]
        numPlate = ''
        for c in l:
            numPlate += c

        self.textEdit.setText(_translate("MainWindow", numPlate))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)

        self.pushButton.setText(_translate("MainWindow", "Check Out"))
        self.label_4.setText(_translate("MainWindow", "Latest ID/ Phone No"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Check Theft"))

def checkOut(NumPlate):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, NumPlate)
    MainWindow.show()
    sys.exit(app.exec_())
