import jdatetime
import time
import os
import re
import requests
from tkinter import Tk , ttk
from tkinter.filedialog import asksaveasfile , askdirectory , asksaveasfilename
from DownloadFileDialog import DownloadDialog, AddNewDialog
from DataAccess import ConnectToDB
from multiprocessing import Process
from ProjectException import Downloadexception , FileBroken
from PyQt5 import QtWidgets , QtCore


class Downloader:
    def __init__(self) -> None:
        self.data_access = ConnectToDB()
        self.is_addr_exists = False
        self.file_addr = None
        self.initGui()

    def reset_insert_new_tab(self):
        pass

    def update_ui_view(self):
        self.update_add_new_window()
        self.update_download_window()

    def update_add_new_window(self):
        self.dlg.progressBar.setValue(0)
        self.anw.url_le.setText('')

    def update_download_window(self):
        self.dlg.fileAddr_lbl2.setText(self.file_url)
        self.dlg.fileExt_lbl_2.setText(self.current_file_type + ' - '+ self.current_file_extention)
        self.is_addr_exists = True
        self.dlg.download_btn.setEnabled(True)
        self.dlg.choosePath_btn.setEnabled(True)
        self.dlg.clear_btn.setEnabled(True)

    def add_new_page(self):
        self.add_new_sub_window.show()
        self.anw.url_submit.clicked.connect(self.get_new_url)

    def get_new_url(self):
        self.file_url = self.anw.url_le.text()
        self.add_new_sub_window.close()
        self.get_data_from_address()
        self.update_ui_view()

    def check_trigger(self):
        self.dlg.addNew_btn.clicked.connect(self.add_new_page)
        self.dlg.download_btn.clicked.connect(self.download_file)
        self.dlg.choosePath_btn.clicked.connect(self.save_path_file)

    def save_path_file(self):
        files , download_folder = self.address_setting()
        self.file_addr = asksaveasfilename(initialdir=download_folder , filetypes=files , defaultextension=self.current_file_extention)
        print(self.file_addr)
        if self.file_addr is None:
            return
        self.dlg.selectedPath_le.setText(self.file_addr)
    
    def address_setting(self):
        files = [('videos' , '*.mp4')]
        download_folder = os.path.expanduser("~")+"/Downloads"
        return files , download_folder
        
    def create_ui(self):
        self.createDownloadDialog()
        self.createAddNewDialog()

    def createDownloadDialog(self):
        self.dlg = DownloadDialog()
        self.update_pending_table()

    def download_file(self):
        self.initial_file_details()
        self.update_pending_table()
        self.dlg.download_btn.setEnabled(False)
        self.dlg.choosePath_btn.setEnabled(False)
        download_process = Process(target=self.create_file_with_data)
        download_process.start()

    def initial_file_details(self):
        file_name = self.file_name_setting()
        self.add_file_to_pending_table(file_name)

    def update_pending_table(self):
        all_pending_list = self.data_access.select_from_pending_list()
        self.dlg.pending_list.setRowCount(0)
        for each_pending_item in all_pending_list:
            rows = self.dlg.pending_list.rowCount()
            self.dlg.pending_list.setRowCount(rows + 1)
            
            name_item = QtWidgets.QTableWidgetItem(str(each_pending_item[1] if each_pending_item[1] is not None else ''))
            name_item.setTextAlignment(QtCore.Qt.AlignHCenter)# name
            name_item.setTextAlignment(QtCore.Qt.AlignVCenter)# name
            
            extention_item = QtWidgets.QTableWidgetItem(str(each_pending_item[2] if each_pending_item[2] is not None else ''))
            extention_item.setTextAlignment(QtCore.Qt.AlignHCenter)# extention
            extention_item.setTextAlignment(QtCore.Qt.AlignVCenter)# extention
            
            self.dlg.pending_list.setItem(rows, 0, name_item)
            self.dlg.pending_list.setItem(rows, 1, extention_item)
            self.dlg.pending_list.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
            self.dlg.pending_list.horizontalHeader().setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        
    def add_file_to_pending_table(self , file_name):
        cdate = jdatetime.date.today()
        ctime = time.strftime("%H:%M:%S",time.localtime())
        self.inserted_id = self.data_access.insert_new_download(file_name , self.current_file_extention , cdate , ctime, 'pending')   
        
    def update_file_status(self , dmid , status):
        cdate = jdatetime.date.today()
        ctime = time.strftime("%H:%M:%S",time.localtime())
        self.data_access.update_downloaded_file_status(status , dmid , cdate , ctime)   
    
    def file_name_setting(self):
        if self.file_addr:
            file_name = self.file_addr.split('/')[-1]
        else :
            file_addr = self.address_setting()
            default_name = self.data_access.select_last_file_of_extention(self.current_file_extention)
            file_name = 'untitled-{}'.format(default_name)
            self.file_addr = file_addr[1] + "/" + file_name
        return file_name
            
    def get_data_from_address(self):
        self.main_data = requests.get(self.file_url, stream=True)
        self.data_size = int(self.main_data.headers.get('content-length'))
        current_file_content_type = self.main_data.headers.get('Content-Type').split('/')
        self.current_file_type = current_file_content_type[0]
        self.current_file_extention = f'.{current_file_content_type[1]}'

    def change_items_visibility(self):
        if self.is_addr_exists:
            self.downloading_visibility()
        else :
            self.no_downloading_visibility()
        
    def downloading_visibility(self):
        self.dlg.download_btn.setEnabled(False)
        self.dlg.clear_btn.setEnabled(False)
        self.dlg.pause_btn.setEnabled(True)
        self.dlg.stop_btn.setEnabled(True)
        self.dlg.choosePath_btn.setEnabled(False)
    
    def no_downloading_visibility(self):
        self.dlg.download_btn.setEnabled(False)
        self.dlg.clear_btn.setEnabled(True)
        self.dlg.pause_btn.setEnabled(False)
        self.dlg.stop_btn.setEnabled(False)
        self.dlg.choosePath_btn.setEnabled(False)
    
    def create_file_with_data(self):
        # with open(f'{self.default_file_name}.{self.file_extention}' , 'wb') as f:
        with open(self.file_addr , 'wb') as f:
            print("Downloading")
            if not self.data_size:
                error = "\nthe file is broken.\nfile size is : {file_size}".format(file_size=self.data_size)
                f.write(self.main_data.content)
                status = 'failed'
                raise FileBroken(error)
            else :
                download_until_now = 0
                lastdone = 0

                for step_data in self.main_data.iter_content(chunk_size=4096):
                    f.write(step_data)
                    download_until_now += len(step_data)
                    done = int(download_until_now*100/self.data_size)
                    if done != lastdone:
                        # self.dlg.progressBar.setValue(done)
                        print(lastdone , done)
                    lastdone = done
                status = 'complete'
        self.is_addr_exists = False
        print("Download Complete !")
        self.update_file_status(self.inserted_id , status)
        self.update_pending_table()
        

    def createAddNewDialog(self):
        self.anw = AddNewDialog()
        self.add_new_sub_window = QtWidgets.QDialog()
        self.anw.setupUi(self.add_new_sub_window)

    def initGui(self):
        self.create_ui()
        self.check_trigger()
        self.dlg.show()
