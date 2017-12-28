#!/usr/bin/env python

import numpy as np
import enum
import timeit
from settings import NUM_CLASSES, HEADER, NUM_PROFILES

Classes = enum.IntEnum("Classes", HEADER)


def make_label():
    _label = np.zeros([NUM_CLASSES])
    _label[[feat-1 for feat in
           [Classes.Young, Classes.Bald, Classes.Chubby]]
           ] = True
    return _label


if __name__ == "__main__":
    print(timeit.timeit(make_label, number=NUM_PROFILES))
    print(dir(Classes))
