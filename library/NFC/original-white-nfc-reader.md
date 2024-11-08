---
title: "Original (white) NFC reader"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


ACR122U PICC Interface
Manufacturer: ACS
Speed: 12Mb/s (full)
Bus:   1
Address:  13
USB Version:  1.10
Device Class: 00
Device Subclass: 00
Device Protocol: 00
Maximum Default Endpoint Size: 8
Number of Configurations: 1
Vendor Id: 072f
Product Id: 2200
Revision Number: 02.14

Config Number: 1
	Number of Interfaces: 1
	Attributes: 80
	MaxPower Needed: 200mA

	Interface Number: 0
		Name: pn533_usb
		Alternate Number: 0
		Class: 0b
		Sub Class: 00
		Protocol: 00
		Number of Endpoints: 3

			Endpoint Address: 02
			Direction: out
			Attribute: 2
			Type: Bulk
			Max Packet Size: 64
			Interval: 0ms

			Endpoint Address: 81
			Direction: in
			Attribute: 3
			Type: Interrupt
			Max Packet Size: 8
			Interval: 50ms

			Endpoint Address: 82
			Direction: in
			Attribute: 2
			Type: Bulk
			Max Packet Size: 64
			Interval: 0ms