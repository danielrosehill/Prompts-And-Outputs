---
title: "USB command to retrieve your USB hubs and data rates"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To summarize: you're asking for a command that can list your USB devices, their types (e.g., USB 2.0, USB 3.0), and their maximum data rates.

You can retrieve this information using a combination of commands. Here's how you can achieve this:

### 1. **Using `lsusb` with `t` (tree) option**
The `lsusb -t` command gives you a tree structure of connected USB devices, including the USB speed and type (e.g., USB 2.0, USB 3.0).

- Run this command:
  ```bash
  lsusb -t
  ```

  This will display a tree view of your USB devices and their corresponding **speed**, such as 480M (USB 2.0), 5000M (USB 3.0), or 10000M (USB 3.1).

  Example output:
  ```
  /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
      |__ Port 2: Dev 3, If 0, Class=Mass Storage, Driver=usb-storage, 5000M
  /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 480M
      |__ Port 1: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 12M
  ```

  - **480M**: USB 2.0
  - **5000M**: USB 3.0
  - **10000M**: USB 3.1

### 2. **Using `lsusb -v` for Detailed Information**
The `lsusb -v` (verbose) option gives detailed information about each device, including the **speed** and **bMaxPacketSize** (maximum data rate).

- Run the following command:
  ```bash
  lsusb -v | grep -E 'Bus|bcdUSB|bMaxPacketSize0|bDeviceProtocol'
  ```

This will output detailed information about the USB protocol version (`bcdUSB`) and packet size, which indicates the **type** of USB device (e.g., 2.0, 3.0).

### 3. **Using `udevadm` for USB Speed and Type**
You can use `udevadm` to show detailed information about each USB device, including **speed**, **protocol version**, and **type**.

- To get information about all USB devices, run:
  ```bash
  udevadm info -a -p /sys/bus/usb/devices/usbX
  ```
  Replace `usbX` with the specific USB device number you want to inspect (e.g., `usb1`, `usb2`). You can find the device numbers from the `lsusb` output.

  This will show you detailed attributes of the device, including speed.

### 4. **Using `dmesg` for USB Device Initialization**
When a USB device is connected