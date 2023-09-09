import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MALE_NAME_FILE = os.path.join(BASE_DIR, "male.txt")
FEMALE_NAME_FILE = os.path.join(BASE_DIR, "female.txt")


class SampleName:

    def listName(self, length=8):
        '''
        取得男生/女生名字隨機
        '''

    def listMaleName(self, length=8):
        '''
        取得男生名稱清單
        '''

    def listFemaleName(self, length=8):
        '''
        取得女生名字清單
        '''
