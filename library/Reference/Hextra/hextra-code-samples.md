---
title: "Code Samples"
---

## Menu block

For `hugo.yaml`:

```
menu:
  main:
    - name: Documentation
      pageRef: /docs
      weight: 1
    - name: Blog
      pageRef: /blog
      weight: 2
    - name: About
      pageRef: /about
      weight: 3
    - name: Search
      weight: 4
      params:
        type: search
    - name: GitHub
      weight: 5
      url: "https://github.com/imfing/hextra"
      params:
        icon: github
```

## Syntax for adding images with captions

```
![landscape](https://picsum.photos/800/600 "Unsplash Landscape")
```

Internal linking

```
![Daniel's weird sloth photos](/images/sloth.png "Happy sloth guy")
```
