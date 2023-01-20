# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloadFileDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 362)
        font = QFont()
        font.setFamily(u"Nazanin")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(MainWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.insertNewTab = QWidget()
        self.insertNewTab.setObjectName(u"insertNewTab")
        self.gridLayout_2 = QGridLayout(self.insertNewTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.insertNewTab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pending_list = QTableWidget(self.groupBox)
        if (self.pending_list.columnCount() < 2):
            self.pending_list.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.pending_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.pending_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.pending_list.setObjectName(u"pending_list")
        font1 = QFont()
        font1.setFamily(u"Nazanin")
        font1.setBold(False)
        font1.setWeight(50)
        self.pending_list.setFont(font1)
        self.pending_list.setLayoutDirection(Qt.LeftToRight)
        self.pending_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pending_list.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_4.addWidget(self.pending_list)


        self.gridLayout_2.addWidget(self.groupBox, 0, 2, 2, 1)

        self.groupBox_2 = QGroupBox(self.insertNewTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.clear_btn = QPushButton(self.frame_2)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setEnabled(False)
        self.clear_btn.setGeometry(QRect(170, 10, 30, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy1)
        self.clear_btn.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"../icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon)
        self.stop_btn = QPushButton(self.frame_2)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setEnabled(False)
        self.stop_btn.setGeometry(QRect(130, 10, 30, 30))
        sizePolicy1.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy1)
        self.stop_btn.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"../icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon1)
        self.stop_btn.setIconSize(QSize(20, 20))
        self.download_btn = QPushButton(self.frame_2)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setEnabled(False)
        self.download_btn.setGeometry(QRect(50, 10, 30, 30))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(30)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.download_btn.sizePolicy().hasHeightForWidth())
        self.download_btn.setSizePolicy(sizePolicy2)
        self.download_btn.setMinimumSize(QSize(30, 30))
        self.download_btn.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"../icons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.download_btn.setIcon(icon2)
        self.pause_btn = QPushButton(self.frame_2)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setEnabled(False)
        self.pause_btn.setGeometry(QRect(90, 10, 30, 30))
        sizePolicy1.setHeightForWidth(self.pause_btn.sizePolicy().hasHeightForWidth())
        self.pause_btn.setSizePolicy(sizePolicy1)
        self.pause_btn.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u"../icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_btn.setIcon(icon3)
        self.pause_btn.setIconSize(QSize(35, 35))
        self.addNew_btn = QPushButton(self.frame_2)
        self.addNew_btn.setObjectName(u"addNew_btn")
        self.addNew_btn.setGeometry(QRect(10, 10, 30, 30))
        sizePolicy1.setHeightForWidth(self.addNew_btn.sizePolicy().hasHeightForWidth())
        self.addNew_btn.setSizePolicy(sizePolicy1)
        self.addNew_btn.setMinimumSize(QSize(0, 30))
        self.addNew_btn.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u"../icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addNew_btn.setIcon(icon4)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fileAddr_lbl = QLabel(self.frame)
        self.fileAddr_lbl.setObjectName(u"fileAddr_lbl")
        sizePolicy1.setHeightForWidth(self.fileAddr_lbl.sizePolicy().hasHeightForWidth())
        self.fileAddr_lbl.setSizePolicy(sizePolicy1)
        self.fileAddr_lbl.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.fileAddr_lbl, 1, 0, 1, 1)

        self.selectedPath_le = QLineEdit(self.frame)
        self.selectedPath_le.setObjectName(u"selectedPath_le")
        self.selectedPath_le.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.selectedPath_le.sizePolicy().hasHeightForWidth())
        self.selectedPath_le.setSizePolicy(sizePolicy3)
        self.selectedPath_le.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setBold(False)
        font2.setWeight(50)
        self.selectedPath_le.setFont(font2)

        self.gridLayout.addWidget(self.selectedPath_le, 3, 1, 1, 1)

        self.fileAddr_lbl2 = QLabel(self.frame)
        self.fileAddr_lbl2.setObjectName(u"fileAddr_lbl2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.fileAddr_lbl2.sizePolicy().hasHeightForWidth())
        self.fileAddr_lbl2.setSizePolicy(sizePolicy4)
        self.fileAddr_lbl2.setFont(font2)

        self.gridLayout.addWidget(self.fileAddr_lbl2, 1, 1, 1, 1)

        self.fileExt_lbl_2 = QLabel(self.frame)
        self.fileExt_lbl_2.setObjectName(u"fileExt_lbl_2")
        sizePolicy.setHeightForWidth(self.fileExt_lbl_2.sizePolicy().hasHeightForWidth())
        self.fileExt_lbl_2.setSizePolicy(sizePolicy)
        self.fileExt_lbl_2.setFont(font2)

        self.gridLayout.addWidget(self.fileExt_lbl_2, 2, 1, 1, 1)

        self.choosePath_btn = QPushButton(self.frame)
        self.choosePath_btn.setObjectName(u"choosePath_btn")
        self.choosePath_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.choosePath_btn.sizePolicy().hasHeightForWidth())
        self.choosePath_btn.setSizePolicy(sizePolicy1)
        self.choosePath_btn.setMinimumSize(QSize(100, 30))
        self.choosePath_btn.setMaximumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamily(u"Koodak")
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.choosePath_btn.setFont(font3)
        self.choosePath_btn.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.choosePath_btn, 3, 0, 1, 1)

        self.fileExt_lbl = QLabel(self.frame)
        self.fileExt_lbl.setObjectName(u"fileExt_lbl")
        sizePolicy1.setHeightForWidth(self.fileExt_lbl.sizePolicy().hasHeightForWidth())
        self.fileExt_lbl.setSizePolicy(sizePolicy1)
        self.fileExt_lbl.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.fileExt_lbl, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.tabWidget.addTab(self.insertNewTab, "")
        self.listViewTab = QWidget()
        self.listViewTab.setObjectName(u"listViewTab")
        self.verticalLayout_3 = QVBoxLayout(self.listViewTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listofDownload_tw = QTableWidget(self.listViewTab)
        if (self.listofDownload_tw.columnCount() < 6):
            self.listofDownload_tw.setColumnCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.listofDownload_tw.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.listofDownload_tw.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.listofDownload_tw.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.listofDownload_tw.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.listofDownload_tw.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.listofDownload_tw.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        self.listofDownload_tw.setObjectName(u"listofDownload_tw")
        self.listofDownload_tw.setFont(font1)

        self.verticalLayout_3.addWidget(self.listofDownload_tw)

        self.tabWidget.addTab(self.listViewTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Download Manager", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0635\u0641 \u062f\u0627\u0646\u0644\u0648\u062f \u0647\u0627", None))
        ___qtablewidgetitem = self.pending_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0641\u0627\u06cc\u0644", None));
        ___qtablewidgetitem1 = self.pending_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0633\u0648\u0646\u062f \u0641\u0627\u06cc\u0644", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u06cc\u0644 \u062c\u062f\u06cc\u062f", None))
        self.clear_btn.setText("")
        self.stop_btn.setText("")
        self.download_btn.setText("")
        self.pause_btn.setText("")
        self.addNew_btn.setText("")
        self.fileAddr_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062f\u0631\u0633 \u0641\u0627\u06cc\u0644 :", None))
        self.fileAddr_lbl2.setText("")
        self.fileExt_lbl_2.setText("")
        self.choosePath_btn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u062a\u062e\u0627\u0628 \u0645\u0633\u06cc\u0631", None))
        self.fileExt_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u0639 \u0648 \u067e\u0633\u0648\u0646\u062f \u0641\u0627\u06cc\u0644 :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.insertNewTab), QCoreApplication.translate("MainWindow", u"\u062e\u0627\u0646\u0647", None))
        ___qtablewidgetitem2 = self.listofDownload_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0631\u062f\u06cc\u0641", None));
        ___qtablewidgetitem3 = self.listofDownload_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0641\u0627\u06cc\u0644", None));
        ___qtablewidgetitem4 = self.listofDownload_tw.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0633\u0648\u0646\u062f \u0641\u0627\u06cc\u0644", None));
        ___qtablewidgetitem5 = self.listofDownload_tw.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062f\u0627\u0646\u0644\u0648\u062f", None));
        ___qtablewidgetitem6 = self.listofDownload_tw.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0632\u0645\u0627\u0646 \u062f\u0627\u0646\u0644\u0648\u062f", None));
        ___qtablewidgetitem7 = self.listofDownload_tw.horizontalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u062f\u0627\u0646\u0644\u0648\u062f", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.listViewTab), QCoreApplication.translate("MainWindow", u"\u0644\u06cc\u0633\u062a \u062f\u0627\u0646\u0644\u0648\u062f \u0647\u0627", None))
    # retranslateUi

