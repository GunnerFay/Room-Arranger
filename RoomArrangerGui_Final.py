# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui5.ui'
#
# Created: Wed May  9 20:15:36 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 724)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 633, 633))
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.MicrowaveButton = QtGui.QPushButton(self.widget)
        self.MicrowaveButton.setObjectName("MicrowaveButton")
        self.gridLayout.addWidget(self.MicrowaveButton, 0, 3, 1, 1)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.DeskWidth = QtGui.QSpinBox(self.widget)
        self.DeskWidth.setMaximum(10)
        self.DeskWidth.setObjectName("DeskWidth")
        self.verticalLayout_10.addWidget(self.DeskWidth)
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.DeskLength = QtGui.QSpinBox(self.widget)
        self.DeskLength.setMaximum(10)
        self.DeskLength.setObjectName("DeskLength")
        self.verticalLayout_10.addWidget(self.DeskLength)
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14)
        self.DeskHeight = QtGui.QSpinBox(self.widget)
        self.DeskHeight.setMaximum(10)
        self.DeskHeight.setObjectName("DeskHeight")
        self.verticalLayout_10.addWidget(self.DeskHeight)
        self.gridLayout.addLayout(self.verticalLayout_10, 1, 5, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_21 = QtGui.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.TableWidth = QtGui.QSpinBox(self.widget)
        self.TableWidth.setMaximum(10)
        self.TableWidth.setObjectName("TableWidth")
        self.verticalLayout_5.addWidget(self.TableWidth)
        self.label_22 = QtGui.QLabel(self.widget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.TableLength = QtGui.QSpinBox(self.widget)
        self.TableLength.setMaximum(10)
        self.TableLength.setObjectName("TableLength")
        self.verticalLayout_5.addWidget(self.TableLength)
        self.label_23 = QtGui.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.TableHeight = QtGui.QSpinBox(self.widget)
        self.TableHeight.setMaximum(10)
        self.TableHeight.setObjectName("TableHeight")
        self.verticalLayout_5.addWidget(self.TableHeight)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 1, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_18 = QtGui.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.MIcrowaveWidth = QtGui.QSpinBox(self.widget)
        self.MIcrowaveWidth.setMaximum(10)
        self.MIcrowaveWidth.setObjectName("MIcrowaveWidth")
        self.verticalLayout_3.addWidget(self.MIcrowaveWidth)
        self.label_19 = QtGui.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.MicrowaveLength = QtGui.QSpinBox(self.widget)
        self.MicrowaveLength.setMaximum(10)
        self.MicrowaveLength.setObjectName("MicrowaveLength")
        self.verticalLayout_3.addWidget(self.MicrowaveLength)
        self.label_20 = QtGui.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.MicrowaveHeight = QtGui.QSpinBox(self.widget)
        self.MicrowaveHeight.setMaximum(10)
        self.MicrowaveHeight.setObjectName("MicrowaveHeight")
        self.verticalLayout_3.addWidget(self.MicrowaveHeight)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 3, 1, 1)
        self.BookshelfButton = QtGui.QPushButton(self.widget)
        self.BookshelfButton.setObjectName("BookshelfButton")
        self.gridLayout.addWidget(self.BookshelfButton, 2, 0, 1, 1)
        self.TableButton = QtGui.QPushButton(self.widget)
        self.TableButton.setObjectName("TableButton")
        self.gridLayout.addWidget(self.TableButton, 2, 1, 1, 1)
        self.WallLightButton = QtGui.QPushButton(self.widget)
        self.WallLightButton.setObjectName("WallLightButton")
        self.gridLayout.addWidget(self.WallLightButton, 2, 3, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.BookshelfWidth = QtGui.QSpinBox(self.widget)
        self.BookshelfWidth.setMaximum(10)
        self.BookshelfWidth.setObjectName("BookshelfWidth")
        self.verticalLayout_4.addWidget(self.BookshelfWidth)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.BookshelfLength = QtGui.QSpinBox(self.widget)
        self.BookshelfLength.setMaximum(10)
        self.BookshelfLength.setObjectName("BookshelfLength")
        self.verticalLayout_4.addWidget(self.BookshelfLength)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.BookshelfHeight = QtGui.QSpinBox(self.widget)
        self.BookshelfHeight.setMaximum(10)
        self.BookshelfHeight.setObjectName("BookshelfHeight")
        self.verticalLayout_4.addWidget(self.BookshelfHeight)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_34 = QtGui.QLabel(self.widget)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_6.addWidget(self.label_34)
        self.WallLightHeight = QtGui.QSpinBox(self.widget)
        self.WallLightHeight.setMaximum(10)
        self.WallLightHeight.setObjectName("WallLightHeight")
        self.verticalLayout_6.addWidget(self.WallLightHeight)
        self.gridLayout.addLayout(self.verticalLayout_6, 3, 3, 1, 1)
        self.BedButton = QtGui.QPushButton(self.widget)
        self.BedButton.setObjectName("BedButton")
        self.gridLayout.addWidget(self.BedButton, 0, 0, 1, 1)
        self.PosterButton = QtGui.QPushButton(self.widget)
        self.PosterButton.setObjectName("PosterButton")
        self.gridLayout.addWidget(self.PosterButton, 0, 1, 1, 1)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout.addLayout(self.verticalLayout_12, 3, 5, 1, 1)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_29 = QtGui.QLabel(self.widget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_13.addWidget(self.label_29)
        self.LampHeight = QtGui.QSpinBox(self.widget)
        self.LampHeight.setMaximum(10)
        self.LampHeight.setObjectName("LampHeight")
        self.verticalLayout_13.addWidget(self.LampHeight)
        self.gridLayout.addLayout(self.verticalLayout_13, 1, 4, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_30 = QtGui.QLabel(self.widget)
        self.label_30.setObjectName("label_30")
        self.verticalLayout.addWidget(self.label_30)
        self.BedWidth = QtGui.QSpinBox(self.widget)
        self.BedWidth.setMaximum(10)
        self.BedWidth.setObjectName("BedWidth")
        self.verticalLayout.addWidget(self.BedWidth)
        self.label_31 = QtGui.QLabel(self.widget)
        self.label_31.setObjectName("label_31")
        self.verticalLayout.addWidget(self.label_31)
        self.BedLength = QtGui.QSpinBox(self.widget)
        self.BedLength.setMaximum(10)
        self.BedLength.setObjectName("BedLength")
        self.verticalLayout.addWidget(self.BedLength)
        self.label_32 = QtGui.QLabel(self.widget)
        self.label_32.setObjectName("label_32")
        self.verticalLayout.addWidget(self.label_32)
        self.BedHeight = QtGui.QSpinBox(self.widget)
        self.BedHeight.setMaximum(10)
        self.BedHeight.setObjectName("BedHeight")
        self.verticalLayout.addWidget(self.BedHeight)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_27 = QtGui.QLabel(self.widget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_2.addWidget(self.label_27)
        self.PosterWidth = QtGui.QSpinBox(self.widget)
        self.PosterWidth.setMaximum(10)
        self.PosterWidth.setObjectName("PosterWidth")
        self.verticalLayout_2.addWidget(self.PosterWidth)
        self.label_28 = QtGui.QLabel(self.widget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_2.addWidget(self.label_28)
        self.PosterLength = QtGui.QSpinBox(self.widget)
        self.PosterLength.setMaximum(10)
        self.PosterLength.setObjectName("PosterLength")
        self.verticalLayout_2.addWidget(self.PosterLength)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.ClosetWidth = QtGui.QSpinBox(self.widget)
        self.ClosetWidth.setMaximum(10)
        self.ClosetWidth.setObjectName("ClosetWidth")
        self.verticalLayout_7.addWidget(self.ClosetWidth)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.ClosetLength = QtGui.QSpinBox(self.widget)
        self.ClosetLength.setMaximum(10)
        self.ClosetLength.setObjectName("ClosetLength")
        self.verticalLayout_7.addWidget(self.ClosetLength)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.ClosetHeight = QtGui.QSpinBox(self.widget)
        self.ClosetHeight.setMaximum(10)
        self.ClosetHeight.setObjectName("ClosetHeight")
        self.verticalLayout_7.addWidget(self.ClosetHeight)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 2, 1, 1)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_36 = QtGui.QLabel(self.widget)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_15.addWidget(self.label_36)
        self.RefrigeratorHeight = QtGui.QSpinBox(self.widget)
        self.RefrigeratorHeight.setMaximum(10)
        self.RefrigeratorHeight.setObjectName("RefrigeratorHeight")
        self.verticalLayout_15.addWidget(self.RefrigeratorHeight)
        self.RefrigeratorLength = QtGui.QSpinBox(self.widget)
        self.RefrigeratorLength.setMaximum(10)
        self.RefrigeratorLength.setObjectName("RefrigeratorLength")
        self.verticalLayout_15.addWidget(self.RefrigeratorLength)
        self.RefrigeratorWidth = QtGui.QSpinBox(self.widget)
        self.RefrigeratorWidth.setMaximum(10)
        self.RefrigeratorWidth.setObjectName("RefrigeratorWidth")
        self.verticalLayout_15.addWidget(self.RefrigeratorWidth)
        self.label_35 = QtGui.QLabel(self.widget)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_15.addWidget(self.label_35)
        self.label_37 = QtGui.QLabel(self.widget)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_15.addWidget(self.label_37)
        self.gridLayout.addLayout(self.verticalLayout_15, 3, 4, 1, 1)
        self.ChairButton = QtGui.QPushButton(self.widget)
        self.ChairButton.setObjectName("ChairButton")
        self.gridLayout.addWidget(self.ChairButton, 2, 2, 1, 1)
        self.ClosetButton = QtGui.QPushButton(self.widget)
        self.ClosetButton.setObjectName("ClosetButton")
        self.gridLayout.addWidget(self.ClosetButton, 0, 2, 1, 1)
        self.DeskButton = QtGui.QPushButton(self.widget)
        self.DeskButton.setObjectName("DeskButton")
        self.gridLayout.addWidget(self.DeskButton, 0, 5, 1, 1)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_24 = QtGui.QLabel(self.widget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_14.addWidget(self.label_24)
        self.ChairWidth = QtGui.QSpinBox(self.widget)
        self.ChairWidth.setMaximum(10)
        self.ChairWidth.setObjectName("ChairWidth")
        self.verticalLayout_14.addWidget(self.ChairWidth)
        self.label_25 = QtGui.QLabel(self.widget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_14.addWidget(self.label_25)
        self.ChairLength = QtGui.QSpinBox(self.widget)
        self.ChairLength.setMaximum(10)
        self.ChairLength.setObjectName("ChairLength")
        self.verticalLayout_14.addWidget(self.ChairLength)
        self.label_26 = QtGui.QLabel(self.widget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_14.addWidget(self.label_26)
        self.ChairHeight = QtGui.QSpinBox(self.widget)
        self.ChairHeight.setMaximum(10)
        self.ChairHeight.setObjectName("ChairHeight")
        self.verticalLayout_14.addWidget(self.ChairHeight)
        self.gridLayout.addLayout(self.verticalLayout_14, 3, 2, 1, 1)
        self.LampButton = QtGui.QPushButton(self.widget)
        self.LampButton.setObjectName("LampButton")
        self.gridLayout.addWidget(self.LampButton, 0, 4, 1, 1)
        self.MaterialsLabel = QtGui.QLabel(self.widget)
        self.MaterialsLabel.setObjectName("MaterialsLabel")
        self.gridLayout.addWidget(self.MaterialsLabel, 5, 0, 1, 1)
        self.RefrigeratorButton = QtGui.QPushButton(self.widget)
        self.RefrigeratorButton.setObjectName("RefrigeratorButton")
        self.gridLayout.addWidget(self.RefrigeratorButton, 2, 4, 1, 1)
        self.MaterialBox = QtGui.QComboBox(self.widget)
        self.MaterialBox.setObjectName("MaterialBox")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.gridLayout.addWidget(self.MaterialBox, 5, 1, 1, 1)
        self.OlinChairButton = QtGui.QPushButton(self.widget)
        self.OlinChairButton.setObjectName("OlinChairButton")
        self.gridLayout.addWidget(self.OlinChairButton, 2, 5, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_40 = QtGui.QLabel(self.widget)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 4, 2, 1, 1)
        self.label_43 = QtGui.QLabel(self.widget)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 7, 2, 1, 1)
        self.label_41 = QtGui.QLabel(self.widget)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 5, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 2, 1, 1)
        self.label_42 = QtGui.QLabel(self.widget)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 6, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 1, 1, 1)
        self.label_39 = QtGui.QLabel(self.widget)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 3, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_38 = QtGui.QLabel(self.widget)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 7, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.widget)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 5, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 6, 1, 1, 1)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.MicrowaveButton.setText(QtGui.QApplication.translate("MainWindow", "Microwave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.BookshelfButton.setText(QtGui.QApplication.translate("MainWindow", "Bookshelf", None, QtGui.QApplication.UnicodeUTF8))
        self.TableButton.setText(QtGui.QApplication.translate("MainWindow", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.WallLightButton.setText(QtGui.QApplication.translate("MainWindow", "Wall Light", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.BedButton.setText(QtGui.QApplication.translate("MainWindow", "Bed", None, QtGui.QApplication.UnicodeUTF8))
        self.PosterButton.setText(QtGui.QApplication.translate("MainWindow", "Poster", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.ChairButton.setText(QtGui.QApplication.translate("MainWindow", "Chair", None, QtGui.QApplication.UnicodeUTF8))
        self.ClosetButton.setText(QtGui.QApplication.translate("MainWindow", "Closet", None, QtGui.QApplication.UnicodeUTF8))
        self.DeskButton.setText(QtGui.QApplication.translate("MainWindow", "Desk", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.LampButton.setText(QtGui.QApplication.translate("MainWindow", "Lamp", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialsLabel.setText(QtGui.QApplication.translate("MainWindow", "Materials", None, QtGui.QApplication.UnicodeUTF8))
        self.RefrigeratorButton.setText(QtGui.QApplication.translate("MainWindow", "Refrigerator", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Plastic", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Earth", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Diffuse", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "Emissive", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "Unshaded", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "Shiny", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(7, QtGui.QApplication.translate("MainWindow", "Chrome", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(8, QtGui.QApplication.translate("MainWindow", "Blazed", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(9, QtGui.QApplication.translate("MainWindow", "Earth with Clouds", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(10, QtGui.QApplication.translate("MainWindow", "Brick", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(11, QtGui.QApplication.translate("MainWindow", "Silver", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(12, QtGui.QApplication.translate("MainWindow", "Wood", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(13, QtGui.QApplication.translate("MainWindow", "Rough", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(14, QtGui.QApplication.translate("MainWindow", "Marble", None, QtGui.QApplication.UnicodeUTF8))
        self.OlinChairButton.setText(QtGui.QApplication.translate("MainWindow", "Olin Chair", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("MainWindow", "Move item horizontally/rotate view", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("MainWindow", "Rotate Item", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("MainWindow", "Snap to View", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Key Board Shortcuts", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Snap selected/all item(s) to grid", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("MainWindow", "Move Item", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Arrow (Item Selected/No Item Selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("MainWindow", "Move selected item/all items to the floor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "G (Item Selected/No Item Selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("MainWindow", "Alt+Click+Drag", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("MainWindow", "1,2,3,4,5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "S (Item Selected/No Item Selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Click+Drag", None, QtGui.QApplication.UnicodeUTF8))

