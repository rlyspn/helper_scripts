#!/bin/bash

adb root
sleep 6
adb remount
sleep 2
source build/envsetup.sh
mmm frameworks/base
sleep 3
adb push out/target/product/crespo/system/framework/framework.jar /system/framework
sleep 5
adb reboot-bootloader
sleep 5
fastboot erase userdata
sleep 5
fastboot flash userdata out/target/product/crespo/userdata.img
sleep 5
fastboot reboot
