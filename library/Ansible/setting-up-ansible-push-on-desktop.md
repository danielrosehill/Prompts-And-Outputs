---
title: "Setup guide for an Ansible push automation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please give me a guide to how to set up Ansible on my desktop. I'd like to capture my current system configuration as a playbook and then sync that to Github. I can pull down that playbook to my laptop later. Today, let's just focus on the first part

# Output

Certainly! I'll guide you through setting up Ansible on your Fedora desktop, capturing your current system configuration as a playbook, and syncing it to GitHub. Here's a step-by-step guide:

## 1. Install Ansible

First, let's install Ansible on your Fedora desktop:

```bash
sudo dnf install -y ansible
```

## 2. Create an Ansible Playbook

Now, let's create a playbook to capture your current system configuration. We'll create a file named `capture_config.yml` in your home directory:

```bash
nano ~/capture_config.yml
```

Copy and paste the following content into the file:

```yaml
---
- name: Capture Current System Configuration
  hosts: localhost
  tasks:
    - name: Get installed packages
      command: dnf list installed
      register: installed_packages
      changed_when: false

    - name: Save installed packages list
      copy:
        content: "{{ installed_packages.stdout }}"
        dest: ~/ansible_packages.txt

    - name: Backup common configuration files
      copy:
        src: '{{ item }}'
        dest: ~/ansible_configs/{{ item | basename }}
      with_items:
        - ~/.bashrc
        - ~/.vimrc
        # Add other config files as needed
```

Save and exit the editor (in nano, press Ctrl+X, then Y, then Enter).

## 3. Run the Playbook

Execute the playbook to capture your current system configuration:

```bash
ansible-playbook ~/capture_config.yml
```

This will create two files:
- `~/ansible_packages.txt`: A list of installed packages
- `~/ansible_configs/`: A directory containing copies of your configuration files

## 4. Set Up Git Repository

Now, let's set up a Git repository to store your Ansible playbook:

```bash
# Initialize a new Git repository
cd ~
git init

# Create a .gitignore file
echo "ansible_packages.txt" > .gitignore
echo "ansible_configs/" >> .gitignore

# Add the playbook to Git
git add capture_config.yml .gitignore

# Commit the changes
git commit -m "Add Ansible playbook for system configuration capture"
```

## 5. Create a GitHub Repository

Go to GitHub and create a new repository. Do not initialize it with a README, .gitignore, or license.

## 6. Push to GitHub

After creating the repository on GitHub, push your local repository:

```bash
# Add the GitHub remote (replace YOUR_USERNAME and YOUR_REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

You may need to authenticate with GitHub. If you haven't set up SSH keys, you might be prompted for your GitHub username and password.

## 7. Verify

Check your GitHub repository to ensure the playbook has been pushed successfully.

That's it! You've now set up Ansible on your desktop, created a playbook to capture your system configuration, and synced it to GitHub. You can later pull this playbook down to your laptop to replicate the configuration.

Remember to update the playbook as you make changes to your system configuration. You can add more tasks to the playbook to capture additional settings or installed software as needed.
