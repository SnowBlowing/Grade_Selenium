#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/21  16:5
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import sqlite3
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')
path = config.get('excel', 'path')


class SQL:
    def __init__(self):
        self.conn = sqlite3.connect('../database/student_grade.db')  # 链接数据库
        self.cursor = None  # 游标对象
        self.results = None  # 查询结果
        self.cursor = self.conn.cursor()  # 创建游标对象
        self.create_table()  # 创建grade表
        self.readExcel()

        self.info_num = 0

    # 创建表
    def create_table(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS grade  (
              name TEXT NULL DEFAULT '?',
              exam_id TEXT NULL DEFAULT '?',
              idcard TEXT NULL DEFAULT '?',
              chinese TEXT NULL DEFAULT '?',
              math TEXT NULL DEFAULT '?',
              english TEXT NULL DEFAULT '?',
              physics TEXT NULL DEFAULT '?',
              chemistry TEXT NULL DEFAULT '?',
              political TEXT NULL DEFAULT '?',
              history TEXT NULL DEFAULT '?',
              geography TEXT NULL DEFAULT '?',
              biology TEXT NULL DEFAULT '?',
              level_pol TEXT NULL DEFAULT '?',
              level_his TEXT NULL DEFAULT '?',
              level_physics TEXT NULL DEFAULT '?',
              level_chem TEXT NULL DEFAULT '?',
              level_geo TEXT NULL DEFAULT '?',
              level_bio TEXT NULL DEFAULT '?',
              physical TEXT NULL DEFAULT '?',
              comprehensive TEXT NULL DEFAULT '?',
              experiment TEXT NULL DEFAULT '?',
              music_art TEXT NULL DEFAULT '?',
              total TEXT NULL DEFAULT '?'
            )
            '''
        )

    def readExcel(self):
        # 读取 Excel 文件，仅选择 'name' 、 'exam_id' 和 'idcard' 列的数据
        excel_data = pd.read_excel(path, usecols=['name', 'exam_id', 'idcard'])

        # 读取已存在的 grade 表的数据
        existing_data = pd.read_sql_query('SELECT * FROM grade', self.conn)

        # 合并已存在的数据和新的数据，使用 'name' 、 'exam_id' 和 'idcard' 列进行连接
        # 注意how为left,excel写在exist前才能保持顺序不变
        merged_data = pd.merge(excel_data, existing_data, how='left', on=['name', 'exam_id', 'idcard'])

        # 选择除了 'name' 、 'exam_id' 和 'idcard' 列以外的其他列
        other_columns = existing_data.columns.difference(['name', 'exam_id', 'idcard'])

        # 将其他列的数据保持不变
        for column in other_columns:
            merged_data[column] = existing_data[column]

        # 将合并后的数据写入数据库的 grade 表中
        merged_data.to_sql('grade', self.conn, index=False, if_exists='replace', schema='main', method='multi',
                           chunksize=500)

    def insert_grade(self, student):
        # 插入数据
        self.cursor.execute(
            '''
                INSERT INTO grade (chinese, math, english, physics, chemistry, political, history, geography, biology, 
                level_pol, level_his, level_physics, level_chem, level_geo, level_bio, physical, comprehensive,
                experiment, music_art, total) 
                VALUES (
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT)
                )
            '''
            , (student.chinese, student.math, student.english, student.physics, student.chemistry, student.political,
               student.history, student.geography, student.biology, student.level_pol, student.level_his,
               student.level_physics, student.level_chem, student.level_geo, student.level_bio, student.physical,
               student.comprehensive, student.experiment, student.music_art, student.total)
        )

    # 提交事务
    def commit(self):
        self.conn.commit()

    def select_grade(self):
        # 查询数据
        self.cursor.execute('SELECT * FROM grade')
        # 获取查询结果
        self.results = self.cursor.fetchall()

    # 获取数据总数
    def get_info_num(self):
        self.select_grade()
        for row in self.results:
            self.info_num += 1

    # 关闭连接
    def close_connection(self):
        self.conn.close()
