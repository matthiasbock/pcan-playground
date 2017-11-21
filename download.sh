#!/bin/bash

wget -c http://www.peak-system.com/produktcd/Develop/PC%20interfaces/Linux/PCAN-Basic_API_for_Linux/PCAN_Basic_Linux-4.2.0.tar.gz
tar -xzf PCAN_Basic_Linux-4.2.0.tar.gz

# Applying patch to Makefile
patch -p0 < p1.patch

# Compile .so
cd PCAN_Basic_Linux-4.2.0/pcanbasic
make && ln -s libpcanbasic.so ../..
cd ../..

wget -c https://www.peak-system.com/fileadmin/media/files/pcan-basic.zip
unzip -o pcan-basic.zip -d PCAN_Basic

# Necessary in order to enable import
echo > PCAN_Basic/__init__.py

