#!/bin/bash

# Download PCANBasic Linux API
curl -L -C - http://www.peak-system.com/produktcd/Develop/PC%20interfaces/Linux/PCAN-Basic_API_for_Linux/{PCAN_Basic_Linux-4.2.0.tar.gz} -o "#1"
tar -xzf PCAN_Basic_Linux-4.2.0.tar.gz

# Apply patches
patch -p0 < p1.patch
patch -p0 < p2.patch

# Compile .so
cd PCAN_Basic_Linux-4.2.0/pcanbasic
make && ln -s libpcanbasic.so ../..
cd ../..


# Download PCANBasic Linux Driver
curl -L -C - http://www.peak-system.com/fileadmin/media/linux/files/{peak-linux-driver-8.5.1.tar.gz} -o "#1"
tar -xzf peak-linux-driver-8.5.1.tar.gz

# Apply patches
patch -p0 < p3.patch

# Compile driver
cd peak-linux-driver-8.5.1/
make
cd ..


# Download PCANBasic Windows API
curl -L -C - https://www.peak-system.com/fileadmin/media/files/{pcan-basic.zip} -o "#1"
unzip -o pcan-basic.zip -d PCAN_Basic

# Enable import in Python scripts
echo > PCAN_Basic/__init__.py

