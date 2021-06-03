# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\桌面\python\PyQt5\科技园登记系统\信息统计界面搭建\resource\UI\register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image:url(:/register/images/register_background.jpg);\n"
"}")
        self.main_menue_btn = QtWidgets.QPushButton(Form)
        self.main_menue_btn.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.main_menue_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    background-color: rgb(182, 87, 98);\n"
"    border: 2px solid rgb(141, 58, 84);\n"
"    color: white\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid rgb(255, 214, 173);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(255, 214, 173);\n"
"}")
        self.main_menue_btn.setCheckable(True)
        self.main_menue_btn.setObjectName("main_menue_btn")
        self.exit_menue_btn = QtWidgets.QPushButton(Form)
        self.exit_menue_btn.setGeometry(QtCore.QRect(10, 90, 41, 41))
        self.exit_menue_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    background-color: rgb(182, 87, 98);\n"
"    border: 2px solid rgb(141, 58, 84);\n"
"    color: white\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid rgb(255, 214, 173);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(255, 214, 173);\n"
"}")
        self.exit_menue_btn.setCheckable(False)
        self.exit_menue_btn.setObjectName("exit_menue_btn")
        self.reset_menue_btn = QtWidgets.QPushButton(Form)
        self.reset_menue_btn.setGeometry(QtCore.QRect(70, 70, 41, 41))
        self.reset_menue_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    background-color: rgb(182, 87, 98);\n"
"    border: 2px solid rgb(141, 58, 84);\n"
"    color: white\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid rgb(255, 214, 173);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(255, 214, 173);\n"
"}")
        self.reset_menue_btn.setCheckable(False)
        self.reset_menue_btn.setObjectName("reset_menue_btn")
        self.about_menue_btn = QtWidgets.QPushButton(Form)
        self.about_menue_btn.setGeometry(QtCore.QRect(90, 10, 41, 41))
        self.about_menue_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    background-color: rgb(182, 87, 98);\n"
"    border: 2px solid rgb(141, 58, 84);\n"
"    color: white\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid rgb(255, 214, 173);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(255, 214, 173);\n"
"}")
        self.about_menue_btn.setCheckable(False)
        self.about_menue_btn.setObjectName("about_menue_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 240, 271, 346))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color: rgb(223, 223, 223);\n"
"font: 12pt \"楷体\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_le.setStyleSheet("background-color: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid lightgray;")
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(223, 223, 223);\n"
"font: 12pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_le.setStyleSheet("background-color: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid lightgray;")
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(223, 223, 223);\n"
"font: 12pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.confirm_pwd_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.confirm_pwd_le.setStyleSheet("background-color: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid lightgray;")
        self.confirm_pwd_le.setClearButtonEnabled(True)
        self.confirm_pwd_le.setObjectName("confirm_pwd_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirm_pwd_le)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.register_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(247, 164, 123);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(234, 156, 116);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(202, 134, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: rgb(184, 184, 184);\n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.register_btn)
        self.label_hint = QtWidgets.QLabel(Form)
        self.label_hint.setGeometry(QtCore.QRect(220, 200, 72, 15))
        self.label_hint.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_hint.setText("")
        self.label_hint.setObjectName("label_hint")
        self.layoutWidget.raise_()
        self.exit_menue_btn.raise_()
        self.reset_menue_btn.raise_()
        self.about_menue_btn.raise_()
        self.main_menue_btn.raise_()
        self.label_hint.raise_()

        self.retranslateUi(Form)
        self.main_menue_btn.clicked['bool'].connect(Form.show_hide_menue)
        self.about_menue_btn.clicked.connect(Form.about)
        self.reset_menue_btn.clicked.connect(Form.reset)
        self.exit_menue_btn.clicked.connect(Form.exit_pane)
        self.register_btn.clicked.connect(Form.check_register)
        self.account_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.password_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.confirm_pwd_le.textChanged['QString'].connect(Form.enable_register_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menue_btn.setText(_translate("Form", "主题"))
        self.exit_menue_btn.setText(_translate("Form", "退出"))
        self.reset_menue_btn.setText(_translate("Form", "重置"))
        self.about_menue_btn.setText(_translate("Form", "关于"))
        self.layoutWidget.setStyleSheet(_translate("Form", "color: rgb(223, 223, 223);\n"
"font: 12pt \"楷体\";"))
        self.label.setText(_translate("Form", "账    号："))
        self.label_2.setText(_translate("Form", "密    码："))
        self.label_3.setText(_translate("Form", "确认密码："))
        self.register_btn.setText(_translate("Form", "注      册"))
import images_rc
