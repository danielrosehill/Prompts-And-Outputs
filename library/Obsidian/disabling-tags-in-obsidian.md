---
title: "Disabling tags in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

In Obsidian, there isn't a built-in feature to entirely disable tags globally, but you can effectively ignore them or hide them with a few workarounds:

# Output

In Obsidian, there isn't a built-in feature to entirely disable tags globally, but you can effectively ignore them or hide them with a few workarounds:

### 1. **Avoid using tags**  
The simplest way is just not to use tags in your notes. If you don't create any `#tags`, then they won't appear. This doesn't disable tags but prevents them from showing up in your workflow.

### 2. **Hide tags with CSS**  
If you'd like to keep tags in your notes but just not see them in the Obsidian interface, you can hide them with a custom CSS snippet. Here’s how:

- Go to **Settings > Appearance > CSS snippets**.
- Create a new snippet and add the following CSS code:

```css
/* Hide tags in editor */
.cm-s-obsidian span.cm-hashtag {
  display: none;
}

/* Hide tags in preview mode */
.markdown-preview-view .hashtag {
  display: none;
}
```

- Save the snippet, then enable it in the **CSS Snippets** settings.

This will hide tags from both the editor and preview modes while still allowing the tag functionality to remain active in the background.

### 3. **Use Plugins**  
There are third-party plugins that allow you to manage tags or customize how they appear. You might explore Obsidian's plugin marketplace to see if there's a plugin that meets your needs.

While these methods don't "disable" tags completely, they can help remove them visually from your workspace.

# Avoiding hashtag tag autopopulate dialog

How about this. I don't wash obsidian to think I'm adding a tag when I type a hashtag. Can that behavior be changed?

# Output

Currently, Obsidian automatically recognizes anything with a `#` as a tag, and there's no built-in way to prevent this behavior. However, you can try the following workarounds to avoid Obsidian treating hashtags as tags when typing:

### 1. **Escape the hashtag**  
You can type a backslash (`\`) before the hashtag to prevent Obsidian from recognizing it as a tag. For example:

```
\#notatag
```

This will display the `#` symbol without Obsidian turning it into a tag.

### 2. **Use a code block or inline code**  
If you want to write a hashtag without it becoming a tag, you can wrap the text in backticks, which formats it as code:

````
`#notatag`
````

This will prevent Obsidian from treating the hashtag as a tag, and the hashtag will just be displayed as plain text.

### 3. **Modify tag behavior via plugin**  
While there’s no native option to stop Obsidian from interpreting `#` as a tag, there may be third-party plugins that can be customized or modified to change the behavior of tags. You can explore the plugin marketplace to see if any plugins allow you to customize tag recognition.

At the moment, using backslashes or code blocks is the most effective way to prevent Obsidian from recognizing hashtags as tags.