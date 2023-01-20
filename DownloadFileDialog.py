import sys
import os
from PyQt5 import uic
# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
path = os.path.dirname(os.path.abspath(__file__))
MainWindowUI, MainWindowBase = uic.loadUiType(
    os.path.join(path, 'gui/AppUi/DownloadFileDialog.ui'))

AddNewUI, AddNewBase = uic.loadUiType(
    os.path.join(path, 'gui/AppUi/AddNewDialog.ui'))


class DownloadDialog(MainWindowBase,MainWindowUI):
    def __init__(self, parent=None):
        """Constructor."""
        MainWindowBase.__init__(self, parent)
        self.setupUi(self)
        
        
class AddNewDialog(AddNewBase,AddNewUI):
    def __init__(self, parent=None):
        """Constructor."""
        AddNewBase.__init__(self, parent)