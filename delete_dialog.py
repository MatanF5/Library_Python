# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete_dialog(object):
    def setupUi(self, delete_dialog):
        delete_dialog.setObjectName("delete_dialog")
        delete_dialog.resize(461, 211)
        self.buttonBox = QtWidgets.QDialogButtonBox(delete_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 140, 151, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(delete_dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 60, 401, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(delete_dialog)
        self.buttonBox.accepted.connect(delete_dialog.accept)
        self.buttonBox.rejected.connect(delete_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(delete_dialog)

    def retranslateUi(self, delete_dialog):
        _translate = QtCore.QCoreApplication.translate
        delete_dialog.setWindowTitle(_translate("delete_dialog", "DeleteBox"))
        self.textBrowser.setHtml(_translate("delete_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Are You Sure You Want to Delete This Books</span></p></body></html>"))
