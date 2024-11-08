---
title: "Hextra Notes"
---

Note: these notes are primarily intended for my own reference. 

For official guidance on how to use the Hextra Hugo theme, please refere to the official documentation.

## Main Theme

 - [Theme home](https://themes.gohugo.io/themes/hextra/)

 ## Templates

 - [Hextra Starter](https://github.com/imfing/hextra-starter-template)

## Starter Templates - Key Areas

- [Content home](https://github.com/imfing/hextra-starter-template/tree/main/content)
- [Home _index.md](https://github.com/imfing/hextra-starter-template/blob/main/content/_index.md)

## Homepage _index.md markdown

```
---
title: My Site
toc: false
---

This is the landing page.

## Explore

{{< cards >}}
  {{< card link="docs" title="Docs" icon="book-open" >}}
  {{< card link="about" title="About" icon="user" >}}
{{< /cards >}}

## Documentation

For more information, visit [Hextra](https://imfing.github.io/hextra).
```

## Theme Documentation

[Hextra docs home](https://imfing.github.io/hextra/docs/getting-started/)

### Starting local dev server

```
hugo server --buildDrafts --disableFastRender
```

### Updating Hextra module to latest version

```
hugo mod get -u github.com/imfing/hextra
```

## Specifying the content directory

By default, Hextra will assume that `content` (as in, the base of that folder) is where your content 'lives'.

If you want to override that, however, you can pass the `contentDir` variable in your config file (ie, `hugo.yaml`).

## Adding images (static approach)

As this project (Daniel Goes Prompting) entails my publishing a *lot* of individual pages, the pages folder approach isn't really feasible. 

I use, instead, the `static/images/` structure which is supported in Hextra (and has the additional benefit that the images are available for any resources, so you can avoid duplicates if you need to reference the same images in different notes).

In Hugo, if you create a `static` folder at base, you can ignore that when writing paths - so resources nested under `/static/images/` can be called just as `/images/`.

## Supported shortcodes

Supported shortcodes are documented [here](https://imfing.github.io/hextra/docs/guide/shortcodes/).

There are some really great options!

### Informational callout

```
{{< callout type="info" >}}
  Please visit GitHub to see the latest releases.
{{< /callout >}}
```

### Warning callout

```
{{< callout type="warning" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
```

### Cards

```
{{< cards >}}
  {{< card link="../callout" title="Callout" icon="warning" >}}
  {{< card link="../callout" title="Card with tag" icon="tag" tag= "A custom tag" >}}
  {{< card link="/" title="No Icon" >}}
{{< /cards >}}
```
### Colum limiters for cards

```
{{< cards cols="1" >}}
  {{< card link="/" title="Top Card" >}}
  {{< card link="/" title="Bottom Card" >}}
{{< /cards >}}

{{< cards cols="2" >}}
  {{< card link="/" title="Left Card" >}}
  {{< card link="/" title="Right Card" >}}
{{< /cards >}}
```

### Cards as simple tags

No images

```
{{< cards >}}
  {{< card link="../callout" title="Card with default tag color" tag="tag text" >}}
  {{< card link="../callout" title="Card with default red tag" tag="tag text" tagType="error" >}}
  {{< card link="../callout" title="Card with blue tag" tag="tag text" tagType="info" >}}
  {{< card link="../callout" title="Card with yellow tag" tag="tag text" tagType="warning" >}}
{{< /cards >}}
```

### Accordions

```
{{% details title="Details" %}}

This is the content of the details.

Markdown is **supported**.

{{% /details %}}
```