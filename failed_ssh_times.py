#!/usr/bin/python

from collections import defaultdict
import matplotlib.pyplot as plt
import re

log_file = "/var/log/auth.log"
tell = "input_userauth_request: invalid user"

def get_hour_count(input_file, hc):
    with open(log_file) as f:
        for line in f:
            if tell in line:
                line = re.sub('\s{2,}', ' ', line)
                match = re.search('(\d{1,2}):\d{1,2}:\d{1,2}', line)
                if match:
                    hour = match.group(1)
                    hc[hour] += 1
    return hc


hour_count = defaultdict(int)
hour_count = get_hour_count(log_file, hour_count)
hour_count = get_hour_count(log_file+'.1', hour_count)
hours = hour_count.items()
hours = sorted(hours, key=lambda x: int(x[0]))
print hours

x_val = [x[0] for x in hours]
y_val = [y[1] for y in hours]

plt.plot(x_val, y_val)

plt.title("Failed SSH Connections Through The Day")
plt.ylabel("Number of failed connections")
plt.xlabel("Time of Day")

plt.show()
