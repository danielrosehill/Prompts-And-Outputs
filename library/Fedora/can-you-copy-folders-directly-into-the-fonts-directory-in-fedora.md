---
title: "Can you copy folders directly into the fonts directory in Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You are asking if installing the entire folders (instead of just the TTF files) into `/usr/share/fonts/custom` will work for adding fonts on Fedora.

---

Yes, you can install the **entire folders** of fonts directly into `/usr/share/fonts/custom`, and it should work. The **font cache** system (`fc-cache`) will recursively scan through subdirectories, so it will detect and register any `.ttf` or `.otf` files within those folders. This method can be convenient because you won't have to manually extract or reorganize the font files.

### **Steps to Install Folders of Fonts to `/usr/share/fonts/custom`**
1. **Create the Custom Fonts Directory (If It Doesn’t Exist)**
   - Ensure that the directory `/usr/share/fonts/custom` exists:
     ```bash
     sudo mkdir -p /usr/share/fonts/custom
     ```

2. **Copy the Entire Folders to the Custom Directory**
   - You can copy your font folders (preserving the structure) directly:
     ```bash
     sudo cp -r ~/Downloads/google-fonts/* /usr/share/fonts/custom
     ```
   - The `-r` flag ensures that directories are copied recursively, so each folder with its TTF/OTF files will be moved as-is.

3. **Update the Font Cache**
   - Run the following command to refresh the system’s font cache and recognize the new fonts:
     ```bash
     sudo fc-cache -fv
     ```

### **Benefits of Installing Folders Instead of Individual Files**
- **Organized Structure:** By keeping the fonts in their original folders, you maintain a more organized structure. This can make it easier to identify or manage fonts later, especially if they come with multiple weights and styles.
- **Easy Removal:** If you need to remove a specific font later, you can simply delete the entire folder instead of hunting down individual files.

### **Verifying the Installation**
You can verify that the fonts are correctly installed by listing the registered fonts:
```bash
fc-list | grep -i "<font name>"
```
Replace `<font name>` with part of the name of the font to confirm it has been successfully added.

### **Conclusion**
Yes, you can copy the **entire folders** containing the TTF/OTF files to `/usr/share/fonts/custom`, and it will work as long as you run `fc-cache` afterward. This approach maintains the organization of your font library, making it easier to manage, and it allows the font system to recognize everything correctly.