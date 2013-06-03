#!/bin/bash

ud="userdata"
c="cache"
b="boot"
sys="system"

declare -a to_flash = ($b, $ud, $sys)
declare -a 

fastboot erase $ud
fastboot erase $c

fastboot flash $b $b.img
fastboot flash $sys $sys.img
fastboot flash $ud $ud.img
