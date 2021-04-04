# -*- coding: utf-8 -*-

from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender, Gender):
            self._gender = gender
        elif isinstance(gender, str):
            if not gender in Gender.__members__: raise ValueError(r"'gender'参数非法")
            self._gender = Gender[gender]
        elif isinstance(gender, int):
            if not gender in set(g for g in Gender.value):raise ValueError(r"'gender'参数非法")
            self._gender = Gender(gender)
        else:
            raise ValueError(r"'gender'参数非法")

    @property
    def gender(self):
        return self._gender
    
# 测试:
# bart = Student('Bart', Gender.Male)
# bart = Student('Bart', 0)
bart = Student('Bart', 'Male')
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')