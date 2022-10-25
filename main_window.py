import csv
import datetime
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import class_iterator
import data_to_weeks
import data_to_years
import div_data
import get_data
import gismeteo_parser


class GismeteoApplication(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Gismeteo Application')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.resize(500, 500)
        self.center()

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor('#99CCFF'))
        self.setPalette(palette)

        qbtn = QPushButton('&Выход', self)
        qbtn.move(210, 470)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        first_btn = QPushButton(
            '&Разделить исходный файл по файлам X.csv и Y.csv', self)
        first_btn.move(5, 5)
        first_btn.clicked.connect(self.start_div_data)

        second_btn = QPushButton('&Разделить исходный файл по годам', self)
        second_btn.move(5, 30)
        second_btn.clicked.connect(self.start_data_to_years)

        third_btn = QPushButton('&Разделить исходный файл по неделям', self)
        third_btn.move(5, 55)
        third_btn.clicked.connect(self.start_data_to_weeks)

        fourth_btn = QPushButton('&Создать исходный файл', self)
        fourth_btn.move(5, 80)
        fourth_btn.clicked.connect(self.start_parser)

        self.show()

    def start_data_to_weeks(self):
        """_summary_
        """
        
        _msg = QMessageBox()
        _msg.setWindowTitle('Сообщение')
        _msg.setText(
            'Выберите исходный файл, затем директорию куда сохранить вывод')
        _msg.setIcon(QMessageBox.Information)

        _msg.exec_()
        
        file_path = QFileDialog.getOpenFileName(self, 'Select Folder')[0]

        output_directory = QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        data_to_weeks.data_to_weeks(file_path, output_directory)

        done_msg = QMessageBox()
        done_msg.setWindowTitle('Сообщение')
        done_msg.setText('Файлы созданы по адресу :' +
                         str(os.path.join(output_directory, 'data_to_years_output')))
        done_msg.setIcon(QMessageBox.Information)

        done_msg.exec_()

    def start_data_to_years(self):
        """Function that sorts data to different files where each individual file will correspond to one year
        """

        _msg = QMessageBox()
        _msg.setWindowTitle('Сообщение')
        _msg.setText(
            'Выберите исходный файл, затем директорию куда сохранить вывод')
        _msg.setIcon(QMessageBox.Information)

        _msg.exec_()

        file_path = QFileDialog.getOpenFileName(self, 'Select Folder')[0]

        output_directory = QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        data_to_years.data_to_years(file_path, output_directory)

        done_msg = QMessageBox()
        done_msg.setWindowTitle('Сообщение')
        done_msg.setText('Файлы созданы по адресу :' +
                         str(os.path.join(output_directory, 'data_to_years_output')))
        done_msg.setIcon(QMessageBox.Information)

        done_msg.exec_()

    def start_div_data(self):
        """Creates X.csv and Y.csv files
        """

        _msg = QMessageBox()
        _msg.setWindowTitle('Сообщение')
        _msg.setText(
            'Выберите исходный файл, затем директорию куда сохранить вывод')
        _msg.setIcon(QMessageBox.Information)

        _msg.exec_()

        file_path = QFileDialog.getOpenFileName(self, 'Select Folder')[0]

        output_directory = QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        div_data.divide_data(file_path, output_directory)

        done_msg = QMessageBox()
        done_msg.setWindowTitle('Сообщение')
        done_msg.setText('Файлы созданы по адресу :' +
                         str(os.path.join(output_directory, 'divide_data_output')))
        done_msg.setIcon(QMessageBox.Information)

        done_msg.exec_()

    def start_parser(self):
        """Creates a source file
        """

        file_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        gismeteo_parser.main_part(file_path)

        done_msg = QMessageBox()
        done_msg.setWindowTitle('Сообщение')
        done_msg.setText('Исходный файл создан!')
        done_msg.setIcon(QMessageBox.Information)

        done_msg.exec_()

    def center(self):
        """Centers the program window
        """

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = GismeteoApplication()
    sys.exit(app.exec_())
