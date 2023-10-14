#!/usr/bin/env python

from unscramble import apply_changes, transform_data
import struct
from solution import *

def main():
    IN = './main'
    OUT = './main.bad'

    apply_changes(IN, OUT, mangle_header)

def mangle_header(data):
    ELF_MAGIC_BYTES = ['%', 'P', 'D', 'F', '-', 2]
    data = transform_data(data, \
            ELF_MAGIC_OFFSET, ELF_MAGIC_BYTES)

    # orig entry_point
    ELF_ENTRY_BYTES = list(struct.pack('<Q', 0x1122334455667788))
    data = transform_data(data, \
            ELF_ENTRY_OFFSET, ELF_ENTRY_BYTES)

    return data

if __name__ == '__main__':
    main()
