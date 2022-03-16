from abc import ABCMeta, abstractmethod
import copy


class CoursesPrototype(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self): pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Python(CoursesPrototype):
    def __init__(self):
        super().__init__()
        self.type = 'Python Basic and Algorithm'

    def course(self):
        print(' Inside Python :: course() method ')


class Java(CoursesPrototype):
    def __init__(self):
        super().__init__()
        self.type = 'Java Basics and Spring Boot'

    def course(self):
        print(' Inside Python :: course() method. ')


class R(CoursesPrototype):
    def __init__(self):
        super().__init__()
        self.type = "R programming language"

    def course(self):
        print(' Inside Python :: course() method. ')


class CoursesCache:
    cache = {}

    @staticmethod
    def get_course(sid):
        course = CoursesCache.cache.get(sid, None)
        return course.clone()

    @staticmethod
    def load():
        python = Python()
        python.set_id('1')
        CoursesCache.cache[python.get_id()] = python

        java = Java()
        java.set_id('2')
        CoursesCache.cache[java.get_id()] = java

        r = R()
        r.set_id('3')
        CoursesCache.cache[r.get_id()] = r


if __name__ == '__main__':
    CoursesCache.load()

    Python = CoursesCache.get_course('1')
    print(Python.get_type())

    Java = CoursesCache.get_course('2')
    print(Java.get_type())

    R = CoursesCache.get_course('3')
    print(R.get_type())
