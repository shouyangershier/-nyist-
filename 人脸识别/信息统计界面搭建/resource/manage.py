# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\桌面\python\PyQt5\科技园登记系统\信息统计界面搭建\resource\UI\manage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(954, 699)
        Form.setMinimumSize(QtCore.QSize(954, 699))
        Form.setMaximumSize(QtCore.QSize(954, 699))
        Form.setStyleSheet("")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 954, 701))
        self.listView.setStyleSheet("background-image: url(:/manage/images/2.jpg);")
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import images_rc
