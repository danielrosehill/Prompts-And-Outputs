---
title: "Storage upgrade planning with Claude"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt


I'm attaching my current desktop specs. You mentioned that I should be using a type of RAID for disc protection. Smart idea. Based on my current PSU and motherboard, can you suggest an optimal multi drive configuration? The NVME isn't replaceable but I could donate my SSDs. Suggest a system that would give me lots of storage capacity even after using RAID and then provide estimates as to probable costs.

# Output

Based on your current desktop specifications and the desire for a RAID setup to enhance data protection and storage capacity, I can suggest an optimal multi-drive configuration. Your motherboard, the PRO B760M-A WIFI from MSI, supports RAID 0, 1, 5, and 10 for SATA storage devices[6], which gives us several options to work with.

## Recommended RAID Configuration

Given your current setup and requirements, I recommend implementing a RAID 5 configuration using SATA SSDs. This will provide a good balance between performance, capacity, and data protection.

**RAID 5 Configuration:**
- Number of drives: 4
- Drive type: SATA SSDs
- Capacity per drive: 2TB

This setup will give you:
- Total raw capacity: 8TB
- Usable capacity: 6TB (one drive's worth of capacity is used for parity)
- Data protection: Can survive one drive failure without data loss

## Implementation Details

1. **Keep your current NVMe SSD:** Your CRUCIAL P3 1TB NVME SSD can remain as your boot drive and for frequently accessed files.

2. **Add new SATA SSDs:** Purchase four 2TB SATA SSDs for the RAID 5 array.

3. **Configuration:** Use your motherboard's RAID functionality to set up the RAID 5 array with the four new SSDs.

## Cost Estimate

Based on current market prices for SSDs[5], here's an approximate cost breakdown:

- 4 x 2TB SATA SSDs: Approximately $125-$170 each
- Total estimated cost: $500-$680

For example, the Crucial BX500 2TB Internal SSD is currently priced at $124.99[5], which would bring the total to about $500 for four drives.

## Benefits of This Configuration

1. **Data Protection:** RAID 5 provides redundancy, allowing the array to continue functioning even if one drive fails.

2. **Increased Capacity:** You'll have 6TB of usable space in the RAID array, plus your 1TB NVMe drive.

3. **Improved Performance:** RAID 5 offers better read performance compared to a single drive.

4. **Compatibility:** This setup is fully supported by your current motherboard and power supply.

## Additional Considerations

1. **Backup:** While RAID 5 provides some data protection, it's not a substitute for proper backups. Consider implementing an external backup solution as well.

2. **Power Consumption:** Your current 850W power supply (SEASONIC FOCUS GX-850) is more than capable of handling this additional load[1].

3. **Future Expandability:** This configuration leaves room for future upgrades, as your motherboard supports up to 4 SATA devices and 2 M.2 slots[6].

By implementing this RAID 5 configuration, you'll significantly increase your storage capacity while also gaining important data protection features, all within the capabilities of your current system components.

 