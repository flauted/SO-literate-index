#!/usr/bin/env python
import numpy as np
import collections
import timeit
from settings import NUM_CLASSES, HEADER, NUM_PROFILES

Classes = collections.namedtuple("Classes", HEADER)

clss = Classes._make(range(NUM_CLASSES))


def make_label():
    _label = np.zeros([NUM_CLASSES])
    _label[[clss.Young, clss.Bald, clss.Chubby]] = True
    return _label


if __name__ == "__main__":
    print(timeit.timeit(make_label, number=NUM_PROFILES))
    print(dir(clss))
