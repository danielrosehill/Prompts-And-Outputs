---
title: "How to set up Newsboat with my sources"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please provide me with a guide to how to set up newsboat
I have a number of RSS feeds I would like to monitor, but they belong to different categories:
Israel news (English)
Israel news (Hebrew)
World news
World newswires

In each category I have a number of RSS feeds. 

Once I this setup I would like to share my config on github so that others can copy it if they wish. But of course, I don't want to commit and share anything private. 

# Output

Setting up **Newsboat** to monitor different categories of RSS feeds is straightforward, and once set up, you can easily share your configuration via GitHub. Here’s a step-by-step guide to help you:

### Step 1: Install Newsboat on Fedora

To install Newsboat, run the following command:
```bash
sudo dnf install newsboat
```

### Step 2: Organize Your Feeds with Categories (Tags)

Newsboat uses a file called `urls` (located at `~/.newsboat/urls`) to manage your RSS feeds. You can categorize feeds using **tags** to group them based on your interests.

#### 1. **Create the `urls` File**:

Open or create the `urls` file:
```bash
nano ~/.newsboat/urls
```

#### 2. **Add Feeds by Category**:

For each category, you can add feeds and tag them. The format for adding feeds is:
```
<feed-url> <tag>
```

Let’s say you want to organize your feeds into **Israel News (English)**, **Israel News (Hebrew)**, **World News**, and **World Newswires**. Here’s an example:

##### Example of `~/.newsboat/urls`:
```txt
# Israel News (English)
https://www.jpost.com/Rss/RssFeedsHeadlines.aspx israel_english
https://www.timesofisrael.com/feed/ israel_english

# Israel News (Hebrew)
https://www.ynet.co.il/Integration/StoryRss2.xml israel_hebrew
https://www.haaretz.co.il/cmlink/1.1458916 israel_hebrew

# World News
https://feeds.bbci.co.uk/news/rss.xml world_news
https://rss.cnn.com/rss/edition.rss world_news

# World Newswires
https://www.reuters.com/rssFeed/worldNews world_newswires
https://www.apnews.com/apf-topnews?format=rss world_newswires
```

- **Tags**: The tags (`israel_english`, `israel_hebrew`, `world_news`, `world_newswires`) are used to group the feeds. You can filter by tags inside Newsboat to show only feeds from a specific category.

Save and exit (`CTRL + O`, `CTRL + X`).

### Step 3: Configuring Newsboat's Behavior (Optional)

You can configure various aspects of how Newsboat behaves by editing the `config` file located in `~/.newsboat/config`.

1. **Open the config file**:
   ```bash
   nano ~/.newsboat/config
   ```

2. **Customize settings** (optional, some examples):
   - Set the **browser** you want to open articles with:
     ```bash
     browser "firefox %u"
     ```
   - Customize the **number of articles** per feed to load:
     ```bash
     max-items 100
     ```
   - Set **article sort order** (newest first):
     ```bash
     article-sort-order date-desc
     ```

Save and exit.

### Step 4: Sync and Refresh Feeds in Newsboat

1. **Open Newsboat**:
   ```bash
   newsboat
   ```

2. **Refresh feeds** by pressing `r`. The feeds will now be organized and displayed according to their tags.

### Step 5: Filter by Tags Inside Newsboat

You can filter your feeds by their **tags**. For example, if you only want to see **Israel News (English)**, press `/` (search) inside Newsboat and type the tag name `israel_english`. This will only show feeds with that tag.

You can toggle tags back and forth or show all feeds by pressing `Esc` after filtering.

### Step 6: Set Up Git to Share the Config

To share your config files with others, you can upload the `urls` and `config` files to a GitHub repository.

#### 1. **Create a Dotfiles Directory**:

Since you may want to share multiple configurations (not just Newsboat), it’s a good idea to create a `dotfiles` directory:
```bash
mkdir ~/Git/dotfiles
mv ~/.newsboat ~/Git/dotfiles/newsboat
```

#### 2. **Create Symlinks** to Keep Your Setup Working:
Since you moved the `.newsboat` folder to `~/Git/dotfiles`, you need to create a symlink so Newsboat still works:
```bash
ln -s ~/Git/dotfiles/newsboat ~/.newsboat
```

#### 3. **Initialize a Git Repository**:
Move to your `dotfiles` directory and initialize a Git repo:
```bash
cd ~/Git/dotfiles
git init
```

#### 4. **Add `.gitignore` to Exclude Private Data**:
Before committing, create a `.gitignore` file to exclude any private or sensitive data (e.g., `cache.db`, queues, etc.):

```bash
nano ~/Git/dotfiles/newsboat/.gitignore
```

Example `.gitignore` for Newsboat:
```txt
cache.db
queue
downloaded-enclosures
```

Save and exit.

#### 5. **Commit the Newsboat Configuration**:
```bash
cd ~/Git/dotfiles
git add newsboat/
git commit -m "Add Newsboat config"
```

#### 6. **Push to GitHub**:
Create a repository on GitHub (called `dotfiles` or `newsboat-config`, for example) and add the remote:
```bash
git remote add origin https://github.com/yourusername/newsboat-config.git
git branch -M main
git push -u origin main
```

### Step 7: Cloning and Sharing

Now that your dotfiles repository is on GitHub, anyone can clone it and replicate your Newsboat configuration.

1. **Clone your dotfiles repository** on a new machine:
   ```bash
   git clone https://github.com/yourusername/newsboat-config.git ~/Git/dotfiles
   ```

2. **Create a symlink to `.newsboat`**:
   ```bash
   ln -s ~/Git/dotfiles/newsboat ~/.newsboat
   ```

### Summary of Steps:
1. **Install Newsboat**.
2. **Organize feeds by category** in `~/.newsboat/urls` using tags.
3. **Configure behavior** in `~/.newsboat/config`.
4. **Move `.newsboat` into a `dotfiles` directory** and create a symlink.
5. **Use Git** to commit the config and push it to GitHub.
6. **Add a `.gitignore`** to prevent sharing private or unnecessary files.
7. **Share your config** by pushing it to GitHub and cloning it on other machines.

This setup allows you to easily monitor RSS feeds in categories like **Israel News**, **World News**, etc., and share your Newsboat configuration with others in a clean, organized way!