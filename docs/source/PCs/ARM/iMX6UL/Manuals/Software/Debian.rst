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

**PREBUILT FILES PACKAGE:**

:download:`prebuilt-cs10600u070v1-debian-emmc-20210201.tar.gz <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6UL/7/Debian8.10/prebuilt-cs10600u070v1-debian-emmc-20210201.tar.gz>`

-----

.. centered:: Table of Contents

.. contents::
   :depth: 2
   :backlinks: top
   :local:

-----

.. sectnum::
   :start: 1
   :suffix: .

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

Prepare a power supply unit (PSU) with proper voltages, as follows: for 7" products, a 6V to 36V PSU is required. 10" and larger products need PSU with 
15V to 36V. USB to serial cable is used for debugging Chipsee Industrial Panel PCs (IPC). The TF card is used to create a bootable storage medium for 
reflashing the system.

Use the prebuilt images package from the :ref:`link above <db_pkg>` to reflash the system. You can use the Xshell terminal emulator to debug Chipsee IPC 
in Windows. You can also use VNC\ |r| Viewer to control Chipsee IPC remotely, over Ethernet. 
The Cross-toolchain software is used to compile the program for flashing.
 
Hardware Requirements
---------------------

* Chipsee Industrial Embedded Computer
* PSU according to the instructions above
* USB-to-serial or other serial cable for debugging
* TF Card (at least 4GB)

Software Requirements
---------------------

* Prebuilt Images Package (from the link above)
* Xshell or similar terminal emulation software
* Cross-toolchain
* VNC-Viewer

Debug
=====

This document uses XShell terminal emulation software to debug Chipsee IPC. However, you can use other tools as well, 
such as SecureCRT or Minicom.

Serial Debug
------------

The explanation of the debugging process covers the use of the first serial port (serial port 1), which consists of **RS232_1_TXD**, 
**RS232_1_RXD** and, **GND** terminals. Please refer to :ref:`1.6.1. RS232/485/CAN <RS232/485/CAN>` chapter in the EPC/PPC-A7-70HB-C 
documentation for additional information on the correct pinout.

More detailed information on how to connect different Chipsee IPCs to a PC can also be found in the following PDF document: 

:download:`How to Connect Board by Serial.pdf </Media/How_To_Connect_Board_By_Serial.pdf>`  

After connection is successfully established, set up the Xshell terminal as shown in figures below:

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_01.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_01.jpg

   Figure 1: Add Session

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_02.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_02.jpg

   Figure 1a: Session Properties

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_03.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_03.jpg

   Figure 1b: Serial Debug

SSH Debug
---------

Connect the Chipsee IPC to the Internet, and get the IP address. Then, config Xshell, or use the SSH tool on Linux PC host, directly.
In this manual, we will cover Xshell SSH debugging. 

First, we need to add one new session, as shown in *Figure 1*. The new session has to be set as in *Figure 2*, below:

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_04.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_04.jpg

   Figure 2: SSH Settings

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_05.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_05.jpg

   Figure 2a: SSH Debug

VCN Debug
---------

You can use VNC Viewer in Windows to control Chipsee IPC over Ethernet, as mentioned above.

* Use xShell serial or SSH connection to Chipsee IPC, login by Chipsee
* Log in using the commands below
* The default login credentials are: *chipsee/chipsee*

.. container:: hatnote hatnote-gray
   
  | $ x11vnc -storepasswd
  | - -set password for VNC-Viewer access--
  | $x11vnc -display :0 -forever -bg -rfbauth /home/chipsee/.vnc/passwd -rfbport 5900 
  | -o /home/chipsee/.vnc/x11vnc.log

* Use VNC Viewer in Windows to control it over Ethernet, as shown in figures 2b, 2c, and 2d.

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_06.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_06.jpg

   Figure 2b: VNC Viewer Connect

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_07.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_07.jpg

   Figure 2c: Authentication

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_08.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_08.jpg

   Figure 2d: VNC Desktop

Downloading Images
==================

The Chipsee industrial embedded computer supports booting from an integrated eMMC or external TF card (also known as micro SD card).
Booting from an external TF card allows flashing the system OS.

DIP Switch Configuration
------------------------

Set the boot DIP switch as shown in *Figure 3* to boot the system from the external TF Card.

.. figure:: /Media/ARM/A7/Debian/Debian_Shot_09.jpg
   :align: center
   :figclass: align-center
   :target: ../../../../../_images/Debian_Shot_09.jpg

   Figure 3: Boot Mode Setup

Prebuilt Files Package
----------------------

As mentioned before, you can get the prebuilt file package from the :ref:`link <db_pkg>` at the beginning of this documentation.
You can also get the prebuilt file package from /Debian8.10/Prebuilts folder on DVD. However, it may be outdated so always compare the 
versions (the last number in the filename is the release date). Typically, the content of the prebuilt package has the structure as in 
*Table 1* below:

.. table:: Table 1: Prebuilt Files Package
  :width: 100%
  :align: center
  

  +----------------------------------------+--------------------------------------+
  | Contents                               | Comment                              |
  +========================================+======================================+
  | boot/imx6ulipc.dtb                     | TF Card boot dtb file                |
  +----------------------------------------+--------------------------------------+
  | boot/u-boot.imx                        | TF Card boot bootloader              |
  +----------------------------------------+--------------------------------------+
  | boot/zImage                            | TF Card boot kernel file             |
  +----------------------------------------+--------------------------------------+
  | filesystem/rootfs-emmc-flasher.tar.bz2 | TF Card boot rootFS                  |
  +----------------------------------------+--------------------------------------+
  | mksdcard.sh                            | Shell tools to make bootable TF Card |
  +----------------------------------------+--------------------------------------+
  | README                                 | Simple guidelines                    |
  +----------------------------------------+--------------------------------------+
  | S1.jpg                                 | Boot Switch Config Figure            |
  +----------------------------------------+--------------------------------------+
  | emmc-flash/emmc/rootfs.tar.gz          | RootFS in target eMMC                |
  +----------------------------------------+--------------------------------------+
  | emmc-flash/emmc/u-boot.imx             | Bootloader in target eMMC            |
  +----------------------------------------+--------------------------------------+
  | emmc-flash/emmc/zImage                 | Kernel file in target eMMC           |
  +----------------------------------------+--------------------------------------+
  | emmc-flash/emmc/imx6ul-eisd.dtb        | dtb file in target eMMC              |
  +----------------------------------------+--------------------------------------+
  | emmc-flash/mkemmc.sh                   | Shell tools to download images       |
  +----------------------------------------+--------------------------------------+
  
  
  
  