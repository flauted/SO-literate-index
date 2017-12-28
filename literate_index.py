#!/usr/bin/env python
import timeit
import dict_method
import dotdict_method
import enum_method
import namedtuple_method
import record_method
import zero_enum_method
from settings import NUM_PROFILES


if __name__ == "__main__":
    print("\nENUM: ")
    print(timeit.timeit(enum_method.make_label, number=NUM_PROFILES))
    # (5) 0.1792
    print(dir(enum_method.Classes))
    # Passes 4 and 5, bonus for sphinx-apidoc
    # Fails 6.

    print("\nNAMEDTUPLE: ")
    print(timeit.timeit(namedtuple_method.make_label, number=NUM_PROFILES))
    # (2) 0.1355
    print(dir(namedtuple_method.clss))
    # Passes 4 and 5, bonus for sphinx-apidoc

    print("\nDICT :")
    print(timeit.timeit(dict_method.make_label, number=NUM_PROFILES))
    # (1) 0.1278
    print(dict_method.classes.keys())
    # Passes 4 well enough.
    print(dir(dict_method.classes))
    # Fails 5.

    print("\nZERO_ENUM: ")
    print(timeit.timeit(enum_method.make_label, number=NUM_PROFILES))
    # (4) 0.1726
    print(dir(zero_enum_method.Classes))
    # Passes 4 and 5, bonus for sphinx-apidoc (although numbering is off...)

    print("\nDOTDICT: ")
    print(timeit.timeit(dotdict_method.make_label, number=NUM_PROFILES))
    # (3) 0.1612
    print(dir(dotdict_method.classes))
    # Passes 4 and 5.

    print("\nRECORD: ")
    print(timeit.timeit(record_method.make_label, number=NUM_PROFILES))
    # (6) 0.1846
    print("    in1d:")
    print("   ",
          timeit.timeit(record_method.make_label_slow,
                        number=NUM_PROFILES))
    # ( :o ) 1.3123
    print(record_method.header_rec)
    # Ugly, but passes 4.
    print(record_method.header_rec.dtype)
    # Could rig it to pass 5.
