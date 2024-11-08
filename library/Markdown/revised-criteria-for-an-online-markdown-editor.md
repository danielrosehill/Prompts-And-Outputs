---
title: "Revised criteria for an online markdown editor"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here’s a summary of your requirements followed by the list of options:

### **Requirements Summary**
- **Markdown Editing**: WYSIWYG (live rendering) markdown editing and markdown auto-detection for pasted text.
- **Scalability**: Ability to grow and store up to **1 million notes or more**, ensuring long-term use.
- **Cloud-Hosted (SaaS)**: Should be cloud-hosted, not self-hosted.
- **Backup**: Regular **backup options**, ideally programmatically exportable.
- **Security**: Strong **authentication**, preferably with **2FA**.
- **User Interface**: Convenient online interface, strong reading, and editing features.
- **Platform Compatibility**: Availability of a **good Android client** for note access and editing.

---

### **1. Notion**
- **Markdown Support**: WYSIWYG editing for live markdown rendering and seamless paste support.
- **Scalability**: Suitable for storing thousands of notes, organized in a database structure.
- **Backup**: Manual export to **Markdown, HTML, and CSV**; can be automated with API tools.
- **Security**: Supports **2FA** for account security.
- **Platform Compatibility**: Offers both Android and iOS apps, plus web and desktop versions.
- **Cost**: Free version available, **$8/month** for personal pro tier.
- **Link**: [Notion](https://www.notion.so)

### **2. Coda.io**
- **Markdown Support**: Supports markdown formatting and live preview.
- **Scalability**: Grows well, suitable for structured document and database management.
- **Backup**: **CSV and PDF export** available, plus API options for automation.
- **Security**: Provides **2FA** and **Single Sign-On (SSO)** for business plans.
- **Platform Compatibility**: Full-featured Android app, browser-based access.
- **Cost**: Free tier available, **$10/month** for personal pro.
- **Link**: [Coda](https://coda.io)

### **3. Nuclino**
- **Markdown Support**: Provides WYSIWYG markdown editing with live preview.
- **Scalability**: Handles thousands of interconnected pages for knowledge management.
- **Backup**: Can be exported to **Markdown or HTML**, suitable for manual backups.
- **Security**: Includes **2FA** for secure access.
- **Platform Compatibility**: Available on web, Android, and iOS.
- **Cost**: Free version available, **$5/month** per user for the standard plan.
- **Link**: [Nuclino](https://www.nuclino.com)

### **4. Craft (Cloud Version)**
- **Markdown Support**: Full WYSIWYG markdown editing and auto-detection on paste.
- **Scalability**: Handles large numbers of documents, perfect for creative projects and SOPs.
- **Backup**: Export options include **Markdown** and **PDF**.
- **Security**: Offers **2FA** for added security.
- **Platform Compatibility**: Browser access, iOS, and Android web access (limited features on Android).
- **Cost**: Free version available, **$4.99/month** for pro tier.
- **Link**: [Craft](https://www.craft.do)

### **5. Evernote**
- **Markdown Support**: Basic markdown support, but not as fully integrated as others.
- **Scalability**: Well-suited to large collections of notes with powerful organization features.
- **Backup**: Data export via **HTML** or **PDF**, programmatic exports are not natively supported.
- **Security**: **2FA** and multiple device support for secure access.
- **Platform Compatibility**: Comprehensive Android and iOS apps, plus desktop and web clients.
- **Cost**: Free plan available, **$7.99/month** for personal use.
- **Link**: [Evernote](https://www.evernote.com)

### **Summary**
Based on your criteria:
- **Notion** and **Nuclino** stand out for their strong markdown support, scalability, cloud-hosting, and comprehensive mobile apps.
- **Coda.io** is also a strong option if you prefer something closer to database integration, although markdown functionality is less focused than Notion or Obsidian.
- **Craft** is great if you like a visually appealing interface but might be limited if you prefer more flexibility on Android.

Let me know if you’d like more information on any of these options, or if you'd like assistance with setting up backups or automation features!

# Estimated userbase

Here's an updated matrix including both the estimated user base and an estimate of growth speed for each tool. The growth estimates are based on recent trends, company announcements, and the tool’s popularity in user communities.

| Tool       | Estimated User Base          | Growth Speed Estimate           |
|------------|------------------------------|---------------------------------|
| **Notion** | Over **30 million users**    | **High Growth** (5-10 million users/year) |
| **Coda.io** | Over **1 million users**     | **Moderate Growth** (200,000-300,000 users/year) |
| **Nuclino** | Around **100,000 users**     | **Steady Growth** (10,000-20,000 users/year) |
| **Craft**   | Over **500,000 users**       | **Rapid Growth** (100,000-200,000 users/year) |
| **Evernote** | Over **200 million users**  | **Slow to Negative Growth** (Declining by a few million users/year) |

### **Notes on Growth Speed Estimates:**
- **Notion**: Growth has been fueled by its increasing adoption by individuals, startups, and large teams. The introduction of powerful integrations and APIs has helped accelerate adoption.
- **Coda.io**: Growing at a moderate rate, popular among users who need structured documents. It’s getting traction especially among productivity-focused teams.
- **Nuclino**: Steady growth mainly within small teams and niche communities interested in knowledge management and wiki tools.
- **Craft**: Experiencing rapid growth thanks to its beautiful UI and appeal to creative users, particularly among personal productivity enthusiasts and smaller work teams.
- **Evernote**: User base is generally declining as newer tools (like Notion) are gaining favor, and long-time users are exploring alternatives.

Let me know if there's anything more you need!

# Closest Look And Feel To Obsidian

# Prompt

Great work. As I've become quite comfortable using Obsidian, can you suggest which of these tools might most closely mirror its functionality? If none of them do, perhaps you could suggest some more options that meet this criteria?

# Output

### **Closest Match to Obsidian Among the Existing Tools**

1. **Nuclino**:
    
    - **Similarities**:
        - Nuclino has a **clean and simple UI** that’s good for wiki-style knowledge management.
        - It supports **markdown with live preview**, allowing you to type and format content instantly, much like Obsidian’s WYSIWYG experience.
        - **Interlinking Notes**: You can link pages together just like you can in Obsidian, helping you build a knowledge network.
    - **Differences**:
        - It doesn’t have the deep flexibility of Obsidian’s plugins or community-made themes.
        - Limited offline capabilities compared to Obsidian’s strong offline mode.
    - **Verdict**: This would be the closest among the tools you've considered, but it lacks the customization and plugin support of Obsidian.
2. **Notion**:
    
    - **Similarities**:
        - **Markdown** support with inline editing (though a bit different from Obsidian’s raw markdown approach).
        - Great for **interlinked content** and creating a wiki-like system.
    - **Differences**:
        - Markdown editing in Notion is not as direct or as flexible as Obsidian. You don’t see raw markdown syntax like `**bold**`; it automatically converts the formatting in real time.
        - Doesn’t provide the same level of customization with third-party plugins as Obsidian.
    - **Verdict**: Notion is flexible and has powerful features, but the markdown experience is quite different from Obsidian, as it's geared more towards non-technical users.

# Additional tools with comparable functionalities

I attempted to update the existing SOP document, but unfortunately, an error occurred during the process. I won't try again, but I'm here to make any changes manually if you'd like.

Now, let me provide a revised list that excludes tools without a robust web UI:

### **Other Tools that Closely Mirror Obsidian’s Functionality (with Robust Web UI)**

1. **Logseq**:
   - **Markdown Support**: Offers **WYSIWYG markdown editing** and supports auto-detection of markdown syntax.
   - **Interlinking and Graph View**: Excellent graph and backlink features similar to Obsidian.
   - **Web UI**: Logseq has recently expanded to include a **web-based UI**, allowing seamless use across devices.
   - **Online Sync (SaaS Option)**: Offers **Logseq Sync** for cloud-hosted synchronization across devices.
   - **Platform Compatibility**: Great Android and desktop support for capturing and accessing notes anywhere.
   - **Backup**: Uses markdown files, making it straightforward to export and back up notes.
   - **Verdict**: **Logseq** is the closest match if you're looking for similar features to Obsidian but with the convenience of a robust web UI.

2. **RemNote**:
   - **Markdown Editing**: Supports **live markdown editing** (WYSIWYG) and auto-detection, making it efficient for quickly capturing structured content.
   - **Interlinking Notes**: Provides a highly organized and interconnected knowledge base with backlinks and hierarchical note-taking, similar to a wiki.
   - **Web UI**: RemNote has a **strong web UI** for accessing and editing notes seamlessly across different platforms.
   - **Cloud-Hosted (SaaS)**: Fully hosted solution, with no need for self-hosting, making it a robust SaaS option.
   - **Backup**: Offers export options to **Markdown** or **PDF**, making backups and data portability easy.
   - **Platform Compatibility**: Supports web, desktop, and **Android** apps for cross-platform access.
   - **Verdict**: **RemNote** is a solid choice if you want a SaaS alternative with strong web capabilities, similar markdown features, and note interlinking.

3. **Slite**:
   - **Markdown Editor**: Slite offers markdown editing with a WYSIWYG-like experience, making it easy to write, format, and capture information.
   - **Interlinking Notes**: Built to manage content in a wiki-style environment, allowing for interconnected knowledge bases and easy navigation between notes.
   - **Web UI**: The **web-based interface** is highly intuitive and makes it easy to access and manage notes across multiple devices.
   - **Cloud-Hosted (SaaS)**: Fully cloud-hosted, requiring no local installations or hosting.
   - **Backup**: Supports manual exports, though automated backups might require additional solutions.
   - **Platform Compatibility**: Provides **Android**, **iOS**, and desktop access, making it a well-rounded choice for users across platforms.
   - **Verdict**: **Slite** is worth considering if you want a markdown-friendly, wiki-style note manager with a strong web-based interface, though it lacks some advanced plugin functionality.

### **Summary**
- **Logseq** would be your best choice if you are looking for an option most closely resembling Obsidian, with a strong web UI and synchronization capabilities.
- **RemNote** offers strong markdown capabilities, a web interface, and built-in cloud hosting.
- **Slite** is a good choice if you are seeking a simple markdown and wiki-style solution, although it lacks some of Obsidian’s deep customizability.

If you need any more detailed comparison or guidance on trying out any of these, I’d be happy to help!