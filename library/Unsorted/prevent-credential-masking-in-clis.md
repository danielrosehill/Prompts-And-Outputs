---
title: "Prevent credential masking in CLIs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

is there any way to prevent a CLI from masking my password entry ? It makes it very hard to tell if it's being pasted correctly from my clipboard? I'm using the b2 cli

# Output

If you're having trouble pasting your password into the B2 CLI and want to see the input, you can temporarily disable password masking. Here's a workaround to help with this:

### Use a Script to Input Password

1. **Create a Script:**
   You can create a simple script to handle the password input without masking it.

   ```bash
   #!/bin/bash
   echo -n "Enter your password: "
   read password
   b2 authorize-account <accountId> "$password"
   ```

2. **Run the Script:**
   Save the script as `auth.sh`, make it executable, and run it:

   ```bash
   chmod +x auth.sh
   ./auth.sh
   ```

This approach allows you to see your input and ensures that the password is correctly captured from your clipboard.

### Alternative: Use Environment Variables

Another method is to use environment variables to pass your credentials, which avoids direct input:

1. **Set Environment Variables:**

   ```bash
   export B2_APPLICATION_KEY_ID="your_key_id"
   export B2_APPLICATION_KEY="your_key"
   ```

2. **Authorize with CLI:**

   ```bash
   b2 account authorize
   ```

This way, you bypass manual input entirely, reducing the chance of errors when pasting.

 ****