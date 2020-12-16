from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
 
class TInteractObj(QObject):
    SigReceivedMessFromJS = pyqtSignal(dict)
    SigSendMessageToJS = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
 
    @pyqtSlot(str,result=str)
    def JSSendMessage(self, strParameter):
        print('JSSendMessage(%s) from Html' %strParameter)
        dict1 = {'param':strParameter,'result':''}
        self.SigReceivedMessFromJS.emit(dict1)
        return dict1['result']
 
    @pyqtSlot(result=str)
    def fun(self):
        print('TInteractObj.fun()')
        return 'hello1'