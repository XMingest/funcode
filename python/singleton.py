import functools
import threading


def singleton(cls):
    cls.__instance = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(clazz, *args, **kwargs):
        # 同步锁
        with threading.Lock():
            it = clazz.__dict__.get('__it__')
            if it is not None:
                return it
            clazz.__it__ = it = clazz.__instance(clazz, *args, **kwargs)
            it.__init_original__(*args, **kwargs)
            return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__
    return cls
