---
title: "How to use Lighthouse to check the responsiveness of a site"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To use **Lighthouse** to check the responsiveness of a website, you can follow these steps. Lighthouse is a tool built into Chrome that audits websites for performance, accessibility, best practices, SEO, and more. One key metric it evaluates is **responsiveness**, which is part of its **Performance** and **Best Practices** audits.

Here’s a step-by-step guide to using Lighthouse for checking the responsiveness of a website:

### Step 1: Open Chrome DevTools
1. Open Google Chrome and navigate to the website you want to test.
2. Right-click on the page and select **Inspect** to open Chrome DevTools, or press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac).

### Step 2: Access Lighthouse in DevTools
1. In Chrome DevTools, click on the **Lighthouse** tab at the top. If you don't see it, click on the double arrow (`>>`) to find it in the hidden menu.
2. The Lighthouse panel will open, showing options for different audits you can run on the website.

### Step 3: Configure Lighthouse Audit for Responsiveness
1. **Device type**: Select **Mobile** or **Desktop** depending on which responsiveness you want to test. For responsive web design, you’ll typically want to select **Mobile** to ensure the site adapts well to smaller screens.
   
2. **Categories**: Make sure that **Performance** and **Best Practices** are checked, as these will help assess responsiveness. You can also select other categories like **SEO** and **Accessibility** if you're auditing for those aspects as well.

### Step 4: Run the Lighthouse Audit
1. Once you’ve configured the options, click the **Generate report** button at the bottom of the Lighthouse panel.
2. Lighthouse will then audit the website and generate a report.

### Step 5: Review the Report
After the report is generated, it will show you several metrics that directly relate to **responsiveness**:

- **First Contentful Paint (FCP)**: Measures how long it takes for the first piece of content to appear on the screen.
- **Largest Contentful Paint (LCP)**: Measures how long it takes for the largest visible element on the page to be rendered. A good LCP score means your site loads content quickly, which is essential for responsiveness.
- **Cumulative Layout Shift (CLS)**: Measures the visual stability of a webpage. A low CLS score means elements don’t shift unexpectedly, which contributes to a responsive user experience.
- **Interaction to Next Paint (INP)**: This measures the responsiveness of interactions, showing how quickly the site reacts to user input, which is crucial for good responsiveness on mobile devices.
- **Viewport Meta Tag**: Checks if the website is using the viewport meta tag to properly scale and size the page across different devices.
- **Responsive Images**: Lighthouse will audit whether images are being properly resized and served for different device sizes.

### Step 6: Analyze Responsiveness Issues
Lighthouse may flag issues related to responsiveness, such as:

- **Viewport not configured**: If the page doesn’t set the viewport meta tag correctly for mobile devices, it will alert you.
- **Content wider than screen**: If elements are overflowing the viewport, this will appear as an issue.
- **Tap targets not sized appropriately**: If buttons and other interactive elements are too small or too close together, making them hard to tap on mobile devices.
- **Serve images in next-gen formats**: Ensures that images are optimized for mobile and desktop, contributing to faster load times and better responsiveness.

### Step 7: Adjust and Re-Test
After reviewing the issues, you can fix the responsiveness issues in your code, then re-run the Lighthouse audit to ensure improvements. Lighthouse will show you improved scores for responsiveness-related metrics after implementing changes.

---

### Key Metrics for Responsiveness in Lighthouse
- **First Contentful Paint (FCP)**
- **Largest Contentful Paint (LCP)**
- **Cumulative Layout Shift (CLS)**
- **Time to Interactive (TTI)**
- **Interaction to Next Paint (INP)**

These metrics together give you a holistic view of how responsive your website is on both mobile and desktop.

By following these steps, you can effectively use Lighthouse to check and improve the responsiveness of your website.