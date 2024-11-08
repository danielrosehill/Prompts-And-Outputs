---
title: "Provisioning storage outside of the actual case"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt**: You are asking if it’s possible to connect drives to your motherboard via SATA, while storing them outside the case, potentially with an independent power supply.

Yes, it is possible to connect drives externally to your motherboard via **SATA** and power them with an independent power supply. This can be achieved with a few different setups. Here's how:

### 1. **SATA to eSATA (External SATA)**
   - **Overview**: **eSATA** is an external version of SATA that allows you to connect external drives directly to your motherboard using a SATA port.
   - **Setup**: You can install an eSATA bracket or use a backplate adapter that connects your internal SATA port to an eSATA port on the back of your case. Then, use eSATA cables to connect external drives to this port.
   - **Power Supply**: eSATA does not carry power, so you would need to power the drives separately, either using an external power adapter designed for the hard drive or an enclosure that provides power.
   - **Example**: eSATA enclosures or standalone drives with independent power supplies are common for this use case.

### 2. **SATA to External Enclosure**
   - **Overview**: Use a **SATA-to-external enclosure** setup where you place your drives in an external enclosure that supports SATA connections. Many enclosures have independent power supplies and use USB or eSATA to connect back to your PC.
   - **Setup**: The enclosure holds your drives and has an external power supply. You can connect the drives to your motherboard via a **SATA extension cable** or **eSATA**, depending on the enclosure.
   - **Power Supply**: Most external enclosures provide their own power, meaning your drives are powered independently from the PC.

### 3. **SATA Extension Cables + External Power Supply**
   - **Overview**: You can use **SATA extension cables** to run from your motherboard's internal SATA ports to outside the case. Then, you can power the drives using a separate power source.
   - **Setup**: 
     - Use SATA extension cables that pass through an unused PCI slot or a cutout in your case.
     - Connect the drives to these external SATA cables.
     - Use a standalone **HDD power supply** to power the drives (such as external AC adapters made for SATA hard drives).
   - **Power Supply**: There are various adapters available that convert wall power to the necessary SATA power connector (often a 12V adapter). These can provide power to the drives independently of your computer’s power supply.

### 4. **Drive Docking Station with SATA Interface**
   - **Overview**: A **drive docking station** allows you to connect SATA drives externally, often via USB or eSATA. Some advanced models may even have a SATA passthrough to connect directly to your motherboard.
   - **Setup**: Place your hard drives in a docking station with its own power supply. The station connects back to your motherboard via eSATA, USB, or Thunderbolt depending on the model.
   - **Power Supply**: Most docking stations come with their own power adapters, eliminating the need to rely on your PC’s power supply.

### 5. **PCIe to SATA Expansion with External Drive Capability**
   - **Overview**: Some **PCIe SATA expansion cards** support external connections, allowing you to add additional SATA ports that can be routed to external drives.
   - **Setup**: Install a PCIe card with SATA connectors and route them to drives outside the case using SATA cables.
   - **Power Supply**: Drives connected this way can be powered externally using independent power sources.

### Conclusion:
You can connect external drives to your motherboard using SATA by:
- Using **eSATA** for direct SATA connections.
- **SATA extension cables** for external setups with independent power.
- Placing drives in **external enclosures** or **docking stations** with their own power supplies.

This method allows you to take full advantage of your motherboard's available SATA ports while storing drives externally. Let me know if you need help with a specific setup!