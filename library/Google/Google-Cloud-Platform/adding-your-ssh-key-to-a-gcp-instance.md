---
title: "Adding your SSH key to a GCP instance"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

How do I add my SSH key to my GCP VM?

# output

To add your **SSH key** to your **Google Cloud VM instance**, you have two main options: adding it through the **Google Cloud Console** or via the **gcloud command-line tool**. Below are detailed steps for both methods.

---

### Option 1: **Add SSH Key via Google Cloud Console**

#### Step 1: Generate an SSH Key (If you don't already have one)
If you don’t have an SSH key pair yet, you can generate one using the following command on your local machine (Linux/macOS/Windows with WSL or Git Bash):
```bash
ssh-keygen -t rsa -f ~/.ssh/YOUR_KEY_NAME
```
This will create a **private key** (`YOUR_KEY_NAME`) and a **public key** (`YOUR_KEY_NAME.pub`).

#### Step 2: Copy Your Public Key
- Open the `.pub` file:
   ```bash
   cat ~/.ssh/YOUR_KEY_NAME.pub
   ```
- Copy the contents of the **public key** (the entire string that starts with `ssh-rsa`).

#### Step 3: Add the SSH Key to Your VM Instance
1. **Go to the Google Cloud Console**:
   - Open [Google Cloud Console](https://console.cloud.google.com).
   - Navigate to **Compute Engine** > **VM Instances**.

2. **Edit Your VM Instance**:
   - Find your VM instance and click on its name to open the instance details page.
   - Click **Edit** at the top of the instance details page.

3. **Scroll Down to the SSH Keys Section**:
   - Scroll down to the **SSH Keys** section.
   - Click **Show and edit** to reveal the section.

4. **Add Your SSH Key**:
   - Click **Add item**.
   - Paste your public SSH key (from the `.pub` file) into the provided field.
   - The format should look something like this:
     ```
     ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr... your-username
     ```
   - You can replace `your-username` with your preferred username (this will be used to connect via SSH).

5. **Save**:
   - Click **Save** at the bottom of the page to apply changes.

#### Step 4: SSH into Your VM Using Your Private Key
You can now SSH into your instance using the private key:
```bash
ssh -i ~/.ssh/YOUR_KEY_NAME your-username@EXTERNAL_IP
```
- Replace `YOUR_KEY_NAME` with the name of your private key.
- Replace `your-username` with the username specified when you added the key.
- Replace `EXTERNAL_IP` with the **external IP address** of your VM (you can find this in the VM details page).

---

### Option 2: **Add SSH Key via gcloud Command**

If you have the **Google Cloud SDK (gcloud)** installed, you can also use it to add your SSH key to your instance.

#### Step 1: Generate an SSH Key (if you don’t have one)
If you haven't already generated an SSH key, do so with:
```bash
ssh-keygen -t rsa -f ~/.ssh/YOUR_KEY_NAME
```

#### Step 2: Use gcloud to Add the Key
You can use the `gcloud` command to add your SSH key to the VM instance:
```bash
gcloud compute ssh --ssh-key-file=~/.ssh/YOUR_KEY_NAME your-username@INSTANCE_NAME --zone=ZONE
```
- Replace `YOUR_KEY_NAME` with the name of your SSH key.
- Replace `your-username` with your preferred username.
- Replace `INSTANCE_NAME` with the name of your VM instance.
- Replace `ZONE` with the zone where your instance is located (e.g., `us-central1-a`).

This command will add your public key to the instance and also directly initiate an SSH session.

---

### Option 3: **Add SSH Key via Metadata (For All Instances)**
If you want to add the same SSH key for **all instances** in a project:

1. **Go to Metadata**:
   - In the **Google Cloud Console**, navigate to **Compute Engine** > **Metadata**.

2. **Add SSH Key to Project Metadata**:
   - Click the **SSH Keys** tab.
   - Add your public key there by clicking **Edit** > **Add item**.
   - Paste your SSH key.

This will apply the SSH key to all instances in the project.

---

### Troubleshooting Tips

- **SSH Permissions**: Ensure your SSH key has the correct permissions:
  ```bash
  chmod 600 ~/.ssh/YOUR_KEY_NAME
  ```
  The private key file must not be accessible to others.

- **Firewall Rules**: Ensure that **SSH traffic** (port 22) is allowed through the firewall. In GCP, make sure your instance’s **network** has a firewall rule allowing **ingress traffic** on port 22.

---

### Conclusion
You can add an SSH key to your instance either via the **Google Cloud Console**, by using **gcloud**, or through **project metadata** for all instances. Once the key is added, you can securely SSH into your instance from your local machine.

Let me know if you run into any issues or need further assistance!