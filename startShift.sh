#!/bin/bash

# New York City - 40.71 north : 74.00 west
# Day Temp - 5500k
# Night Temp - 4000k

redshift -l 40.71:74.00 -t 5500:4000 &
