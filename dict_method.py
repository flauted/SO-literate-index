#!/usr/bin/env python
import numpy as np
import timeit
from settings import NUM_CLASSES, HEADER, NUM_PROFILES

classes = {head: idx for (idx, head) in enumerate(HEADER.split())}


def make_label():
    _label = np.zeros([NUM_CLASSES])
    _label[[classes["Young"], classes["Bald"], classes["Chubby"]]] = True
    return _label


if __name__ == "__main__":
    print(timeit.timeit(make_label, number=NUM_PROFILES))
    print(dir(classes))
