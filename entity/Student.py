# -*- coding: utf-8 -*-
# @Time    : 2023/7/8  15:08
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe:
class Student:
    def __init__(self, name='', exam_id='', idcard='', chinese='', math='', english='', physics='', chemistry='',
                 political='', history='', geography='', biology='', level_pol='', level_his='', level_physics='',
                 level_chem='', level_geo='', level_bio='', physical='', comprehensive='', experiment='', music_art='',
                 total=''):
        # 基本信息
        self.name = name
        self.exam_id = exam_id
        self.idcard = idcard

        # 成绩信息
        self.chinese = chinese
        self.math = math
        self.english = english
        self.physics = physics
        self.political = political
        self.chemistry = chemistry
        self.geography = geography
        self.history = history
        self.biology = biology
        self.level_pol = level_pol
        self.level_his = level_his
        self.level_physics = level_physics
        self.level_chem = level_chem
        self.level_geo = level_geo
        self.level_bio = level_bio
        self.physical = physical
        self.comprehensive = comprehensive
        self.experiment = experiment
        # self.computer = computer
        self.music_art = music_art
        self.total = total

