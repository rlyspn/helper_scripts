#!/bin/bash

app=$1

source build/envsetup.sh

mmm packages/apps/$1

adb root
sleep 3
adb remount
sleep 3
adb shell rm /data/app/$app.apk
adb push out/target/product/crespo/data/app/$app.apk /data/app
