import pytest
import random
from typing import Callable
from sampleName import SampleName


def common_list_name(func: Callable[[SampleName], list]):
    '''
    共用的測試
    '''
    length = random.randint(1, 10)
    # 輸出必須為 list
    assert isinstance(func(length), list)
    # 輸出 list length 必須跟輸入一樣
    assert len(func(length)) == length


def common_list_name_failed(func):
    '''
    共用的測試, 輸入不為 int 時是否會 raise TypeError
    '''
    with pytest.raises(TypeError):
        func('test')


def test_listName():
    sampleNameInst = SampleName()
    common_list_name(sampleNameInst.listName)
    common_list_name_failed(sampleNameInst.listName)


def test_listNameCht():
    sampleNameInst = SampleName()
    common_list_name(sampleNameInst.listNameCht)
    common_list_name_failed(sampleNameInst.listNameCht)


def test_listMaleName():
    sampleNameInst = SampleName()
    common_list_name(sampleNameInst.listMaleName)
    common_list_name_failed(sampleNameInst.listMaleName)


def test_listMaleNameCht():
    sampleNameInst = SampleName()
    common_list_name(sampleNameInst.listMaleNameCht)
    common_list_name_failed(sampleNameInst.listMaleNameCht)


def test_listFemaleName():
    sampleNameInst = SampleName()
    common_list_name(sampleNameInst.listFemaleName)
    common_list_name_failed(sampleNameInst.listFemaleName)


def test_listFemaleNameCht():
    sampleNameInst = SampleName()
    common_list_name(sampleNameInst.listFemaleNameCht)
    common_list_name_failed(sampleNameInst.listFemaleNameCht)
