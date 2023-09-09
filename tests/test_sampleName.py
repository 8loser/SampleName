import pytest
import random
from sampleName import SampleName


def test_listMaleName():
    sampleNameInst = SampleName()
    length = random.randint(1, 10)
    assert len(sampleNameInst.listMaleName(length)) == length


def test_listMaleName_failed():
    sampleNameInst = SampleName()
    with pytest.raises(TypeError):
        sampleNameInst.listMaleName('test')
