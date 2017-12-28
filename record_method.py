#!/usr/bin/env python
import numpy as np
import timeit
from settings import HEADER, NUM_PROFILES, NUM_CLASSES

h_split = HEADER.split()
header_rec = np.array([tuple(range(len(h_split)))],
                      dtype=list(zip(h_split, [int]*len(h_split))))


def make_label():
    _label = np.zeros([NUM_CLASSES])
    _label[[header_rec[key].item() for key in ["Young", "Bald", "Chubby"]]] = True
    return _label


def make_label_slow():
    return np.in1d(header_rec.item(), [header_rec[key].item() for key in ["Young", "Bald", "Chubby"]]).astype(int)


if __name__ == "__main__":
    print(timeit.timeit(make_label, number=NUM_PROFILES))
    print(dir(header_rec))
