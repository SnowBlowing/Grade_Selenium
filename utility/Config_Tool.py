#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22  20:05
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import configparser


def modify_ini_file(new_file_path, new_web_site):
    # 配置文件路径
    inifile_path = '../config/config.ini'
    # 创建 ConfigParser 对象
    config = configparser.ConfigParser()

    # 读取 INI 文件
    config.read(inifile_path)

    # 修改值
    config.set('web', 'site', new_web_site)
    config.set('excel', 'path', new_file_path)

    # 写入修改后的内容到文件
    with open(inifile_path, 'w', encoding='utf-8') as config_file:
        config.write(config_file)
