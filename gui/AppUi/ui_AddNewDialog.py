# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(484, 96)
        Dialog.setMinimumSize(QSize(484, 96))
        Dialog.setMaximumSize(QSize(484, 96))
        font = QFont()
        font.setFamily(u"Nazanin")
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.url_le = QLineEdit(self.groupBox)
        self.url_le.setObjectName(u"url_le")
        self.url_le.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url_le.sizePolicy().hasHeightForWidth())
        self.url_le.setSizePolicy(sizePolicy)
        self.url_le.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamily(u"Nazanin")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.url_le.setFont(font1)
        self.url_le.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.url_le)

        self.url_submit = QPushButton(self.groupBox)
        self.url_submit.setObjectName(u"url_submit")
        self.url_submit.setMinimumSize(QSize(0, 35))
        self.url_submit.setFont(font)

        self.horizontalLayout_2.addWidget(self.url_submit)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add New", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u0627\u0641\u0632\u0648\u062f\u0646 \u0622\u062f\u0631\u0633 \u062c\u062f\u06cc\u062f", None))
        self.url_le.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0622\u062f\u0631\u0633 \u0645\u0648\u0631\u062f \u0646\u0638\u0631 \u062e\u0648\u062f \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f", None))
        self.url_submit.setText(QCoreApplication.translate("Dialog", u"\u0627\u0641\u0632\u0648\u062f\u0646", None))
    # retranslateUi

