# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 903)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1281, 951))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.DashBoard_Tab = QtWidgets.QWidget()
        self.DashBoard_Tab.setObjectName("DashBoard_Tab")
        self.widget = QtWidgets.QWidget(self.DashBoard_Tab)
        self.widget.setGeometry(QtCore.QRect(30, 30, 111, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.New_Book_Button = QtWidgets.QPushButton(self.widget)
        self.New_Book_Button.setObjectName("New_Book_Button")
        self.verticalLayout_8.addWidget(self.New_Book_Button)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(self.DashBoard_Tab)
        self.widget1.setGeometry(QtCore.QRect(30, 140, 1131, 581))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IssuedBooks_Table = QtWidgets.QTableWidget(self.widget1)
        self.IssuedBooks_Table.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.IssuedBooks_Table.setRowCount(0)
        self.IssuedBooks_Table.setColumnCount(8)
        self.IssuedBooks_Table.setObjectName("IssuedBooks_Table")
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table.setHorizontalHeaderItem(7, item)
        self.horizontalLayout.addWidget(self.IssuedBooks_Table)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Delete_Issued = QtWidgets.QPushButton(self.widget1)
        self.Delete_Issued.setObjectName("Delete_Issued")
        self.verticalLayout_2.addWidget(self.Delete_Issued)
        self.Edit_Issued = QtWidgets.QPushButton(self.widget1)
        self.Edit_Issued.setObjectName("Edit_Issued")
        self.verticalLayout_2.addWidget(self.Edit_Issued)
        self.Refresh_Issued = QtWidgets.QPushButton(self.widget1)
        self.Refresh_Issued.setObjectName("Refresh_Issued")
        self.verticalLayout_2.addWidget(self.Refresh_Issued)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.UnIssuedBooks_Table = QtWidgets.QTableWidget(self.widget1)
        self.UnIssuedBooks_Table.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.UnIssuedBooks_Table.setRowCount(0)
        self.UnIssuedBooks_Table.setColumnCount(8)
        self.UnIssuedBooks_Table.setObjectName("UnIssuedBooks_Table")
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.UnIssuedBooks_Table.setHorizontalHeaderItem(7, item)
        self.horizontalLayout_2.addWidget(self.UnIssuedBooks_Table)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Delete_UnIssued = QtWidgets.QPushButton(self.widget1)
        self.Delete_UnIssued.setObjectName("Delete_UnIssued")
        self.verticalLayout_3.addWidget(self.Delete_UnIssued)
        self.Edit_UnIssued = QtWidgets.QPushButton(self.widget1)
        self.Edit_UnIssued.setObjectName("Edit_UnIssued")
        self.verticalLayout_3.addWidget(self.Edit_UnIssued)
        self.Refresh_UnIssued = QtWidgets.QPushButton(self.widget1)
        self.Refresh_UnIssued.setObjectName("Refresh_UnIssued")
        self.verticalLayout_3.addWidget(self.Refresh_UnIssued)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.DashBoard_Tab, "")
        self.Find_Tab = QtWidgets.QWidget()
        self.Find_Tab.setObjectName("Find_Tab")
        self.widget2 = QtWidgets.QWidget(self.Find_Tab)
        self.widget2.setGeometry(QtCore.QRect(10, 20, 811, 681))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.SearchInput = QtWidgets.QLineEdit(self.widget2)
        self.SearchInput.setObjectName("SearchInput")
        self.horizontalLayout_4.addWidget(self.SearchInput)
        self.SearchButton = QtWidgets.QPushButton(self.widget2)
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout_4.addWidget(self.SearchButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.IssuedBooks_Table_2 = QtWidgets.QTableWidget(self.widget2)
        self.IssuedBooks_Table_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.IssuedBooks_Table_2.setRowCount(0)
        self.IssuedBooks_Table_2.setColumnCount(8)
        self.IssuedBooks_Table_2.setObjectName("IssuedBooks_Table_2")
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.IssuedBooks_Table_2.setHorizontalHeaderItem(7, item)
        self.verticalLayout_9.addWidget(self.IssuedBooks_Table_2)
        self.tabWidget.addTab(self.Find_Tab, "")
        self.AllBooks_Tab = QtWidgets.QWidget()
        self.AllBooks_Tab.setObjectName("AllBooks_Tab")
        self.All_Books_Table = QtWidgets.QTableWidget(self.AllBooks_Tab)
        self.All_Books_Table.setGeometry(QtCore.QRect(30, 80, 811, 741))
        self.All_Books_Table.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.All_Books_Table.setShowGrid(True)
        self.All_Books_Table.setRowCount(0)
        self.All_Books_Table.setColumnCount(8)
        self.All_Books_Table.setObjectName("All_Books_Table")
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.All_Books_Table.setHorizontalHeaderItem(7, item)
        self.All_Books_Table.horizontalHeader().setVisible(False)
        self.All_Books_Table.horizontalHeader().setHighlightSections(True)
        self.All_Books_Table.verticalHeader().setVisible(False)
        self.widget3 = QtWidgets.QWidget(self.AllBooks_Tab)
        self.widget3.setGeometry(QtCore.QRect(30, 20, 131, 51))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.RefreshButton = QtWidgets.QPushButton(self.widget3)
        self.RefreshButton.setObjectName("RefreshButton")
        self.verticalLayout_10.addWidget(self.RefreshButton)
        self.tabWidget.addTab(self.AllBooks_Tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Actions"))
        self.New_Book_Button.setText(_translate("MainWindow", "New Book"))
        self.label_2.setText(_translate("MainWindow", "Books"))
        self.label_3.setText(_translate("MainWindow", "Issued Books"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page Count"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.IssuedBooks_Table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.Delete_Issued.setText(_translate("MainWindow", "Delete"))
        self.Edit_Issued.setText(_translate("MainWindow", "Edit"))
        self.Refresh_Issued.setText(_translate("MainWindow", "Refresh"))
        self.label_4.setText(_translate("MainWindow", "Unissued Books"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page Count"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.UnIssuedBooks_Table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.Delete_UnIssued.setText(_translate("MainWindow", "Delete"))
        self.Edit_UnIssued.setText(_translate("MainWindow", "Edit"))
        self.Refresh_UnIssued.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DashBoard_Tab), _translate("MainWindow", "DashBoard"))
        self.label_5.setText(_translate("MainWindow", "Search By ID:"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page Count"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.IssuedBooks_Table_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Find_Tab), _translate("MainWindow", "Find"))
        item = self.All_Books_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.All_Books_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.All_Books_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.All_Books_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.All_Books_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page Count"))
        item = self.All_Books_Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.All_Books_Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.All_Books_Table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.label_6.setText(_translate("MainWindow", "All Books"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AllBooks_Tab), _translate("MainWindow", "All Books"))
