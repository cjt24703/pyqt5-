from PyQt5.QtWidgets import QWidget,QDialog, QPlainTextEdit, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from TInteractObject import TInteractObj
 
class TMainWindow(QDialog):
    
    SigSendMessageToJS = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
        #---Qt widget and layout---
        self.mpQtContentTextEdit = QPlainTextEdit(self)
        self.mpQtContentTextEdit.setMidLineWidth(1000)
        self.mpQtContentTextEdit.setReadOnly(True)
 
        self.mpQtSendLineEdit = QLineEdit(self)
 
        self.mpQtSendBtnByInteractObj = QPushButton('Send', self)
        self.mpQtSendBtnByInteractObj.setToolTip('Send message by Interact object style')
 
        self.mpQtSendBtnByJavaScript = QPushButton('Send2', self)
        self.mpQtSendBtnByJavaScript.setToolTip('Send message by runJavaScript style')
 
        self.pQtSendHLayout = QHBoxLayout()
        self.pQtSendHLayout.setSpacing(0)
        self.pQtSendHLayout.addWidget(self.mpQtSendLineEdit)
        self.pQtSendHLayout.addSpacing(5)
        self.pQtSendHLayout.addWidget(self.mpQtSendBtnByInteractObj)
        self.pQtSendHLayout.addSpacing(5)
        self.pQtSendHLayout.addWidget(self.mpQtSendBtnByJavaScript)
 
        self.pQtTotalVLayout = QVBoxLayout()
        self.pQtTotalVLayout.setSpacing(0)
        self.pQtTotalVLayout.addWidget(self.mpQtContentTextEdit)
        self.pQtTotalVLayout.setSpacing(5)
        self.pQtTotalVLayout.addLayout(self.pQtSendHLayout)
 
        self.pQtGroup = QGroupBox('Qt View', self)
        self.pQtGroup.setLayout(self.pQtTotalVLayout)
 
        #---Web widget and layout---
        self.mpJSWebView = QWebEngineView(self)
        self.pWebChannel = QWebChannel(self.mpJSWebView.page())
        self.pInteractObj = TInteractObj(self)
        self.pWebChannel.registerObject("interactObj", self.pInteractObj)
        self.mpJSWebView.page().setWebChannel(self.pWebChannel)
 
        self.url = 'file:///D:/python/pyqt/web/JSTest.html'
        self.mpJSWebView.page().load(QUrl(self.url))
        self.mpJSWebView.setFixedWidth(800)
        self.mpJSWebView.show()
 
        self.pJSTotalVLayout = QVBoxLayout()
        self.pJSTotalVLayout.setSpacing(0)
        self.pJSTotalVLayout.addWidget(self.mpJSWebView)
        self.pWebGroup = QGroupBox('Web View', self)
        self.pWebGroup.setLayout(self.pJSTotalVLayout)
 
        #---TMainWindow total layout---
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(5)
        self.mainLayout.addWidget(self.pQtGroup)
        self.mainLayout.setSpacing(5)
        self.mainLayout.addWidget(self.pWebGroup)
        self.setLayout(self.mainLayout)
        self.setMinimumSize(100, 100)
 
        self.mpQtSendBtnByInteractObj.clicked.connect(self.OnSendMessageByInteractObj)
        self.mpQtSendBtnByJavaScript.clicked.connect(self.OnSendMessageByJavaScript)
        self.pInteractObj.SigReceivedMessFromJS.connect(self.OnReceiveMessageFromJS)
        self.SigSendMessageToJS.connect(self.pInteractObj.SigSendMessageToJS)
 
    def OnReceiveMessageFromJS(self, strParameter):
        print('OnReceiveMessageFromJS()')
        if not strParameter:
            return
        self.mpQtContentTextEdit.appendPlainText(strParameter['param'])
        strParameter['result'] = 'success'
 
    def OnSendMessageByInteractObj(self):
        strMessage = self.mpQtSendLineEdit.text()
        if not strMessage:
            return
        self.SigSendMessageToJS.emit(strMessage)
 
    def OnSendMessageByJavaScript(self):
        strMessage = self.mpQtSendLineEdit.text()
        if not strMessage:
            return
        self.mpJSWebView.page().runJavaScript("output(%s)" %strMessage)
        self.mpJSWebView.page().runJavaScript("showAlert()")
    
    def keyPressEvent(self,event):
        print("按下：" + str(event.key()))
        if(event.key() == Qt.Key_F12):
            print('测试：F12')
            # self.hide()#隐藏此窗口
            self.s = TDevWindow()#将第二个窗口换个名字
            self.s.show()#经第二个窗口显示出来
            self.mpJSWebView.page().setDevToolsPage(self.s.mpJSWebView.page())


class TDevWindow(QDialog):
    def __init__(self):
        super(TDevWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.mpJSWebView = QWebEngineView(self)
        self.url = 'https://www.baidu.com/'
        self.mpJSWebView.page().load(QUrl(self.url))
        self.mpJSWebView.show()
 
        self.pJSTotalVLayout = QVBoxLayout()
        self.pJSTotalVLayout.setSpacing(0)
        self.pJSTotalVLayout.addWidget(self.mpJSWebView)
        self.pWebGroup = QGroupBox('Web View', self)
        self.pWebGroup.setLayout(self.pJSTotalVLayout)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(5)
        self.mainLayout.addWidget(self.pWebGroup)
        self.setLayout(self.mainLayout)
        self.setMinimumSize(800, 800)

       
    
    