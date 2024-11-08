---
title: "Android URL opening rule for specific LAN IP and port"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Port

On Android, I'd like to setup a rule. If a URL is received with the following pattern 192.168.1.1:3100 It should open in a specific app (A Hermit web app). Is there a way to configure a rule like this?

# Output

To set up a rule on Android that opens a specific URL pattern (`192.168.1.1:3100`) in a **Hermit web app**, you can try the following approaches:

### **1. Using Tasker to Create a Custom URL Handler**
**Tasker** is a powerful automation app that can be used to intercept specific URLs and open them in a designated app.

#### **Steps:**
1. **Install Tasker**:
   - Download **Tasker** from the Google Play Store.
2. **Create a Profile**:
   - Open Tasker and create a new **Profile**:
     1. Tap the **“+”** button.
     2. Choose **Event** > **System** > **Notification**.
     3. Set the **Owner Application** to your messaging app (or the app that will receive the URL).
3. **Set Up the Task**:
   - Create a **Task** to handle the event:
     1. Add a **“Variable Search Replace”** action to extract the URL from the message.
     2. Use conditions to match the **URL pattern** (`192.168.1.1:3100`).
     3. Add an **Action**:
        - **“Launch App”**: Choose the Hermit web app where you want to open the URL.
4. **Set Hermit to Open Specific URL**:
   - In Tasker, use the **“Send Intent”** action to send a URL directly to **Hermit**:
     ```bash
     Action: android.intent.action.VIEW
     Data: http://192.168.1.1:3100
     Package: com.chimbori.hermitcrab
     ```
   - Replace the URL and **Hermit** package name as needed.

#### **Limitations**:
- You will need to customize the **intent action** if Hermit does not support `VIEW` intents directly.
- Tasker is **paid**, but it allows for highly configurable automation.

### **2. Use Android’s Built-in App Linking**
Android can be configured to **open certain URLs directly** in specific apps using **intent filters**. This may require custom setup within Hermit if not supported out of the box:

#### **Option A: Configure Intent Filters**
1. **Check Hermit App Settings**:
   - Open **Hermit** and see if there’s an option to configure **Custom URL Handling** or **Open URL Patterns**. This is often found in web app settings, and you can specify a URL pattern to handle directly within Hermit.
2. **Set Hermit as Default for the URL**:
   - Go to **Android Settings** > **Apps** > **Default apps** > **Opening links**.
   - Find **Hermit** and add **“Open supported links”** if this is available.

#### **Option B: Modify Hermit Configuration (Advanced)**
You can set up **Hermit Lite Apps** (custom web apps) to open a specific URL pattern:
1. **Open Hermit** and **Create a Lite App** for `192.168.1.1:3100`.
2. **Add a Custom Intent Filter**:
   - Check if Hermit allows you to specify which URLs the Lite App should intercept.

### **3. Using Automate (Alternative to Tasker)**
If you prefer not to use Tasker, **Automate** is a free alternative:
1. **Install Automate** from the Play Store.
2. **Create a Flow**:
   - Start a **new flow** that listens for **Notification Events** containing your URL pattern.
   - Add an **HTTP Intent** step that redirects to **Hermit** when it detects `192.168.1.1:3100`.

### **Summary**
1. **Tasker** is your best bet if you want **highly customized** automation to open specific URLs. You can create a rule that detects `192.168.1.1:3100` and triggers **Hermit** to open it.
2. **Android App Linking** might work if Hermit supports URL filters, allowing you to register Hermit as the default for specific patterns.
3. **Automate** can be a free alternative to Tasker and offers similar capabilities for creating custom rules.

These approaches should enable you to configure Android to **automatically open URLs** following the pattern `192.168.1.1:3100` in Hermit. Let me know if you need more details on any specific setup!