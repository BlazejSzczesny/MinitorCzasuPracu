import PyQt5
import PySide2.QtCore

import mysql.connector
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QTimer
from ui_functions import *
from PyQt5.QtWidgets import QMessageBox
import time


class dataBase(MainWindow):

    def insert_image(self,result):
        print(result)
        mydb = connects()
        mycursor = mydb.cursor()
        sql =""" INSERT INTO img (photo) VALUES (%s)"""
        empPicture = convertToBinaryData(result)
        val=(empPicture,)

        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()


    def UserSerrings(self):
        zapamietaj=self.ui.radioButton.isChecked()
        zapamietaj=str(zapamietaj)
        imie=str(self.ui.lineEdit.text())
        godzinas=str(self.ui.timeEdit_3.text())
        godzinae=str(self.ui.timeEdit_4.text())
        stawka=str(self.ui.lineEdit_3.text())

        mydb = connects()
        mycursor = mydb.cursor()
        sql = '''UPDATE settingsuser SET id = %s, zapamietaj = %s, imie = %s, start = %s, koniec = %s, stawka = %s WHERE settingsuser.id = 0; '''
        val = ("NULL", zapamietaj, imie,godzinas,godzinae,stawka)
        mycursor.execute(sql, val)

        mydb.commit()
        mydb.close()



    def setDeafultValues(self):
        mydb = connects()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM settingsuser")
        myresult = mycursor.fetchall()

        if(myresult[0][1]=="True"):
            self.ui.radioButton.setChecked(True)
            self.ui.lineEdit.setText(myresult[0][2])
            self.ui.lineEdit_3.setText(myresult[0][5])
            self.ui.timeEdit_3.setTime(QTime.fromString(myresult[0][3]))
            self.ui.timeEdit_4.setTime(QTime.fromString(myresult[0][4]))
            self.ui.label_20.setText("Hello,\n"+myresult[0][2])
        mycursor.execute("SELECT * FROM img")
        myresult = mycursor.fetchall()
        print(myresult[0][0])



    def addDataToDatabase(self):
        mydb = connects()
        mycursor = mydb.cursor()
        data=self.ui.dateEdit.text()
        data=data.replace(".","-")

        godz=self.ui.label_16.text()
        godz=godz+":00"

        sql = "INSERT INTO miesiace (id,data, ilegodzin) VALUES (%s, %s, %s)"
        val = ("NULL",data, godz)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        print(self.ui.pushButton_10.text())

    def calculateStats(self):

        month=self.ui.comboBox.currentIndex()
        mydb = connects()
        mycursor = mydb.cursor()
        #mycursor.execute("SELECT SEC_TO_TIME( SUM( TIME_TO_SEC( `ilegodzin` ) ) )FROM miesiace WHERE MONTH(data) = 05")
        sql = """SELECT SEC_TO_TIME( SUM( TIME_TO_SEC( `ilegodzin` ) ) )FROM miesiace WHERE MONTH(data) = %s;"""
        val = (month+1,)

        mycursor.execute(sql, val)

        try:
            myresult = mycursor.fetchall()
            days=myresult[0][0].days*86400
            seconds=myresult[0][0].seconds
            results=days+seconds
            totalhours=str(round(results/3600))
            self.ui.label_4.setText(totalhours)
            self.ui.label_6.setText(str(round(results/3600)*15))
        except:
            label = self.ui.label_22
            label.setVisible(True)
            UIFunctions.fadeOut(self)
            self.ui.label_4.setText("0")
            self.ui.label_6.setText("0")

        mycursor = mydb.cursor()
        sql = """SELECT COUNT(*) FROM `miesiace` WHERE MONTH(data) = %s;"""
        val = (month + 1,)

        mycursor.execute(sql, val)
        #mycursor.execute("SELECT COUNT(*) FROM `miesiace` WHERE MONTH(data) = 05")
        myresult = mycursor.fetchall()
        self.ui.label_8.setText(str(myresult[0][0]))

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def connects():
    mydb = mysql.connector.connect(user='root', password='',
                                       host='127.0.0.1',
                                       database='godziny')
    return mydb
