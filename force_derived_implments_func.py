"""
Forcing derived classes to implement specific functions

Source: James Powell talk at Pydata Seattle 2017
https://www.youtube.com/watch?v=7lmCu8wz8ro
"""


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if name != "Base" and not "bar" in body:
            raise TypeError("User class must implement func `bar`")
        return type.__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def __init_subclass__(self, *a, **kw):
        print("init_subclass", a, kw)
        return super().__init_subclass__(*a, **kw)


class BadDerived(Base):
    pass


class GoodDerived(Base):
    def foo(self):
        pass
