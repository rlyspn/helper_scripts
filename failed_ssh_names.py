#!/usr/bin/python

from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import re

fileName = "/var/log/auth.log"
tell = "input_userauth_request: invalid user"
min_count = 3
title = "Failed SSH Log In Names (count > %d)" % min_count

def get_name_count(input_file, nc):
    with open(input_file) as f:
        for line in f:
            if tell in line:
                line = re.sub('\s{2,}', ' ', line)
                name = line.split(' ')[8]
                nc[name] += 1
    return nc


name_count = defaultdict(int)
name_count = get_name_count(fileName, name_count)
name_count = get_name_count(fileName + '.1', name_count)
names = name_count.items()
names = [x for x in names if x[1] > min_count]
names = sorted(names, key=lambda x: x[1])
print names

x_val = [x[0] for x in names]
y_val = [y[1] for y in names]

print x_val
print y_val

width = 0.35
ind = np.arange(len(y_val))
fig = plt.figure()
ax = plt.subplot(111)
ax.bar(ind, y_val, width=.35)

plt.title(title);
plt.ylabel("Count")
plt.xlabel("Names")
plt.xticks(ind + width / 2.0, x_val, rotation=90)
plt.show()
