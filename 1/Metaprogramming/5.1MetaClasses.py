import time
def get_instantiation_time(cls):
    print(cls.instantiation_time)

class My_Meta(type):
    instantiated_by = []
    def __new__(mcs, name, bases, dictionary):
        if 'instantiation_time' not in dictionary:
            dictionary['instantiation_time'] = time.time()
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        My_Meta.instantiated_by.append(name)
        return obj


class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def get_instantiation_time(self):
        print('Ha no time for you!')

myobj1 = My_Class1()
myobj1.get_instantiation_time() #This instance got 'get_instantiation_time' method from metaclass
myobj2 = My_Class2()
myobj2.get_instantiation_time() #This instance got 'get_instantiation_time' by definition