# PCAN-Basic Python playground

When using Linux, it is not necessary to install additional drivers
in order to use the <a href="https://www.peak-system.com/PCAN-USB.199.0.html">PCAN-USB CAN adapter</a>.
However, when using Windows, it is: The "PCAN-Basic" driver/API must be used then.
Driver and API are available on the Peak website.
In order to being able to write Python applications running both with Linux and Windows,
I am in this repository attempting to get said API to work,
first the .so with Linux
and then the .dll with Windows,
hoping that they work with identical API calls.

## Getting the API

Run ./download.sh from the root folder of the repository, it will download the necessary files from Peak, apply my patches and compile it.

## Requirements

 * Python 3.4 or higher
 * tk
 * <a href="https://packages.debian.org/stretch/tix">tix</a>
 * <a href="https://packages.debian.org/stretch/libpopt-dev">libpopt-dev</a>
 * <a href="https://packages.debian.org/jessie/gcc-4.9">GCC Version 4.9 (6 and 7 will fail, see issue #2)</a>

## License
The software within this repository is published under the terms and conditions of the GNU GPLv3.
Please note, that this does not necessarily apply to software or libraries, that this software depends on.
