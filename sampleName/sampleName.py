import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MALE_NAME_FILE = os.path.join(BASE_DIR, "male.json")
FEMALE_NAME_FILE = os.path.join(BASE_DIR, "female.json")


class SampleName:

    def __init__(self):
        # TODO 加上可讀取自訂名稱 JSON 檔
        # TODO class variable -> list 長度
        self._loadNameList()

    def _loadNameList(self):
        '''
        instance 建立時載入名稱檔案, 不要每次呼叫 function 才讀取 JSON
        '''
        with open(MALE_NAME_FILE, 'r', encoding='utf-8') as file:
            self._male_name_list = json.loads(file.read())

        with open(FEMALE_NAME_FILE, 'r', encoding='utf-8') as file:
            self._female_name_list = json.loads(file.read())

    def listName(self, length) -> list:
        '''
        隨機取得男生/女生英文名字
        '''

    def listNameCht(self, length) -> list:
        '''
        隨機取得男生/女生英文名字翻譯
        '''

    def listMaleName(self, length) -> list:
        '''
        隨機取得男生英文名稱
        '''

    def listMaleNameCht(self, length) -> list:
        '''
        隨機取得男生英文名字翻譯
        '''

    def listFemaleName(self, length) -> list:
        '''
        隨機取得女生英文名字
        '''

    def listFemaleNameCht(self, length) -> list:
        '''
        隨機取得女生英文名字翻譯
        '''
