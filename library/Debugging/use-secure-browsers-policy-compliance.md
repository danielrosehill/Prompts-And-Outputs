---
title: "Use secure browsers policy compliance"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The error you're seeing—**"Access blocked: does not comply with use secure browsers policy"**—is related to **Cloudflare's "Secure Browser" policy**, which enforces certain security standards for browsers accessing Cloudflare-protected applications. This typically happens when the browser (or app) doesn't meet Cloudflare's criteria for "secure browsing," such as:

1. **Browser Version**: The browser might be outdated.
2. **Security Features**: The browser might not have certain security features enabled (e.g., TLS 1.2+, cookies, JavaScript).
3. **Browser Integrity Check**: Cloudflare might be checking for the browser's integrity, and something about your client isn't passing the test.

### Steps to Fix the "Use Secure Browsers" Policy Issue:

#### 1. **Check Browser Compatibility and Update**:
   - Ensure that you're using an **up-to-date browser**. If this is happening on a mobile device, update your browser (Chrome, Firefox, etc.) to the latest version from the Google Play Store or App Store.
   - If you’re using an app like **Home Assistant** that embeds a web view for authentication, ensure that your system WebView component is up to date as well.

   On Android, you can update **Android System WebView** via the Google Play Store:
   - Go to **Play Store** and search for **Android System WebView**.
   - Update if there's a new version available.

#### 2. **Check Security Features (Cookies, JavaScript)**:
   - Ensure **cookies** and **JavaScript** are enabled in your browser. Some secure browser checks require that both of these features are active.
   - For Chrome/Firefox, go to the settings and ensure cookies and JavaScript are allowed.

#### 3. **Disable Browser Integrity Check in Cloudflare Access**:
   If the above steps don't resolve the issue, and you're still encountering problems, you may need to adjust the **Browser Integrity Check** in Cloudflare Access.

   Here's how to disable or adjust it:

   1. **Log in to Cloudflare Dashboard**.
   2. Go to **Access > Applications** and select the application in question.
   3. Under **Policies**, look for a setting or rule related to **Browser Integrity Checks** or **Secure Browser Enforcement**.
   4. You can try disabling this check temporarily to see if it resolves the issue.

#### 4. **Review Secure Browser Policy in Cloudflare for Teams**:
   If you're using **Cloudflare for Teams** with **Browser Isolation** or **Secure Browser policies**, review the policies set up for the application:

   1. Navigate to **Teams Dashboard > Settings > Secure Browsers**.
   2. Review the settings and make sure the policy isn't overly restrictive for your environment.
   3. Consider adjusting the policy to allow a broader range of browsers or devices.

#### 5. **Use a Supported Browser or Device**:
   Cloudflare's **Secure Browser policy** may only allow certain browsers (like Chrome or Firefox) that meet their security criteria. If you're using an embedded browser in an app or an unsupported browser, try accessing the application from a **supported browser**.

#### 6. **Testing with Different Devices**:
   - Try accessing the resource from another device, such as a different computer or mobile device, to see if the issue persists across multiple devices or if it’s isolated to one.

### Conclusion:
- **Update your browser or WebView component** on your device.
- Ensure **cookies** and **JavaScript** are enabled.
- If needed, **disable Browser Integrity Check** in Cloudflare Access or adjust the **Secure Browser policy**.
- Test access using a different device or browser.

These steps should help you resolve the **"does not comply with use secure browsers policy"** error and allow access to your Cloudflare-protected application.