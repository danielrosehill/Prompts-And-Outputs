---
title: "Can you create your own benchmark suite in Phoronix"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great! Is it possible to create my own suite of tests so that I can run these tests repeatedly without needing to run the same commands? And do you have an approximate for how long it might take?

# Output

Certainly! To ensure that your custom test suite in the **Phoronix Test Suite** runs with anonymization enabled, you'll need to specify the `--anonymize` flag in the test commands within your suite configuration. Here’s how to modify your custom suite configuration to include anonymization.

### **Updated Suite Configuration with Anonymization**

1. **Edit Your Suite Configuration**: Open the XML file for your custom suite that you previously created:

   ```bash
   nano ~/.phoronix-test-suite/test-suites/my-custom-btrfs-suite.xml
   ```

2. **Add Anonymization to the Tests**: Modify the XML structure to include the `--anonymize` flag for each test. Here's an example of how to structure it:

   ```xml
   <phoronix-test-suite>
       <tests>
           <test name="disk">
               <options>--anonymize</options>
           </test>
           <test name="btrfs">
               <options>--anonymize</options>
           </test>
           <test name="fio">
               <options>--anonymize</options>
           </test>
           <test name="cpio">
               <options>--anonymize</options>
           </test>
           <test name="btrfs-compression">
               <options>--anonymize</options>
           </test>
           <test name="mdadm">
               <options>--anonymize</options>
           </test>
           <test name="system">
               <options>--anonymize</options>
           </test>
           <test name="sqlite">
               <options>--anonymize</options>
           </test>
           <test name="dd">
               <options>--anonymize</options>
           </test>
       </tests>
   </phoronix-test-suite>
   ```

3. **Save and Exit**: Save the changes and exit the text editor.

### **Running the Custom Suite with Anonymization**
Now, when you run your custom suite, the `--anonymize` flag will be applied to each test, ensuring that any sensitive information is not included in the results.

To run the suite, use the following command:
```bash
phoronix-test-suite run my-custom-btrfs-suite
```

### **Summary**
- You can include the `--anonymize` flag in your custom suite configuration to ensure that results do not contain sensitive information.
- After saving your changes, running the suite will automatically anonymize the results.

Let me know if you need any further assistance or adjustments!