#!/usr/bin/env python

import subprocess

count = 1000

for index in range(1, count+1):
    process = subprocess.Popen("/bin/bash", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, encoding='utf8')
    proc_stdout = process.communicate(input = "source ./vars; ./build-key --batch cie%d" %(index))
    print(proc_stdout)
