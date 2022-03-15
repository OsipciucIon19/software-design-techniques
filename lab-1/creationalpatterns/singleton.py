class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    obj1 = Singleton()
    print(obj1)

    obj2 = Singleton()
    print(obj2)
