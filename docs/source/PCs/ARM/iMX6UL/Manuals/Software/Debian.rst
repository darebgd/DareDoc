Debian 8.10
###########

.. centered:: Chipsee IMX6UL Debian8.10 User Manual

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

.. table::
   :align: center
   :width: 100%

   +----------+-----------+--------+-----------------+
   | Revision |    Date   | Author |   Description   |
   +==========+===========+========+=================+
   |   V1.0   | 2018-4-14 |  Madi  | Initial Version |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

CS10600U070-V1.0

.. _db_pkg:

**PREBUILT IMAGES PACKAGE:**

:download:`prebuilt-cs10600u070v1-debian-emmc-20210201.tar.gz <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6UL/7/Debian8.10/prebuilt-cs10600u070v1-debian-emmc-20210201.tar.gz>`

-----

.. centered:: Table of Contents

.. contents::
   :depth: 2
   :local:

-----

.. centered:: System Features

.. table::
   :align: center
   :width: 100%

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | Kernel        | Kernel version: 3.14.52          |
   +---------------+----------------------------------+
   | Bootloader    | Uboot 2015.04                    |
   +---------------+----------------------------------+
   | System        | Debian8.10                       |
   +---------------+----------------------------------+
   | Python        | Python version: 2.7.9            |
   +---------------+----------------------------------+
   | Qt            | Need install                     |
   +---------------+----------------------------------+
   | Desktop       | lxde                             |
   +---------------+----------------------------------+
   | user/password | [root/root] or [chipsee/chipsee] |
   +---------------+----------------------------------+
   
Preparation
===========

You must prepare the power supply unit (PSU) yourself. For 7" products, a 6V to 36V PSU is required. 10" and larger products need PSU with 15V to 36V. 
USB to serial cable is used for debugging Chipsee Industrial Panel PCs (IPC). The TF card is used to create a boot card to reflash the system.

The prebuilt images package from the link above is used to reflash the system. You can use Xshell to debug Chipsee IPC in Windows.
You can also use VNC-Viewer to remote control Chipsee IPC over Ethernet. The Cross-toolchain software is used to compile the program for flashing.
 
Hardware Requirements
---------------------

* Chipsee Industrial Embedded Computer
* PSU according to the instructions above
* USB to serial or other serial cable for debugging
* TF Card (at least 4GB)

Software Requirements
---------------------

* Prebuilt Images Package (from the link above)
* Xshell or similar terminal emulation software
* Cross-toolchain
* VNC-Viewer

Debug
=====

This document uses XShell software to debug Chipsee IPC. However, you can use other tools as well, such as SecureCRT or Minicom.

Serial Debug
------------

The explanation of the debugging process covers the use of the first serial port (serial port 1), which consists of **RS232_1_TXD**, 
**RS232_1_RXD** and, **GND** terminals. Please refer to the :ref:`RS232/485/CAN` chapter in the CS10600U070 User Manual for additional
information on correct pinout.

More detailed information on how to connect different Chipsee IPCs to a PC can also be found in the following PDF document: 

:download:`How to Connect Board by Serial.pdf </Media/How_To_Connect_Board_By_Serial.pdf>`  

After connection is successfully established, set up the Xshell terminal as shown in the Figures below:


