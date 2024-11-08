---
title: "App for running multiple instances of Perplexity"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Chrome allows you to create Chrome Apps which are essentially embedded virtual "apps" of websites. I use one for accessing Perplexity AI a lot. However, it's not perfect. I frequently need to run multiple instances of it to keep several chats going. A better solution would be to build my own desktop GUI which would allow me to open new instances of the embedded app easily. I'd like to have a sidebar where I could toggle between the different instances. And I guess I'd need (ideally) to have this integrated with Google Chrome so that it can read the cache and recognise that I'm already logged in. I use Fedora Linux. What do you think of this idea? Would it be a lot of effort to develop?

# Output

Your idea for creating a custom desktop application to manage multiple instances of Perplexity AI is interesting and could potentially enhance your workflow. Let's break down the feasibility and considerations for developing such an application:

## Concept Evaluation

The concept of creating a desktop GUI with a sidebar to manage multiple instances of a web application is sound and could indeed provide a more streamlined experience compared to using multiple Chrome Apps.

## Development Approach

There are a few potential approaches to developing this application:

### 1. Chrome App or Extension

While this wouldn't fully meet your requirements, it's worth noting that you could potentially create a Chrome App or Extension that manages multiple instances of Perplexity AI within Chrome itself[1]. However, this might not provide the level of customization and integration you're looking for.

### 2. Electron-based Application

Electron allows you to build cross-platform desktop applications using web technologies (HTML, CSS, and JavaScript). This approach would allow you to:

- Create a custom UI with a sidebar
- Embed multiple instances of Perplexity AI
- Potentially integrate with Chrome's cache (though this would require careful consideration of security implications)

### 3. Go-based Application with Web View

Using a framework like Guark, you could create a desktop application using Go for the backend logic and web technologies for the UI[4]. This approach would allow you to:

- Build a native application for Fedora Linux
- Use web technologies for the UI, including the sidebar and embedded web views
- Potentially have more low-level control for integrating with the system

## Development Effort

The development effort required would depend on your experience level and the approach you choose:

1. For an experienced web developer, creating an Electron-based application could be relatively straightforward, potentially taking a few weeks to develop a basic version.

2. Using Go with a framework like Guark might require more time, especially if you're not familiar with Go, but could result in a more performant application.

3. Integrating with Chrome's cache and login state would add complexity and potential security concerns, regardless of the approach chosen.

## Considerations

1. **Security**: Accessing Chrome's cache and login state from an external application raises security concerns and may not be advisable or easily achievable.

2. **Performance**: Running multiple instances of a web application can be resource-intensive. You'll need to consider memory usage and performance optimization.

3. **Updates**: You'll need to design the application to handle updates to Perplexity AI's web interface.

4. **Cross-platform**: While you mentioned Fedora Linux, consider whether you might want to use this on other platforms in the future.

## Conclusion

Creating a custom desktop application to manage multiple Perplexity AI instances is feasible and could potentially improve your workflow. However, it would require a significant development effort, especially to create a polished, secure, and performant application.

For a proof of concept, you might consider starting with an Electron-based application that simply embeds multiple instances of Perplexity AI without trying to integrate with Chrome's cache. This would allow you to validate the usefulness of the concept before investing in more complex development.

 