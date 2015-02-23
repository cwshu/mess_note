#!/usr/bin/env python3
import sys

num = int(sys.argv[1])
file_arr = []
for i in range(num):
    file_arr.append(open("tmp" + str(i), "w"))
