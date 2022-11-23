import time
class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'instantiation_time' not in dictionary:
            dictionary['instantiation_time'] = time.time()