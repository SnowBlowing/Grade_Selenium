#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22  19:49
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import threading
import time

from PyQt5.Qt import *
import sys
import configparser

from WebScraper import WebScraper
from ui.ProcessDialog import ProcessDialog
from utility import Config_Tool, SQLite_Tool
from MenuContext import HelpDocument, AboutDialog

config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='utf-8')


class MenuBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # 创建菜单栏 QMenuBar
        menubar = QMenuBar(self)  # 创建菜单栏对象，并设置父对象
        menubar.setObjectName('menubar')  # 给菜单栏对象设置ObjectName
        # menubar.move(0, 0)                              # 设置菜单栏位置
        # menubar.resize(500, 30)                         # 设置菜单栏大小
        menubar.setGeometry(QRect(0, 0, 800, 30))  # 同时设置菜单栏位置和大小

        # 创建主菜单 QMenu
        menu = QMenu(menubar)  # 创建主菜单对象，并设置父对象
        menu.setObjectName('menu')  # 给主菜单设置ObjectName
        menu.setTitle('帮助')  # 给主菜单设置标题
        # menu.setIcon(QIcon('../images/bmp/204.bmp'))  # 设置主菜单是否可用
        # menu.setEnabled(False)                        # 设置主菜单是否可用

        # 创建菜单项 QAction
        action_help = QAction(menu)  # 创建菜单项对象，并设置父对象
        action_help.setObjectName('help')  # 给菜单项设置ObjectName
        action_help.setText('帮助文档')  # 设置菜单项显示文本
        # action.setIcon(QIcon('../images/bmp/100.bmp'))  # 设置菜单项图标
        action_help.setShortcut('Ctrl+H')  # 设置菜单项快捷键
        action_help.triggered.connect(self.help)

        action_about = QAction(menu)  # 创建菜单项对象，并设置父对象
        action_about.setObjectName('about')  # 给菜单项设置ObjectName
        action_about.setText('关于')  # 设置菜单项显示文本
        action_about.setShortcut('Ctrl+A')  # 设置菜单项快捷键
        action_about.triggered.connect(self.about)

        # 菜单项添加到主菜单
        menu.addAction(action_help)
        menu.addAction(action_about)
        # 主菜单添加分隔线
        menu.addSeparator()

        # 主菜单添加到菜单栏
        menubar.addMenu(menu)

    def help(self):
        help_document = HelpDocument()
        help_document.show()
        help_document.exec_()

    def about(self):
        about_document = AboutDialog()
        about_document.show()
        about_document.exec_()


# 无事件控件
class WidgetNonEvent(QWidget):
    def __init__(self, parent, *args):
        super().__init__(parent)
        self.move(80, 90)
        self.resize(700, 80)

        self.led = QLineEdit(self)
        self.led.move(100, 10)
        self.led.resize(self.width() - 120 - self.led.width(), 30)
        self.led.setText('http://218.26.234.85/views/search.html')

        self.label = QLabel(self)
        self.label.resize(100, 30)
        self.label.move(self.width() - 120 - self.led.width() - self.label.width(), 10)
        self.label.setText('网址：')


# 运行成绩爬虫
class RunScraper(QWidget):
    def __init__(self, parent, widget_select, widget_website, widget_save):
        super().__init__(parent)
        self.move(650, 220)
        self.resize(130, 50)

        self.btn = QPushButton(self)
        self.btn.resize(120, 30)
        self.btn.move(self.width() - self.btn.width(), 10)

        self.widget_select = widget_select
        self.widget_website = widget_website
        self.widget_save = widget_save

    def runs(self):
        self.btn.setText('运行')

        def process_dialog(my_process_dialog):
            my_process_dialog.exec_()

        def scraper():
            self.deal()
            # web_scraper.deal_data()

        def run():
            # 修改配置文件
            new_file_path = self.widget_select.led.text()
            new_web_site = self.widget_website.led.text()
            Config_Tool.modify_ini_file(new_file_path, new_web_site)

            # 运行爬虫
            web_scraper = WebScraper()

            # 处理数据
            # 获取数据总数
            web_scraper.sql.get_info_num()
            info_num = web_scraper.sql.info_num
            # 计算时间
            per_time = config.get('scraper', 'time')
            total_time = info_num * int(per_time)  # test为5，实际修改为info_num

            # 创建进度对话框
            my_process_dialog = ProcessDialog(total_time)

            # 创建线程：进度对话框，爬虫
            process_dialog_thread = threading.Thread(target=process_dialog, args=(my_process_dialog,))
            scraper_thread = threading.Thread(target=scraper)

            # 打开进度对话框
            my_process_dialog.show()

            # 运行线程
            process_dialog_thread.start()
            scraper_thread.start()

            self.widget_save.btn.setEnabled(True)

            # 关闭数据库
            web_scraper.sql.close_connection()

        self.btn.clicked.connect(run)

    # 模拟爬虫
    def deal(self):
        count = 0
        while count < 3:
            count += 1
            time.sleep(1)
            print('爬取数据中...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    process_dialog = ProcessDialog(5)

    process_dialog.show()
    sys.exit(app.exec_())
