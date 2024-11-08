---
title: "Digital ocean CLI on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To install the DigitalOcean CLI (`doctl`) on Fedora, follow these steps:

### 1. Download the Latest Release
First, download the latest release of the `doctl` binary. You can do this using `curl` or `wget`.

```bash
curl -sLO https://github.com/digitalocean/doctl/releases/download/v1.99.0/doctl-1.99.0-linux-amd64.tar.gz
```

### 2. Extract the Downloaded Archive
Extract the downloaded tarball to your desired directory.

```bash
tar xf doctl-1.99.0-linux-amd64.tar.gz
```

### 3. Move the Binary to `/usr/local/bin`
Move the `doctl` binary to a directory that is in your system's PATH, typically `/usr/local/bin`.

```bash
sudo mv doctl /usr/local/bin
```

### 4. Verify the Installation
To ensure `doctl` is installed correctly, check the version:

```bash
doctl version
```

This should display the installed version of `doctl`, confirming that it's installed correctly.

### 5. Authenticate `doctl`
To use `doctl`, you'll need to authenticate it with your DigitalOcean account. Run:

```bash
doctl auth init
```

This will prompt you to enter your DigitalOcean API token, which you can generate from your DigitalOcean account under the "API" section.

Now, `doctl` should be ready to use on your Fedora system!