from collections import namedtuple
from ctypes import Structure, POINTER, cast, c_ssize_t, c_void_p, py_object


SizeCapacity = namedtuple('SizeCapacity', ('size', 'capacity'))


class PyListObject(Structure):
    _fields_ = [
        ('ob_refcnt', c_ssize_t),
        ('ob_type', c_void_p),
        ('ob_size', c_ssize_t),
        ('ob_item', POINTER(py_object)),
        ('allocated', c_ssize_t),
    ]
    pass


def listobject(l):
    return cast(id(l), POINTER(PyListObject)).contents


def size_capacity(l):
    c_l = listobject(l)
    return SizeCapacity(c_l.ob_size, c_l.allocated)


def avg(l):
  return float(sum(l)) / float(len(l))


def repeat(stmt, setup, repeat=1000):
   return avg(timeit.repeat(stmt, setup, number=1, repeat=repeat))


def bits(n):
    return bin(n + 2 ** 63)[2:].zfill(64)


'''
categories = ['food', 'tacos', 'bar', 'dentist', 'scuba diving']
print(size_capacity(categories))

categories = []
categories.append('food')
categories.append('tacos')
categories.append('bar')
categories.append('dentist')
categories.append('scuba diving')

c_categories = listobject(categories)
print(size_capacity(categories))

ints = [i for i in range(5)]
print(size_capacity(ints))

ints = list([0, 1, 2, 3, 4])
print(size_capacity(ints))
'''
