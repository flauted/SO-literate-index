#!/usr/bin/env python
import numpy as np
import timeit
from settings import HEADER, NUM_PROFILES, NUM_CLASSES


class dotdict(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__.update({k: v for k, v in self.items()})

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self.__dict__.update({key: value})

    __getattr__ = dict.__getitem__
    __setattr__ = __setitem__
    __delattr__ = dict.__delitem__


classes = dotdict({head: idx for (idx, head) in enumerate(HEADER.split())})


def make_label():
    _label = np.zeros([NUM_CLASSES])
    _label[[classes["Young"], classes["Bald"], classes["Chubby"]]] = True
    return _label


if __name__ == "__main__":
    print(timeit.timeit(make_label, number=NUM_PROFILES))
    print(dir(classes))
