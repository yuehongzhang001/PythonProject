# -*- coding: utf-8 -*-
import sys
def log(level, *args,**kvargs):
    def inner(func):
        def wrapper(*args,**kvargs):
            print level,'before calling ',func.__name__
            print level,'args',args,'kvargs',kvargs
            func(*args,**kvargs)
            print level,'after calling ',func.__name__
        return wrapper
    return inner

@log(level='info')
def hello(name,age):
    print 'hello',name,age

def Log(func):
    def wrapper(name,age):
        print 'before calling ',func.__name__
        func(name,age)
        print 'after calling ',func.__name__
    return wrapper()
#hello(name='jay',age=11)

